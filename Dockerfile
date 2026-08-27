FROM python:3.11-alpine
WORKDIR /app

# Patch OS-level packages — fixes libcrypto3/libssl3 CVEs
RUN apk update && apk upgrade --no-cache

# Patch Python toolchain — fixes jaraco.context/wheel CVEs
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY --from=builder /build /app
COPY app.py .
EXPOSE 8080
USER guest
CMD ["python", "app.py"]
