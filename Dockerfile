FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "msgpack>=1.2.1"

# Verify the actual installed versions
RUN python - <<'PY'
from importlib.metadata import version

for package in ["msgpack", "setuptools", "wheel"]:
    print(f"{package}=={version(package)}")
PY

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]