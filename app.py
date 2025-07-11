import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
model = joblib.load('lung_cancer.pkl')
scaler = joblib.load('scaler.pkl')
st.title("Prediksi Kanker PAru2")
# Form input
with st.form("form_kanker"):
  GENDER = st.number_input('Gender', min_value=0, max_value=1)
  AGE = st.number_input('Age', min_value=0, max_value=200)
  SMOKING = st.number_input('Smoking', min_value=0, max_value=1)
  YELLOW_FINGERS = st.number_input('Yellow Fingers', min_value=0, max_value=1)
  ANXIETY = st.number_input('ANXIETY', min_value=0, max_value=1)
  PEER_PRESSURE = st.number_input('PEER_PRESSURE', min_value=0, max_value=1)
  CHRONICDISEASE = st.number_input('CHRONIC DISEASE', min_value=0, max_value=1)
  FATIGUE = st.number_input('FATIGUE', min_value=0, max_value=1)
  ALLERGY = st.number_input('ALLERGY', min_value=0, max_value=1)
  WHEEZING = st.number_input('WHEEZING', min_value=0, max_value=1)
  ALCOHOLCONSUMING = st.number_input('ALCOHOL CONSUMING', min_value=0, max_value=1)
  COUGHING = st.number_input('COUGHING', min_value=0, max_value=1)
  SHORTNESSOFBREATH = st.number_input('SHORTNESS OF BREATH', min_value=0, max_value=1)
  SWALLOWINGDIFFICULTY = st.number_input('SWALLOWING DIFFICULTY', min_value=0, max_value=1)
  CHESTPAIN = st.number_input('CHEST PAIN', min_value=0, max_value=1)
  
  submit = st.form_submit_button("Proses")
# Ketika tombol ditekan
if submit:
  # Format input ke bentuk array
  # features = np.array([[GENDER, AGE,
  # SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONICDISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOLCONSUMING, COUGHING, SHORTNESSOFBREATH, SWALLOWINGDIFFICULTY, CHESTPAIN]])
  data_dict = {
    'GENDER': [GENDER], 'AGE': [AGE],
    'SMOKING': [SMOKING], 'YELLOW_FINGERS': [YELLOW_FINGERS], 'ANXIETY': [ANXIETY],
    'PEER_PRESSURE': [PEER_PRESSURE], 'CHRONIC DISEASE': [CHRONICDISEASE],
    'FATIGUE': [FATIGUE], 'ALLERGY': [ALLERGY], 'WHEEZING': [WHEEZING],
    'ALCOHOL CONSUMING': [ALCOHOLCONSUMING], 'COUGHING': [COUGHING],
    'SHORTNESS OF BREATH': [SHORTNESSOFBREATH], 'SWALLOWING DIFFICULTY': [SWALLOWINGDIFFICULTY],
    'CHEST PAIN': [CHESTPAIN]
  }
  features_df = pd.DataFrame(data_dict)
  # Scaler
  features_df['AGE'] = scaler.transform(features_df[['AGE']])
  # Prediksi
  prediction = model.predict(features_df)[0]
  # Tampilkan hasil
  if prediction == 1:
    st.error("Hasil: Positif Kanker")
  else:
    st.success("Hasil: Tidak Kanker")
