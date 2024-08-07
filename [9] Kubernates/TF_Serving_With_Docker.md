docker run -it --rm \
    -p 8500:8500 \
    -v "$(pwd)/clothing-model:/models/clothing-model/1" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest

docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model_savedmodel:/models/clothing-model" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest


docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model:/models/clothing-model" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest



docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model:/models/clothing-model/" \
    -e MODEL_NAME=clothing-model \
    tensorflow/serving:latest

docker run -it --rm \
    -p 8502:8500 \       # Пробрасываем порт 8502 на порт 8500 внутри контейнера для gRPC API
    -p 8503:8501 \       # Пробрасываем порт 8503 на порт 8501 внутри контейнера для REST API
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model:/models/clothing-model/1" \  # Монтируем локальный каталог с моделью в контейнер
    -e MODEL_NAME=clothing-model \  # Устанавливаем переменную окружения с именем модели
    emacski/tensorflow-serving:latest  # Используем последний образ TensorFlow Serving


docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model_savedmodel:/models/clothing-model" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest
