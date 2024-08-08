FROM python:3.11

ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app

RUN apt-get update && apt-get install -y libhdf5-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY "gateway_service.py" "gateway_service.py"

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "gateway_service.py:app"]