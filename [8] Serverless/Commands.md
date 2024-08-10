1) Создание образа Docker


2) Cоздание образа докер
```bash
docker build -t tf-lite-lambda .
```


3) Запуск контейнера
```bash
docker run -p 9000:8080 tf-lite-lambda
```

4) Проверка работы в testing_service.ipynb


## Отправка изображения в AWS ECR ##

5) Создание репозитория в AWS ECR
```bash
aws ecr create-repository --repository-name lambda-images
```
# Выдает: 992382766194.dkr.ecr.us-east-1.amazonaws.com/lambda-images

6) Аунтификация в AWS ECR
```bash
$(aws ecr get-login --no-include-email)
```

7) Тегирование образа
```bash
docker tag tf-lite-lambda 992382766194.dkr.ecr.us-east-1.amazonaws.com/lambda-images:tf-lite-lambda
```

8) Пуш образа в AWS ECR
```bash
docker push 992382766194.dkr.ecr.us-east-1.amazonaws.com/lambda-images:tf-lite-lambda
```

9) Создание функции AWS Lambda и API Gateway Через интерфейс AWS Console
