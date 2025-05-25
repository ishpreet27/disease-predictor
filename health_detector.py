from tkinter import *
from tkinter import ttk
import numpy as np

# List of symptoms
l1 = ['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of_urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
'Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)','Jaundice','Malaria',
'Chicken pox','Dengue','Typhoid','hepatitis A','Hepatitis B','Hepatitis C','Hepatitis D',
'Hepatitis E','Alcoholic hepatitis','Tuberculosis','Common Cold','Pneumonia',
'Dimorphic hemmorhoids(piles)','Heart attack','Varicose veins','Hypothyroidism',
'Hyperthyroidism','Hypoglycemia','Osteoarthristis','Arthritis',
'(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis','Impetigo']

# Empty list for symptom presence
l2 = [0]*len(l1)

# Improved logic to predict diseases
def mock_predict(symptoms_selected):
    symptom_indices = [i for i, val in enumerate(symptoms_selected) if val == 1]
    if not symptom_indices:
        return "No symptoms selected", "Please select symptoms for accurate diagnosis."

    symptom_names = [l1[i] for i in symptom_indices]

    # Rule-based logic
    if "mild_fever" in symptom_names and "phlegm" in symptom_names and "chest_pain" in symptom_names:
        return "Bronchial Asthma", "Avoid allergens, use inhalers regularly, and monitor breathing."
    elif "diarrhoea" in symptom_names and "abdominal_pain" in symptom_names:
        return "Gastroenteritis", "Stay hydrated, avoid spicy food, and consult a doctor if severe."
    elif "yellowing_of_eyes" in symptom_names and "yellow_urine" in symptom_names:
        return "Jaundice", "Get liver function tests, avoid alcohol and oily food."
    elif "joint_pain" in symptom_names and "muscle_weakness" in symptom_names:
        return "Arthritis", "Exercise regularly, maintain a healthy weight, and take anti-inflammatory meds."
    elif "skin_peeling" in symptom_names or "pus_filled_pimples" in symptom_names:
        return "Fungal infection", "Use antifungal creams and keep the affected area dry."
    else:
        return "Common Cold", "Rest, drink fluids, and use steam inhalation to relieve congestion."

# Tkinter GUI
root = Tk()
root.title("Disease Predictor")
root.geometry("750x600")
root.configure(bg='lightblue')

# Header
Label(root, text="Disease Predictor", fg="white", bg="blue", font=("Elephant", 30)).grid(row=0, column=0, columnspan=2, pady=20)
Label(root, text="A Project by Ishpreet", fg="white", bg="blue", font=("Aharoni", 20)).grid(row=1, column=0, columnspan=2, pady=5)

# Patient name
Label(root, text="Name of Patient:", bg='lightblue', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky=W)
Name = StringVar()
Entry(root, textvariable=Name, width=40).grid(row=2, column=1, padx=10, pady=10)

# Symptom dropdowns
SymptomVars = [StringVar() for _ in range(5)]

def create_autocomplete_combo(row, symptom_var, label):
    Label(root, text=label, bg='lightblue', font=('Arial', 12)).grid(row=row, column=0, sticky=W, padx=10)
    combo = ttk.Combobox(root, textvariable=symptom_var, values=sorted(l1), width=45)
    combo.grid(row=row, column=1, padx=10, pady=5)
    combo.set('')
    combo['state'] = 'normal'
    return combo

S1 = create_autocomplete_combo(3, SymptomVars[0], "Symptom 1:")
S2 = create_autocomplete_combo(4, SymptomVars[1], "Symptom 2:")
S3 = create_autocomplete_combo(5, SymptomVars[2], "Symptom 3:")
S4 = create_autocomplete_combo(6, SymptomVars[3], "Symptom 4:")
S5 = create_autocomplete_combo(7, SymptomVars[4], "Symptom 5:")

# Output box
result_text = Text(root, height=5, width=70, bg='orange', fg='black', font=('Arial', 12))
result_text.grid(row=9, column=0, columnspan=2, padx=10, pady=20)

# Prediction function
def predict_disease():
    for i in range(len(l2)):
        l2[i] = 0

    for sv in SymptomVars:
        symptom = sv.get().strip()
        if symptom in l1:
            l2[l1.index(symptom)] = 1

    disease_name, suggestion = mock_predict(l2)
    result_text.delete('1.0', END)
    result_text.insert(END, f"Predicted Disease: {disease_name}\n\nAI Suggestion: {suggestion}")

# Button
Button(root, text="Predict Disease", command=predict_disease, bg='green', fg='white', font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
