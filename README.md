# 🎓 Face Recognition Attendance System
A modern Computer Vision–based attendance system that uses **OpenCV** and **face recognition techniques** to automatically detect faces using a webcam and securely log attendance records in real time.

## 🚀 Features & Recent Upgrades

- 📷 **Real-time Face Detection:** Utilizes tuned Haar cascades from a live webcam feed.
- 🧠 **High-Accuracy LBPH Recognition:** Advanced OpenCV LBPH algorithm with lowered distance thresholds to prevent false positives and "Unknown" mismatches.
- 🎯 **Automated Registration Script (`register_face.py`):** A custom tool that rapidly extracts optimal face crops directly from your webcam to massively improve training robustness.
- 📅 **Date & Day Tracking:** CSV logs are now meticulously tracked by `Name, Time, Date, Day`.
- 🛡️ **Smart Anti-Spam Logging:** Intelligently logs a person only *once per day* to prevent thousands of identical webcam frames from spamming the CSV log. 
- 🪟 **Real-time Confidence Metrics:** The live video feed dynamically displays name labels alongside the exact mathematical "Distance Score" and clearly highlights `UNKNOWN` entities in red.
- 💻 **Cross-Platform File Safety:** Bulletproof CSV read/write mechanisms securely evade common Windows Python file-pointer bugs.

## 🛠️ Technologies Used

- Python 3.10
- OpenCV (`opencv-contrib-python`)
- NumPy
- Computer Vision (Face Detection + Face Recognition)
- Haar Cascade Classifier
- LBPH Face Recognizer

## 📂 Project Structure
```text
Face-Recognition-Attendance-System/
│
├── dataset/                     # Directory storing registered face images
│   ├── mayank_1.jpg             # Auto-generated optimal face crops
│   ├── aditya.jpeg
│   └── ...
│
├── src/
│   └── attendance.py            # Main real-time AI recognition engine
│
├── register_face.py             # Script to effortlessly capture facial datasets
├── attendance.csv               # Secured database of strictly-formatted logs
├── requirements.txt             # Project dependencies (OpenCV, NumPy, etc.)
└── README.md                    # Detailed documentation
```

## 🔗 Live Demo
👉 Run the project locally using the steps below.

## 🧠 How It Works
1. **Register Faces:** Run `python register_face.py`, punch in a name, and look at the camera. The script effortlessly pulls 5 perfectly-cropped facial snapshots directly into the `dataset` folder.
2. **Start Recognition:** Run `python src/attendance.py`.
3. The AI scans the dataset, standardizes filenames, trains the LBPH model, and launches the webcam automatically.
4. The system locates faces in real time and calculates their metric similarity.
5. If the model distance score passes the strict authenticity threshold:
   - Green bounding box with Name and Confidence Score appears.
   - Attendance is seamlessly appended to the `attendance.csv` file (only once per day).
6. If the face fails the threshold requirement:
   - A red bounding box alerts you of an `UNKNOWN` entity and displays their poor score for calibration debugging.

## ▶️ How to Run the Project

**Step 1:** Clone the repository
```bash
git clone https://github.com/your-username/Face-Recognition-Attendance-System.git
```

**Step 2:** Open the project folder
```bash
cd Face-Recognition-Attendance-System
```

**Step 3:** Create and activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**Step 4:** Install required libraries
```bash
pip install -r requirements.txt
```

**Step 5:** Register a New Face
```bash
python register_face.py
```

**Step 6:** Start the Attendance System
```bash
python src/attendance.py
```

## 🧾 Output Example (attendance.csv)
```csv
Name,Time,Date,Day
MAYANK,14:58:21,2026-03-27,Friday
SHIVAM,15:03:40,2026-03-27,Friday
```

## 📚 Applications
- College & School attendance systems
- Office employee authentication
- Smart classroom systems
- Identity verification projects

## 🚀 Future Improvements
- Add GUI using Tkinter
- Store attendance in a Database
- Improve accuracy using Deep Learning
- Add student ID system
- Deploy as a web-based application

## 👨‍💻 Author
**Mayank Gomase**  
*Computer Vision Mini Project*
