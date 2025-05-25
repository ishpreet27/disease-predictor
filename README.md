🩺 Disease Predictor with Symptom Autocomplete
A simple AI-powered desktop application built using Python and Tkinter that predicts possible diseases based on selected symptoms, with intelligent suggestions and user-friendly autocomplete inputs.

📸 Preview
(Add your screenshot here)

🧠 Features
✅ Autocomplete symptom search with dropdown menus

✅ AI-like suggestions for common conditions

✅ Clean and intuitive GUI using Tkinter

✅ Dynamic prediction based on selected symptoms

✅ Personalized input: Patient Name

🛠️ Technologies Used
Python 3

Tkinter (GUI)

ttk.Combobox for autocomplete dropdowns

Rule-based AI logic for prediction (expandable to ML models)

📂 Project Structure
python
Copy
Edit
├── python_disease_predictor.py
├── README.md
└── (Optional) disease_model.pkl   # If using ML later
🚀 How to Run
Install Python
Make sure Python 3.7+ is installed on your system:
https://www.python.org/downloads/

Clone or Download this repository.

Run the application:

bash
Copy
Edit
python python_disease_predictor.py
Usage:

Enter the patient name

Select up to 5 symptoms using dropdowns

Click "Predict Disease"

View the predicted disease and AI suggestion

🔍 Example Symptoms
Try selecting:

mild_fever

phlegm

chest_pain
You'll get: Bronchial Asthma with an appropriate suggestion.

📌 Notes
This version uses mock rule-based AI logic.

You can upgrade it by integrating a real machine learning model (.pkl) trained on health data.

All symptom entries are mapped from a pre-defined list for accuracy and consistency.

🤖 Future Improvements
Integrate ML model for dynamic predictions

Add voice assistant using pyttsx3

Save diagnosis history

Add more symptoms/diseases

Export results as PDF or text

👨‍💻 Author
Ishpreet – Built as a personal project to help users get early insight into possible diseases using symptoms.

📄 License
This project is open-source and free to use for educational and non-commercial purposes.

