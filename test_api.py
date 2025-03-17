import streamlit as st
import requests

# URL de ton API Heroku
API_URL = "https://scoring-api-unique-name.herokuapp.com"

st.title("Test de l'API de scoring crédit")

# Bouton pour tester l'API
if st.button("Tester l'API"):
    response = requests.get(f"{API_URL}/")
    if response.status_code == 200:
        st.success(response.json())
    else:
        st.error("Erreur lors de la connexion à l'API.")
 
