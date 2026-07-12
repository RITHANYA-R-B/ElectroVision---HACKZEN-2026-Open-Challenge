# ElectroVision

ElectroVision is an AI-powered educational platform that detects electronic components using a YOLOv11 object detection model and provides interactive explanations through an AI Tutor. The system aims to make learning electronics more engaging for students, beginners, and hobbyists.

# Instalation & Setup Instructions
1. Clone the repository:
   git clone https://github.com/RITHANYA-R-B/ElectroVision---HACKZEN-2026-Open-Challenge.git
2. Navigate to the project directory:
   cd ElectroVision---HACKZEN-2026-Open-Challenge
3.Install the required dependencies:
   pip install -r requirements.txt
4.Ensure the trained YOLOv11 model (best.pt) is placed in the project directory.
5.Run the Streamlit application:
  streamlit run app.py

# Usage Instructions
1.Launch the Streamlit application using the command:
  streamlit run app.py
2.Open the local URL displayed in the terminal (usually http://localhost:8501).
3.Upload an image containing an electronic component.
4.Click Predict/Detect (if applicable).
5.The application identifies the electronic component using the trained YOLOv11 model.
6.The AI Tutor displays the detected component name along with its description, working principle, and applications.
7.Upload additional images to identify and learn about other electronic components.
