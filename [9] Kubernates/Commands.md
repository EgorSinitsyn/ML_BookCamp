***КОМАНДЫ***

1) Запуск контейкера Docker:

docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model:/models/clothing-model" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest

2) Создание реестра с именем model-serving:
aws ecr create-repository --repository-name model-serving

3) Создание образа докер для Tensorflow Serving  и отправка в ECR

 # Постройте и загрузите образ для модели TensorFlow Serving
docker build -t tf-serving-clothing-model -f tf-serving.dockerfile .
docker tag tf-serving-clothing-model 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving

# Постройте и загрузите образ для шлюза
docker build -t serving-gateway -f gateway.dockerfile .
docker tag serving-gateway 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving


4) Установка зависимостей Pipfile
pipenv install flask gunicorn keras_image_helper==0.0.1 grpcio==1.64.1 tensorflow==2.17.0 tensorflow-serving-api==2.17.0
