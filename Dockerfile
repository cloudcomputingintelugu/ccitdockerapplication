FROM python:3.11-slim-bookworm

WORKDIR /app

COPY requirements.txt .

# Install only application dependencies
RUN python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y setuptools wheel \
    && rm -rf /root/.cache/pip

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]