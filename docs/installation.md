# Instalación

En esta página se explica cómo instalar y ejecutar la API de Cafetería Intergaláctica.

## Requisitos

Antes de instalar el proyecto, asegúrate de tener:

- Python 3.10 o superior.
- Git.
- pip.
- Una cuenta de GitHub.

!!! note "Entorno virtual"

    Se recomienda utilizar un entorno virtual para mantener las dependencias de este proyecto separadas de otros proyectos de Python.

## Clonar el repositorio

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/TU-USUARIO/intergalactic-snack-api.git
```

Entra en la carpeta del proyecto:

```bash
cd intergalactic-snack-api
```

## Crear un entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS o Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

La documentación interactiva generada por FastAPI estará disponible en:

```text
http://127.0.0.1:8000/docs
```

La documentación alternativa de ReDoc estará disponible en:

```text
http://127.0.0.1:8000/redoc
```

!!! warning "Servidor de desarrollo"

    La opción `--reload` debe utilizarse durante el desarrollo. Esta opción reinicia automáticamente el servidor cuando detecta cambios en el código fuente.

## Ejecutar el sitio de MkDocs

Abre una segunda terminal y ejecuta:

```bash
mkdocs serve --dev-addr 127.0.0.1:8001
```

El sitio de documentación estará disponible en:

```text
http://127.0.0.1:8001
```

## Construir el sitio

Para comprobar que el sitio puede construirse correctamente, ejecuta:

```bash
mkdocs build
```

MkDocs creará una carpeta llamada `site`.

Puedes continuar con la documentación de los [endpoints de la API](endpoints.md).