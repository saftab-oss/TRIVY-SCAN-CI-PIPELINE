FROM python:3.11-slim AS builder
WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends gcc || true
FROM python:3.11-alpine

WORKDIR /app

COPY --from=builder /build /app
COPY app.py .

EXPOSE 8080

USER guest

CMD ["python", "app.py"]
