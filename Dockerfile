FROM python:3.12-slim
WORKDIR /app

# Copy runtime dependencies only
COPY requirements_docker.txt .

# Upgrade vulnerable packaging components
RUN python -m pip install --no-cache-dir --upgrade \
    pip \
    "setuptools>=78.1.1" \
    "wheel>=0.46.2" \
    "msgpack>=1.2.1"

# Install application dependencies
RUN pip install --no-cache-dir -r requirements_docker.txt

# Copy application
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]