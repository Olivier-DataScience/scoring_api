from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Charger le modèle et le seuil optimal
model, best_threshold = joblib.load("best_lightgbm_model.pkl")

# Définition de l'API
app = FastAPI()

# Définition du format d'entrée
class ClientData(BaseModel):
    CNT_CHILDREN: float
    CNT_FAM_MEMBERS: float
    CODE_GENDER_F: float
    CODE_GENDER_M: float
    FLAG_OWN_CAR_Y: float
    FLAG_OWN_CAR_N: float
    FLAG_OWN_REALTY_Y: float
    FLAG_OWN_REALTY_N: float
    NAME_FAMILY_STATUS_Married: float
    NAME_FAMILY_STATUS_Single_not_married: float
    NAME_FAMILY_STATUS_Widow: float
    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    AMT_GOODS_PRICE: float
    INCOME_CREDIT_PERC: float
    ANNUITY_INCOME_PERC: float
    PAYMENT_RATE: float
    DAYS_BIRTH: float
    DAYS_EMPLOYED: float
    DAYS_EMPLOYED_PERC: float
    DAYS_REGISTRATION: float
    DAYS_ID_PUBLISH: float
    NAME_EDUCATION_TYPE_Higher_education: float
    NAME_EDUCATION_TYPE_Secondary_secondary_special: float
    NAME_EDUCATION_TYPE_Lower_secondary: float
    OCCUPATION_TYPE_Accountants: float
    OCCUPATION_TYPE_Core_staff: float
    OCCUPATION_TYPE_Laborers: float
    OCCUPATION_TYPE_Managers: float
    OCCUPATION_TYPE_Sales_staff: float
    EXT_SOURCE_2: float
    EXT_SOURCE_3: float
    AMT_REQ_CREDIT_BUREAU_YEAR: float
    AMT_REQ_CREDIT_BUREAU_MON: float
    AMT_REQ_CREDIT_BUREAU_QRT: float
    OBS_30_CNT_SOCIAL_CIRCLE: float
    DEF_30_CNT_SOCIAL_CIRCLE: float
    OBS_60_CNT_SOCIAL_CIRCLE: float
    DEF_60_CNT_SOCIAL_CIRCLE: float
    REGION_POPULATION_RELATIVE: float
    REGION_RATING_CLIENT: float
    REGION_RATING_CLIENT_W_CITY: float
    DAYS_LAST_PHONE_CHANGE: float
    FLAG_PHONE: float
    FLAG_EMAIL: float
    FLAG_EMP_PHONE: float
    FLAG_WORK_PHONE: float

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


