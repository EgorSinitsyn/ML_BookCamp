import pickle
import numpy as np

from flask import Flask, request, jsonify


def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


with open('churn-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')


@app.route('/predict', methods=['POST']) # Назначает маршрут /predict функции predict
def predict():
    customer = request.get_json() # Получает содержимое запроса в Json

    # Оценивает клиента
    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5

    # Подготавливает ответ
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    # Преобразует в json
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)