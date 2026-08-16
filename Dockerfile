FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir pipdeptree

RUN pipdeptree

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]