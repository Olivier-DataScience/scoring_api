import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftTable

# Charger les datasets
train_data = pd.read_csv("application_train.csv")
test_data = pd.read_csv("application_test.csv")

# Sélectionner les mêmes colonnes dans les deux datasets
common_columns = [col for col in train_data.columns if col in test_data.columns]
train_data_filtered = train_data[common_columns]  # On garde TARGET mais on ne l'analyse pas
test_data_filtered = test_data[common_columns]  # Même colonnes que train_data sans TARGET

# 📌 Prendre un échantillon aléatoire pour éviter l'explosion de la mémoire
train_data_sample = train_data_filtered.sample(n=50000, random_state=42)  # 50 000 lignes
test_data_sample = test_data_filtered.sample(n=10000, random_state=42)  # 10 000 lignes

# 📌 Créer un rapport de Data Drift avec l'échantillon réduit
report = Report(metrics=[DataDriftTable()])
report.run(reference_data=train_data_sample, current_data=test_data_sample)

# Générer le rapport HTML
report.save_html("data_drift_report.html")

print("✅ Rapport Evidently généré : data_drift_report.html")