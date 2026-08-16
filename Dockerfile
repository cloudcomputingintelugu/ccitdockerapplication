FROM python:3.12-slim

WORKDIR /app

COPY requirements_docker.txt .

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements_docker.txt \
    && pip install --no-cache-dir "msgpack>=1.2.1"

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]