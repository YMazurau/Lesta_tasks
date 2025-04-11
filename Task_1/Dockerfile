FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN useradd -m userym

USER userym

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
