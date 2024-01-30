# app.py: Flask API sunucu dosyası

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Model ve Label Encoder'ı yükle
trained_models = joblib.load('trained_models.joblib')
label_encoder = joblib.load('label_encoder.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # JSON'dan DataFrame oluştur
    df = pd.DataFrame(data, index=[0])

    # Tahmin yap
    predictions = {}
    for model_name, model in trained_models.items():
        pred_label_index = model.predict(df)[0]
        pred_label = label_encoder.inverse_transform([pred_label_index])[0]
        predictions[model_name] = pred_label

    return jsonify(predictions)


if __name__ == '__main__':
    app.run(debug=True)
