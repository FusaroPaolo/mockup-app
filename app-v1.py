# Importación de módulos necesarios
from flask import Flask, request, render_template, jsonify, send_file
from rembg import remove
from PIL import Image
from io import BytesIO
import os

# Creación de la instancia de la aplicación Flask
app = Flask(__name__)

# Mockup homepage 
@app.route('/')
def home():
    return render_template('index.html')

# Configuración para entorno de desarrollo
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

# Ruta para listar los archivos disponibles
@app.route('/files', methods=['GET'])
def list_files():
    directory = 'uploads'
    files = os.listdir(directory)
    print(f"Files in {directory}: {files}")
    return jsonify(files)

# Ruta para solicitar un archivo específico
@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    file_path = os.path.join('uploads', filename)
    if os.path.exists(file_path):
        return jsonify({'filename': filename})
    else:
        return jsonify({'error': 'File not found'}), 404

# Ruta para borrar un archivo
@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join('uploads', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'message': 'File deleted successfully'})
    else:
        return jsonify({'error': 'File not found'}), 404

# Ruta para subir un archivo
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Guardar el archivo en el directorio 'uploads'
    file.save(os.path.join('uploads', file.filename))

    return jsonify({'message': 'File uploaded successfully'})

# Ruta para la funcionalidad de rembg-app
@app.route('/rembg', methods=['POST'])
def rembg():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Procesamiento con rembg
    input_image = Image.open(file.stream)
    output_image = remove(input_image, post_process_mask=True)
    img_io = BytesIO()
    output_image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_rmbg.png')

# Inicio de la aplicación en el puerto 5000
if __name__ == '__main__':
    # Creación del directorio 'uploads' si no existe
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Ejecución de la aplicación en el host 0.0.0.0 y puerto 5000 en modo de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)

