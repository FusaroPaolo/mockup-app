# Microservicio de Gestión de Archivos

Como parte del desafio técnico propuesto por DataRocking este microservicio proporciona funcionalidades básicas para gestionar archivos: solicitar un archivo, listar archivos disponibles, borrar un archivo y aunque no estaba en la consigna soporta que se suban nuevos archivos.

## Estructura de archivos

- `deploy_script.py`: Script que automatiza el despliegue del microservicio.
- `app.py`: Código fuente del microservicio.
- `Dockerfile`: Script para construir la imagen Docker.
- `requirements.txt`: Archivo de requisitos para instalar los módulos de python.
- `uploads/`: Carpeta para almacenar archivos.
- `README.md`: Documentación.


## Requerimientos
 
Versiones utilizadas en este proyecto
  
- Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1
- pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

## Ejecución
   
   ```bash
   python3 deploy_script.py 8080
   ```

## Intrucciones de uso

La app por una parte levanta una página web básica que a la cuál se puede acceder desde un navegador con la ruta http://localhost:8080/ . La misma es solo un homepage con la opción de Ver los achivos almacenados en formato json.

Para interactuar con estos archivos se recomienda utilizar curl desde otra terminal.
Actualmente existe un despliegue de prueba en el cluster data-tools en fargate al cuál se puede acceder con:

Para armar la imagen:
docker build -t mockup-app-rembg .

Para descargar los datos pre entrenados:
 wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx

```bash
 curl http://3.128.181.4:5000/files
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
