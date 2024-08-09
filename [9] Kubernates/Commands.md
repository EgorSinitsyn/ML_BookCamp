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

# Авторизация:
$(aws ecr get-login --no-include-email)

 # Постройте и загрузите образ для модели TensorFlow Serving
docker build -t tf-serving-clothing-model -f tf-serving.dockerfile .
docker tag tf-serving-clothing-model 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:tf-serving-clothing-model
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:tf-serving-clothing-model

# Постройте и загрузите образ Gateway
docker build -t serving-gateway -f gateway.dockerfile .
docker tag serving-gateway 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:serving-gateway
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:serving-gateway


4) Установка зависимостей Pipfile
pipenv install flask==3.0.3 gunicorn==22.0.0 keras-image-helper==0.0.1 grpcio==1.64.1 tensorflow==2.17.0 tensorflow-serving-api==2.17.0
pipenv install flask gunicorn keras-image-helper grpcio tensorflow tensorflow-serving-api
pipenv install flask==3.0.0 gunicorn==22.0.0 keras-image-helper==0.0.1 grpcio tensorflow==2.17.0 tensorflow-serving-api==2.17.0


5) Развертывание в AWS Elastic Kubernates Service
# Развертывание кластера
eksctl create cluster -f cluster.yaml
# Настройка kubectl для получения доступа
aws eks --region us-east-1 update-kubeconfig --name ml-bookcamp-eks
# Подключение к кластеру
kubectl get service
# Развертывание конфигурации модели
kubectl apply -f tf-serving-clothing-model-deployment.yaml
# Развертывание конфигурации сервиса для TF Serving
kubectl apply -f tf-serving-clothing-model-service.yaml
# Развертывание конфигурации Gateway
kubectl apply -f serving-gateway-deployment.yaml
# Развертывание конфигурации сервиса для Gateway
kubectl apply -f serving-gateway-service.yaml
# Вы ключение кластера
eksctl delete cluster --name ml-bookcamp-eks


# Получение списка всех активных развертываний
kubectl get deployments
# Получение скиска модулей
kubectl get pods
# Получение списка сервисов
kubectl get services
# Чтобы увидеть внешний url сервиса
kubectl describe service serving-gateway
## LoadBalancer Ingress:     ae0b820c610ad4386ac3f2f4d7602ae5-1939140193.us-east-1.elb.amazonaws.com

# URL сервиса
tf-serving-clothing-model.default.svc.cluster.local

