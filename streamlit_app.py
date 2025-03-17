import streamlit as st
import requests
import json

# 🔹 Titre de l'application
st.title("Prédiction de remboursement de crédit 💰")

# 🔹 Création des champs de saisie pour les 15 features
EXT_SOURCE_3 = st.number_input("EXT_SOURCE_3", value=0.5)
EXT_SOURCE_2 = st.number_input("EXT_SOURCE_2", value=0.3)
PAYMENT_RATE = st.number_input("PAYMENT_RATE", value=0.02)
EXT_SOURCE_1 = st.number_input("EXT_SOURCE_1", value=0.6)
CODE_GENDER_F = st.selectbox("CODE_GENDER_F", [0, 1])
DAYS_EMPLOYED = st.number_input("DAYS_EMPLOYED", value=-5000)
AMT_GOODS_PRICE = st.number_input("AMT_GOODS_PRICE", value=150000)
NAME_EDUCATION_TYPE_Higher_education = st.selectbox("NAME_EDUCATION_TYPE_Higher_education", [0, 1])
OWN_CAR_AGE = st.number_input("OWN_CAR_AGE", value=5)
AMT_ANNUITY = st.number_input("AMT_ANNUITY", value=25000)
NAME_FAMILY_STATUS_Married = st.selectbox("NAME_FAMILY_STATUS_Married", [0, 1])
DAYS_BIRTH = st.number_input("DAYS_BIRTH", value=-12000)
NAME_CONTRACT_TYPE_Cash_loans = st.selectbox("NAME_CONTRACT_TYPE_Cash_loans", [0, 1])
AMT_CREDIT = st.number_input("AMT_CREDIT", value=200000)
DAYS_ID_PUBLISH = st.number_input("DAYS_ID_PUBLISH", value=-4000)

# 🔹 Bouton pour envoyer la requête
if st.button("Prédire si le client remboursera"):

    # 🔹 Création du JSON pour l'API
    input_data = {
        "EXT_SOURCE_3": EXT_SOURCE_3,
        "EXT_SOURCE_2": EXT_SOURCE_2,
        "PAYMENT_RATE": PAYMENT_RATE,
        "EXT_SOURCE_1": EXT_SOURCE_1,
        "CODE_GENDER_F": CODE_GENDER_F,
        "DAYS_EMPLOYED": DAYS_EMPLOYED,
        "AMT_GOODS_PRICE": AMT_GOODS_PRICE,
        "NAME_EDUCATION_TYPE_Higher_education": NAME_EDUCATION_TYPE_Higher_education,
        "OWN_CAR_AGE": OWN_CAR_AGE,
        "AMT_ANNUITY": AMT_ANNUITY,
        "NAME_FAMILY_STATUS_Married": NAME_FAMILY_STATUS_Married,
        "DAYS_BIRTH": DAYS_BIRTH,
        "NAME_CONTRACT_TYPE_Cash_loans": NAME_CONTRACT_TYPE_Cash_loans,
        "AMT_CREDIT": AMT_CREDIT,
        "DAYS_ID_PUBLISH": DAYS_ID_PUBLISH
    }

    # 🔹 Envoi de la requête POST à l'API FastAPI
    url = "https://mon-api-fastapi-32b9272786a2.herokuapp.com/predict"
    response = requests.post(url, json=input_data)
    
    # 🔹 Affichage du résultat
    if response.status_code == 200:
        result = response.json()
        st.success(f"Résultat : {result['prediction']}")
        st.info(f"Probabilité : {round(result['probabilité'], 4)}")
    else:
        st.error("Erreur lors de la requête à l'API")
 
