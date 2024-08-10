***КОМАНДЫ***

# KFserving EKS #
https://mlbookcamp.com/article/kfserving-eks-install ...

1) Установка KFserving с инструкциями по установке:
```bash
git clone git@github.com:alexeygrigorev/kubeflow-deep-learning.git
```


2) Создаем кластер EKS cluster.yaml и применяем:
```bash
eksctl create cluster -f cluster.yaml
```


3) Настройка kubectl для получения доступа
```bash
aws eks --region es-east-1 update-kubeconfig --name ml-bookcamp-eks
```


4) Проверка подключения к кластеру
```bash
kubectl get service
```


5) .... https://mlbookcamp.com/article/kfserving-eks-install


6) Создаем корзину в S3, в которую будем загружать модели:
```bash
aws s3api create-bucket \
    --bucket mlbookcamp-models-egor \
    --region us-east-1 
```


7) Загружаем модель в S3, предварительно перейдя в рабочий каталог:
```bash
aws s3 cp --recursive clothing-model s3://mlbookcamp-models-egor/clothing-model/0001
```


7) Создаем tf-clothing.yaml с конфигурацией модели:


8) Применяем конфигурацию модели:
```bash
kubectl apply -f tf-clothing.yaml
```


9) Получаем список объектов кластера и проверяем готовность сервиса:
```bash
kubectl get inferenceservice
```


10) Тестируем сервис:
```bash
python test_service.py
```


11) Удаляем старый сервис вывода для теста преобразователя:
https://mlbookcamp.com/article/kfserving-transformers
```bash
kubectl delete -f tf-clothing.yaml
```


12) Создаем файл tf-clothing-keras-transformer.yaml и применяем конфигурацию:
```bash
kubectl apply -f tf-clothing-keras-transformer.yaml
```
Проверяем готовность сервиса:
```bash
kubectl get inferenceservice
```

13) Тестирование преобразователя:
```bash
python test_transformer.py
```

