***КОМАНДЫ***

1) Запуск контейкера Docker:

docker run -it --rm \
    -p 8500:8500 \
    -v "/Users/oudzhi/PycharmProjects/ML_BookCamp/[9] Kubernates/clothing-model:/models/clothing-model" \
    -e MODEL_NAME=clothing-model \
    emacski/tensorflow-serving:latest

