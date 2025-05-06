from pathlib import Path
import streamlit as st
import joblib
import pandas as pd

# Path setup
here = Path(__file__).resolve().parent      
project_root = here.parent                    
model_path = project_root / "model" / "model.pkl"

# Load the trained model
model = joblib.load(model_path)

st.title("Prédiction de Défaut de Crédit")
st.markdown("Entrez les informations du client pour prédire le risque de défaut.")

# -- user inputs as before --
age = st.number_input("Âge", min_value=18, max_value=100, value=30)
income = st.number_input("Revenu annuel (€)", min_value=0, value=30000)
home_ownership = st.selectbox("Statut logement", ["OWN", "RENT", "MORTGAGE", "OTHER"])
emp_length = st.number_input("Années d'emploi", min_value=0, value=5)
loan_intent = st.selectbox("Objectif du prêt", 
                           ["EDUCATION","MEDICAL","VENTURE","PERSONAL",
                            "HOMEIMPROVEMENT","DEBTCONSOLIDATION"])
loan_grade = st.selectbox("Note de crédit", ["A","B","C","D","E","F","G"])
loan_amnt = st.number_input("Montant du prêt (€)", min_value=100, value=5000)
loan_int_rate = st.number_input("Taux d'intérêt (%)", min_value=0.0, value=10.0)
loan_percent_income = loan_amnt / (income + 1e-6)
cb_default = st.selectbox("Défaut dans le fichier crédit ?", ["Y","N"])
cred_hist_length = st.number_input("Ancienneté historique crédit (années)", min_value=0, value=5)

if st.button("Prédire"):
    input_df = pd.DataFrame([{
        "person_age": age,
        "person_income": income,
        "person_home_ownership": home_ownership,
        "person_emp_length": emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_default,
        "cb_person_cred_hist_length": cred_hist_length
    }])

    # now this will work
    proba = model.predict_proba(input_df)[0][1]
    st.subheader("Résultat")
    st.write(f"Probabilité de défaut : **{proba * 100:.2f}%**")

