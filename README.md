<h1 align="center">Inference API</h1>

## 馃 Descripci贸n <a name = "about"></a>
Este proyecto es parte de un repositorio de recursos para comenzar a desarrollar proyectos de
investigaci贸n aplicada a nivel licenciatura. El principal objetivo de esta API es mostrar c贸mo
generar una interfaz para utilizar los modelos entrenados en el repositorio [Intro to Machine Learning](https://github.com/helloerikaaa/IntroMachineLearning).

## 馃敄 Estructura del proyecto

```
InferenceAPI/
|- app/                                    # Directorio principal de la API
|- app/routes                              # Directorio donde habitan las rutas
|- app/consts                              # Directorio con constantes 煤tiles
|- app/core                                # Configuraci贸n y seguridad de la API
|- app/models                              # Modelos utilizados dentro de la API
|- app/services                            # Servicios para leer y utilizar el model de ML
|- artifacts/                              # Directorio donde se guarda el modelo y metadatos
|- Pipfile                                 # Archivo con las dependencias del proyecto
|- .pre-commit-config.yaml                 # Archivo de configuraci贸n del pre-commit
|- docker-compose.yaml                     # Archivo para ejecutar docker-compose
|- Dockerfile                              # Archivo para utilizar docker en el proyecto
|- Makefile                                # Archivo para automatizar comandos
```

## 馃弫 C贸mo empezar <a name = "getting_started"></a>

Estas instrucciones generar谩n una copia de este proyecto lista para ejecutarse en tu m谩quina local.

### Requisitos
Prepara tu ambiente e instala las dependencias del proyecto.
* Es necesario tener instalado Docker para correr la API en un ambiente web

Clona el repositorio del proyecto:

```
git clone https://github.com/helloerikaaa/InferenceAPI
```
Instalaci贸n de dependencias y ejecuci贸n del ambiente usando Pipenv:
```
pipenv install
pipenv shell
```

## Variables de entorno
El proyecto necesita de algunas variables que se deben agregar a un archivo llamado `.env`, un ejemplo de estas variables se puede encontrar en el archivo `example.env`. 

## 馃敡 Ambiente local
Para comenzar a utilizar la API es necesario agregar los archivo `model.pkl` y `metada.json` del proyecto Intro to Machine Learning en la carpeta `artifacts/`
Una vez teniendo estos archivos, se puede ejecutar `docker-compose` para ver la interfaz de la API en el navegador. Ejecutar el siguiente comando:
```
make up
```

Ir al navegador, ingresar a la url http://127.0.0.1:8000 y comenzar a utilizar la API de inferencia.

## 鉁嶏笍 Autores
* Erika S谩nchez Femat (helloerikaaa)
