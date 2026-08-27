FROM python:3.11-alpine
WORKDIR /app

RUN apk update && apk upgrade --no-cache
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY app.py .
EXPOSE 8080
USER guest
CMD ["python", "app.py"]
