FROM python:3.9

COPY u2net.onnx /home/.u2net/u2net.onnx

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos y carpetas

COPY . .

CMD ["python", "app.py"]

