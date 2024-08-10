1) Запуск pipenv
```bash
pipenv shell
```

2) Запуск приложения с помощью Gunicorn
```bash
pipenv run gunicorn --bind 0.0.0.0:9696 churn_serving:app
```


# Docker #
1) Создание образа
```bash
docker build -t churn_prediction .
```

2) Запуск контейнера
```bash
docker run -d -p 9696:9696 churn_prediction:latest
```


# AWS Elastic Beanstalk #
1) Добавляем Pipenv как рабочую зависимость
```bash
pipenv install awsebcli --dev
```

2) Входим в виртуальное окружение
```bash
pipenv shell
```

3) Проверяем доступность EB CLI
```bash
eb --version
```

4) Запустим команду инициализации
```bash
eb init -p docker churn-serving
```

5) Тестируем приложение локально
```bash
eb local run --port 9696
```

6) Разворачиваем приложение на AWS
```bash
eb create churn-serving-env
```

7) Тестируем развернутое приложение
```bash
python churn_serving.py
```

8) Отключаем приложение
```bash
eb terminate churn-serving-env
```
