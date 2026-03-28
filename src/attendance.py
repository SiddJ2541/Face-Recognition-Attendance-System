import cv2
import os
import numpy as np
from datetime import datetime

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load images
path = "dataset"
images = []
classNames = []

for file in sorted(os.listdir(path)):
    img = cv2.imread(f"{path}/{file}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Lower scaleFactor to 1.1 and minNeighbors to 4 so it's more sensitive for the training images
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        print(f"[WARNING] No face detected in {file}. This person will not be recognized!")

    for (x,y,w,h) in faces:
        face = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
        images.append(face)
        # Split by underscore to map "mayank_1", "mayank_2" all back to "mayank"
        base_name = os.path.splitext(file)[0].split('_')[0]
        classNames.append(base_name)

# Create face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train recognizer
faces = []
labels = []

for i, img in enumerate(images):
    faces.append(img)
    labels.append(i)

recognizer.train(faces, np.array(labels))

# Face detector
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Attendance function
def markAttendance(name):
    if not os.path.exists("attendance.csv"):
        with open("attendance.csv", "w") as f:
            f.write("Name,Time,Date,Day\n")

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    current_day = now.strftime("%A")

    already_marked_today = False
    
    # Safely read existing records
    with open("attendance.csv", "r") as f:
        data = f.readlines()
        for line in data[1:]:  # Skip the header
            parts = line.strip().split(",")
            # Ensure this row actually has the new Date column before checking
            if len(parts) >= 3:
                recorded_name = parts[0].strip()
                recorded_date = parts[2].strip()
                if recorded_name == name and recorded_date == current_date:
                    already_marked_today = True
                    break

    # Safely append if not recorded ON THIS EXACT DATE
    if not already_marked_today:
        with open("attendance.csv", "a") as f:
            # Ensure we start on a new line if the file didn't end with one
            if len(data) > 0 and not data[-1].endswith("\n"):
                f.write("\n")
            
            f.write(f"{name},{current_time},{current_date},{current_day}\n")

# Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face = cv2.resize(gray[y:y+h, x:x+w], (200, 200))

        label, confidence = recognizer.predict(face)

        if confidence < 80:  # Tightened threshold to 50 for strict attendance marking
            name = classNames[label].upper()
            markAttendance(name)

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(img, f"{name} ({round(confidence)})", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            cv2.putText(img, f"UNKNOWN ({round(confidence)})", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    cv2.imshow("Attendance System", img)

    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()