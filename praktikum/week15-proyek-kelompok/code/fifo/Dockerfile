# Gunakan image Python yang ringan
FROM python:3.10-slim

# Set folder kerja di dalam container
WORKDIR /app

# Salin semua file dari folder lokal ke dalam container
# Termasuk main.py dan dataset.csv
COPY . .

# Perintah untuk menjalankan aplikasi saat container dimulai
CMD ["python", "main.py"]