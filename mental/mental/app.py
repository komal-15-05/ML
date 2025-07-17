import streamlit as st
import joblib
import numpy as np

# Load trained model
import joblib
import os

# This will load model from the same folder where app.py is
model_path = os.path.join(os.path.dirname(__file__), "mental_health_treatment_model.pkl")
model = joblib.load(model_path)


# Title
st.title("🧠 Mental Health Treatment Predictor")
st.markdown("Predict if someone might need mental health treatment based on workplace and personal factors.")

# Input fields
age = st.slider("Your Age", 16, 80, 25)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
self_employed = st.selectbox("Are you self-employed?", ["Yes", "No"])
family_history = st.selectbox("Family history of mental illness?", ["Yes", "No"])
work_interfere = st.selectbox("Does your mental health interfere with work?", ["Never", "Rarely", "Sometimes", "Often", "Don't know"])
no_employees = st.selectbox("Company size", ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"])
remote_work = st.selectbox("Do you work remotely?", ["Yes", "No"])
tech_company = st.selectbox("Is it a tech company?", ["Yes", "No"])
benefits = st.selectbox("Does your employer provide mental health benefits?", ["Yes", "No", "Don't know"])
care_options = st.selectbox("Access to mental health care options?", ["Yes", "No", "Not sure"])
wellness_program = st.selectbox("Does your employer offer wellness programs?", ["Yes", "No", "Don't know"])
seek_help = st.selectbox("Is there help available for mental health?", ["Yes", "No", "Don't know"])
anonymity = st.selectbox("Anonymity provided by employer?", ["Yes", "No", "Don't know"])
leave = st.selectbox("How easy is it to take mental health leave?", ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult", "Don't know"])
mental_health_consequence = st.selectbox("Perceived consequence of discussing mental health at work?", ["Yes", "No", "Maybe"])
phys_health_consequence = st.selectbox("Perceived consequence of discussing physical health at work?", ["Yes", "No", "Maybe"])
coworkers = st.selectbox("Comfort discussing with coworkers?", ["Yes", "No", "Some of them"])
supervisor = st.selectbox("Comfort discussing with supervisor?", ["Yes", "No", "Some of them"])
mental_health_interview = st.selectbox("Would you discuss mental health in interview?", ["Yes", "No", "Maybe"])
phys_health_interview = st.selectbox("Would you discuss physical health in interview?", ["Yes", "No", "Maybe"])
mental_vs_physical = st.selectbox("Is mental health as important as physical?", ["Yes", "No", "Don't know"])
obs_consequence = st.selectbox("Observed consequences of coworkers with mental health issues?", ["Yes", "No"])

# Encode manually (as in model)
def encode(val, mapping):
    return mapping.get(val, 0)

gender_map = {"Male": 1, "Female": 0, "Other": 2}
yn_map = {"Yes": 1, "No": 0, "Don't know": 2, "Not sure": 2}
freq_map = {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Don't know": 4}
leave_map = {
    "Very easy": 0,
    "Somewhat easy": 1,
    "Somewhat difficult": 2,
    "Very difficult": 3,
    "Don't know": 4
}
maybe_map = {"Yes": 1, "No": 0, "Maybe": 2}
some_map = {"Yes": 1, "No": 0, "Some of them": 2}

# Prepare input data
input_data = np.array([[
    age,
    encode(gender, gender_map),
    encode(self_employed, yn_map),
    encode(family_history, yn_map),
    encode(work_interfere, freq_map),
    encode(no_employees, {
        "1-5": 0, "6-25": 1, "26-100": 2, "100-500": 3,
        "500-1000": 4, "More than 1000": 5
    }),
    encode(remote_work, yn_map),
    encode(tech_company, yn_map),
    encode(benefits, yn_map),
    encode(care_options, yn_map),
    encode(wellness_program, yn_map),
    encode(seek_help, yn_map),
    encode(anonymity, yn_map),
    encode(leave, leave_map),
    encode(mental_health_consequence, maybe_map),
    encode(phys_health_consequence, maybe_map),
    encode(coworkers, some_map),
    encode(supervisor, some_map),
    encode(mental_health_interview, maybe_map),
    encode(phys_health_interview, maybe_map),
    encode(mental_vs_physical, yn_map),
    encode(obs_consequence, yn_map)
]])

# Predict button
if st.button("🧠 Predict"):
    input_data = input_data[:, :21]
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ You **might need** mental health treatment.")
        st.markdown("💡 **Suggestions:** Talk to a mental health professional, check for employer benefits, reach out to support groups.")
    else:
        st.success("✅ You likely **do not need** treatment right now.")
        st.markdown("🧘‍♀️ Keep taking care of your well-being and stay mentally healthy!")
