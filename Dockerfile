# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements and install dependencies into a wheel store / site-packages
COPY app/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Hardened Distroless Runtime Stage
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local
# Copy application files
COPY app/ /app

# Switch to built-in non-root user
USER nonroot:nonroot

EXPOSE 8080

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Safe execution entrypoint using gunicorn
ENTRYPOINT ["python3", "-m", "gunicorn.app.wsgiapp", "-b", "0.0.0.0:8080", "app:app"]