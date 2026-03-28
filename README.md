# 🗣️ Verbatim  
### Real-Time ASL Translation with Audio-Reactive Visualization  

---

## 🚀 Elevator Pitch
Verbatim bridges communication gaps by translating American Sign Language (ASL) into spoken language in real time, enhanced with interactive, audio-reactive visuals that make communication both accessible and expressive.  

---

## 💡 Inspiration
- One of our teammates is friends with someone who is deaf and has seen firsthand the challenges of communication, especially due to the lack of universality of ASL  
- This inspired us to create a tool that makes ASL more accessible while bridging language gaps—and turning the process into a fun and engaging visual experience  

---

## 🧠 What It Does
- Verbatim translates ASL in real time and visualizes it through audio-reactive particle motion  
- As users sign:  
  - 🤟 Hand gestures are detected and translated into text  
  - 🔊 Text is converted into speech  
  - ✨ The audio drives a live visual simulation  
- The result is an immersive, multi-sensory communication experience that makes language both accessible and engaging  

---

## 🛠️ How We Built It
- **Hand Tracking:** Google Mediapipe + OpenCV to detect and extract hand landmarks  
- **Machine Learning:**  
  - Processed landmark data into a dataset  
  - Trained a **Random Forest model** using scikit-learn  
- **Translation Pipeline:** ASL → Text → Speech using pyttsx3  
- **Visualization:**  
  - Sent audio data via OSC (python-osc)  
  - Built an audio-reactive simulation in TouchDesigner  

---

## ⚠️ Challenges/Changes
- Pivoting from TensorFlow/Keras to Random Forest due to small datasets and training speed  
- Integrating multiple systems: ML + TTS + OSC + TouchDesigner  
- A major system crash deleted ~6 hours of TouchDesigner work  
- Rebuilding quickly under hackathon time pressure  
- Thanks to strong documentation and planning, we were able to fully rebuild our system in about an hour  

---

## 🏆 Accomplishments
- Successfully built a **fully integrated real-time pipeline**  
- Connected Python + TouchDesigner using OSC  
- Quickly recovered from a major system crash  
- Created a system that is both functional *and* visually engaging  

---

## 🔮 What’s Next
- Expand beyond fingerspelling to support a full ASL vocabulary  
- Collaborate with the deaf community to ensure accuracy and usability  
- Integrate with platforms like Zoom for real-time virtual translation  
- Scale accessibility for broader real-world applications  

---

## ⚙️ Tech Stack
- **Python** — core language  
- **MediaPipe** — hand landmark detection  
- **OpenCV** — webcam capture + processing  
- **scikit-learn (Random Forest)** — gesture classification  
- **pyttsx3** — text-to-speech engine  
- **python-osc** — OSC communication bridge  
- **TouchDesigner** — real-time visual simulation  

---

## 📂 File Structure
```
/
├── main.py # Main ASL translation pipeline
├── model/ # Trained Random Forest model
├── data/ # Training dataset
├── osc/ # OSC communication scripts
├── touchdesigner/ # Visual simulation file (.toe)
└── utils/ # Helper functions
```

---

## ▶️ How to Run
- **Install dependencies:**  
  ```bash
  pip install mediapipe opencv-python scikit-learn pyttsx3 python-osc
  ```
- **Run Python translator:** `python main.py`
- **Open TouchDesigner file** (ensure OSC port matches, e.g., 9000)
- **Start signing!** 🤟

---

## 👥 Developers
- Raksha Kumaresan — Machine Learning & AI Software Engineer 
- Kali Bucklen - Graphics & Systems Integration Developer  

---

## 🏁 Built at
FemmeHacks @ UPenn
