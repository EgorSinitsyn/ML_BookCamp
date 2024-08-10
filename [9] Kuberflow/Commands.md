***КОМАНДЫ***

1) Установка KFserving с инструкциями по установке:
```bash
git clone git@github.com:alexeygrigorev/kubeflow-deep-learning.git
```

2) Создаем корзину в S3, в которую будем загружать модели:
```bash
aws s3api create-bucket \
    --bucket mlbookcamp-models-egor \
    --region us-east-1 
```

3) Загружаем модель в S3, предварительно перейдя в рабочий каталог:
```bash
aws s3 cp --recursive clothing-model s3://mlbookcamp-models-egor/clothing-model/0001
```

4) Создаем tf-clothes.yaml с конфигурацией модели:

5) Применяем конфигурацию модели:
```bash
kubectl apply -f tf-clothes.yaml
```