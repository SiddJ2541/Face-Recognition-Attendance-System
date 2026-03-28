import cv2
import os

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
path = "dataset"

name = input("Enter your name (e.g., mayank): ").lower()

print(f"Look at the camera! Capturing 5 images for {name}...")
count = 0

while True:
    success, img = cap.read()
    if not success:
        continue
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        count += 1
        # Save the captured face into the dataset folder
        cv2.imwrite(f"{path}/{name}_{count}.jpg", img[y:y+h, x:x+w])
        
        cv2.putText(img, f"Captured: {count}/5", (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Registering Face...", img)

    # Wait for 100ms between captures, or break on 'ENTER'
    if count >= 5:
        break

print(f"Success! Saved {count} images into the dataset folder.")
cap.release()
cv2.destroyAllWindows()
