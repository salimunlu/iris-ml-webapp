# streamlit_app.py: Streamlit frontend dosyası.

import pandas as pd
import streamlit as st
import requests

# API URL'si
API_URL = "http://127.0.0.1:5000/predict"

# Sayfa başlığı
st.title('İris Tür Tahmini')

# Kullanıcıdan girişlerin alınacağı form
with st.form("prediction_form"):
    st.write("Lütfen aşağıdaki değerleri girin:")

    # Kullanıcı girişleri
    sepal_length = st.number_input('Sepal Length', min_value=0.0, value=5.0, format="%.2f")
    sepal_width = st.number_input('Sepal Width', min_value=0.0, value=3.0, format="%.2f")
    petal_length = st.number_input('Petal Length', min_value=0.0, value=3.5, format="%.2f")
    petal_width = st.number_input('Petal Width', min_value=0.0, value=1.0, format="%.2f")

    # Form submit butonu
    submitted = st.form_submit_button("Tahmin Yap")

    if submitted:
        # Kullanıcı girişlerini bir sözlükte topla
        data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }

        # API'ye POST isteği yap
        response = requests.post(API_URL, json=data)

        # Yanıtı al ve göster
        if response.status_code == 200:
            predictions = response.json()

            # Tahminleri bir pandas DataFrame'e dönüştür
            predictions_df = pd.DataFrame(predictions.items(), columns=['Model', 'Tahmin'])

            # DataFrame'i tablo olarak göster
            st.table(predictions_df)
        else:
            st.error("Bir hata oluştu. API'den yanıt alınamadı.")

# Sayfa alt bilgisi
st.markdown("""
    <hr>
    İris Çiçeği Tür Tahmini Uygulaması<br>
    Data Science ve Makine Öğrenimi Projesi
    """, unsafe_allow_html=True)
