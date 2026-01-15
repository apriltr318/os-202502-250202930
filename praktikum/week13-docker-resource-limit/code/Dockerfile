FROM python:3.9-slim

# Tentukan direktori kerja
WORKDIR /app

# Menyalin file script kita ke dalam container
# Kamu kurang kata 'COPY' di depan app.py
COPY app.py .

# Menjalankan script saat container dinyalakan
# Kamu kurang kata 'CMD' dan formatnya harus pakai ["python", "app.py"]
CMD ["python", "app.py"]