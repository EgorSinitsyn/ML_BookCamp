***КОМАНДЫ***

1) Запуск контейкера Docker:
```bash
docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model:/models/clothing-model" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest
```

2) Создание реестра с именем model-serving:
```bash
aws ecr create-repository --repository-name model-serving
```

3) Создание образа докер для Tensorflow Serving и отправка в ECR

* Авторизация:
```bash
$(aws ecr get-login --no-include-email)
```

* Постройте и загрузите образ для модели TensorFlow Serving
```bash
docker build -t tf-serving-clothing-model -f tf-serving.dockerfile .
```
```bash
docker tag tf-serving-clothing-model 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:tf-serving-clothing-model
```
```bash
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:tf-serving-clothing-model
```

* Постройте и загрузите образ Gateway
```bash
docker build -t serving-gateway -f gateway.dockerfile .
```
```bash
docker tag serving-gateway 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:serving-gateway
```
```bash
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/model-serving:serving-gateway
```


4) Установка зависимостей Pipfile
```bash
pipenv install flask==3.0.3 gunicorn==22.0.0 keras-image-helper==0.0.1 grpcio==1.64.1 tensorflow==2.17.0 tensorflow-serving-api==2.17.0
```
или
```bash
pipenv install flask gunicorn keras-image-helper grpcio tensorflow tensorflow-serving-api
```


5) Развертывание в AWS Elastic Kubernates Service
* Развертывание кластера
```bash
eksctl create cluster -f cluster.yaml
```
* Настройка kubectl для получения доступа
```bash
aws eks --region us-east-1 update-kubeconfig --name ml-bookcamp-eks
```
* Подключение к кластеру
```bash
kubectl get service
```
* Развертывание конфигурации модели
```bash
kubectl apply -f tf-serving-clothing-model-deployment.yaml
```
* Развертывание конфигурации сервиса для TF Serving
```bash
kubectl apply -f tf-serving-clothing-model-service.yaml
```
* Развертывание конфигурации Gateway
```bash
kubectl apply -f serving-gateway-deployment.yaml
```
* Развертывание конфигурации сервиса для Gateway
```bash
kubectl apply -f serving-gateway-service.yaml
```
* Выключение кластера
```bash
eksctl delete cluster --name ml-bookcamp-eks
```


* Получение списка всех активных развертываний
```bash
kubectl get deployments
```
* Получение скиска модулей
```bash
kubectl get pods
```
* Получение списка сервисов
```bash
kubectl get services
```
* Чтобы увидеть внешний url сервиса
```bash
kubectl describe service serving-gateway
```
 LoadBalancer Ingress:     ae0b820c610ad4386ac3f2f4d7602ae5-1939140193.us-east-1.elb.amazonaws.com

* URL сервиса
tf-serving-clothing-model.default.svc.cluster.local

