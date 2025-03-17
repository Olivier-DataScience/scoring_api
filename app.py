from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# 🔹 Charger le modèle et le seuil optimal
model, best_threshold = joblib.load("best_lightgbm_model.pkl")

# 🔹 Définition de l'API
app = FastAPI()

# 🔹 Définition du format d'entrée
class ClientData(BaseModel):
    EXT_SOURCE_3: float
    EXT_SOURCE_2: float
    PAYMENT_RATE: float
    EXT_SOURCE_1: float
    CODE_GENDER_F: float
    DAYS_EMPLOYED: float
    AMT_GOODS_PRICE: float
    NAME_EDUCATION_TYPE_Higher_education: float
    OWN_CAR_AGE: float
    AMT_ANNUITY: float
    NAME_FAMILY_STATUS_Married: float
    DAYS_BIRTH: float
    NAME_CONTRACT_TYPE_Cash_loans: float
    AMT_CREDIT: float
    DAYS_ID_PUBLISH: float

@app.get("/")
def home():
    return {"message": "API en ligne avec LightGBM !"}

@app.post("/predict")
def predict(client: ClientData):
    # Convertir les données en DataFrame
    client_df = pd.DataFrame([client.dict()])

    # Faire la prédiction
    probas = model.predict_proba(client_df)[:, 1]  # Probabilité de remboursement

    # Appliquer le seuil optimal
    prediction = "Oui, le client remboursera" if probas[0] >= best_threshold else "Non, le client ne remboursera pas"

    return {"prediction": prediction, "probabilité": float(probas[0])}

