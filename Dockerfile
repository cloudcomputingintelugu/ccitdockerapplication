FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade packaging tools and vulnerable dependencies
RUN python -m pip install --upgrade \
    pip \
    setuptools \
    wheel \
    jaraco.context

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]