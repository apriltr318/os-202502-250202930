# Menggunakan image Python yang stabil dan ringan
FROM python:3.9-slim

# Set folder kerja di dalam Docker
WORKDIR /app

# Salin hanya file yang dibutuhkan untuk simulasi kasir
COPY main.py .
COPY dataset.csv .

# Perintah menjalankan simulasi kasir
CMD ["python", "main.py"]