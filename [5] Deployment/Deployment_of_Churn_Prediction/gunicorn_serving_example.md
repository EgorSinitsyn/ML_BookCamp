 Смена рабочей папки:
```bash
cd /ML_BookCamp/[5] Deployment/Deployment_of_Churn_Prediction/
```

# Запуск виртуального окружения pipenv
```bash
pipenv shell
```

# Запуск веб-сервиса через python
```bash
python churn_serving.py
```

# Альтернативный запуск веб-сервиса через gunicorn
# В отличии от встроенного веб-сервера Flask, Gunicorn готов к промышленной эксплуатации, поэтому у него не возникает никаких проблем с нагрузкой при реальном исп-ии
```bash
pipenv run gunicorn --bind 0.0.0.0:9696 churn_serving:app
```