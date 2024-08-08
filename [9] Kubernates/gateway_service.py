'''

Сервис Gateway - приложение Flask, которое получает URL изображения и подготавливает его.
Затем использует gRPC и protobuf для взаимодействия с  TF Serving.

Сервис выполняет следующие действия:
- Получает URL изобр из запроса
- Скачивает изображение, предварительно обрабатывает его и преобразовывает в массив NumPy
- Преобразовывает массив NumPu в protobuf и использует gRPC для связи с TF Serving
- Выполняет окончательную обработку результатов. Преобразовывает необработанные список с числами в понятную человеку форму

'''

import os

import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

from keras_image_helper import create_preprocessor

from flask import Flask, request, jsonify

# Заглушка для подключения gRPC
server = os.getenv('TF_SERVING_HOST', 'localhost:8500')
channel = grpc.insecure_channel(server)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

# Создаем препроцессор
preprocessor = create_preprocessor('xception', target_size=(299, 299))

# Определяем имена классов
labels = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]


def np_to_protobuf(data):
    '''
    Ф-ция преобразования массива Numpy в Protobuf
    '''
    return tf.make_tensor_proto(data, shape=data.shape)


def make_request(X):
    '''
    Функция создания запроса gRPC из массива NumPy
    '''
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = 'clothing-model'
    pb_request.model_spec.signature_name = 'serving_default'
    pb_request.inputs['input_layer_34'].CopyFrom(np_to_protobuf(X))
    return pb_request


def process_response(pb_result):
    '''
    Функция прогноза + присвоения меток
    '''
    pred = pb_result.outputs['output_0'].float_val
    result = {c: p for c, p in zip(labels, pred)}
    return result


def apply_model(url):
    '''
    Фунция обработки изображения, отправки запроса и получения результата
    '''
    X = preprocessor.from_url(url) # предварительно обрабатывает изобр из URl
    pb_request = make_request(X) # Преобразует массив Numpy в запрос gRPC
    pb_result = stub.Predict(pb_request, timeout=20.0) # Выполняет запрос
    return process_response(pb_result) # Обрабатывает ответ и закрепляет метки за прогнозами



app = Flask('clothing-model')


@app.route('/predict', methods=['POST'])
def predict():
    url = request.get_json()
    result = apply_model(url['url'])
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)