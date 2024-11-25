# Aplicación de procesamiento de imágenes

Esta aplicación fue creara a para se utilizada como mockup y probar distintas funcionalidades. Respuestas http, manejo de archivos y rendimiento de procesamiento de imágenes (reconocimiento de bordes y eliminación de fondo).

## Estructura de archivos

- `deploy_script.py`: Script que automatiza el despliegue del microservicio.
- `app.py`: Código fuente del microservicio.
- `Dockerfile`: Script para construir la imagen Docker.
- `requirements.txt`: Archivo de requisitos para instalar los módulos de python.
- `uploads/`: Carpeta para almacenar archivos.
- `u2net.onnx`: Datos pre entrenados para procesar la imágenes
- `README.md`: Documentación.


## Requerimientos
 
Versiones utilizadas en este proyecto
  
- Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1
- pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

## Intrucciones de uso

La app despliega un webpage en http://localhost:8080/. La aplicación premite subir imágenes en cualquier formato reconoce los bordes del objeto de pricipal de una imágen separando este de su fondo y devolviendo una nueva imagén en formato png. También se pueden los registros de los achivos procesados en formato json.

Para interactuar con estos archivos se recomienda utilizar curl desde otra terminal.
Actualmente existe un despliegue de prueba en el cluster data-tools en fargate al cuál se puede acceder con:

Para armar la imagen:
docker build -t mockup-app-rembg .

Para descargar los datos pre entrenados:

```bash
 wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
```

- Listar archivos:

  ```bash
   curl -X GET http://localhost:8080/files
   	o
   curl http://localhost:8080/files
  ```
- Solicitar un archivo específico:

  ```bash
   curl -X GET http://localhost:8080/files/<nombre_archivo>
   	o
   curl http://localhost:8080/files/<nombre_archivo>
  ```

- Borrar un archivo:

  ```bash
   curl -X DELETE http://localhost:8080/files/<nombre_archivo>

- Subir un nuevo archivo:

  ```bash
   curl -X POST -F "file=@/home/user/<path_del_archivo>/<nombre_archivo>" http://localhost:8080/upload

Estos a también puede verse refrescando el navegador en la ruta http://localhost:8080/files

## Acerca de la App

El microservicio en sí esta definido en app.py y utiliza Flask para armar una APIrest y contiene la lógica con los métodos para manejar los archivos. Se armó además una homepage simple en donde se pueden ver los cambios de los archivos.

El script de docker arma la imagen utilizando como base la imagen oficial python:3.8 desde DockerHub. Se copian los archivos necesarios a la carpeta /app  partir python:3.8 y corre en script de python con la app.

Se implemento además un script de python que automatiza el despliegue del contenedor y que pide especificar el puerto a exponer como parámetro.
