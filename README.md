# Prototipo de Detección con IA

> **Tipo de proyecto:** Prototipo técnico / proyecto de aprendizaje

Prototipo desarrollado para experimentar con detección de objetos usando **FastAPI**, **YOLOv8** y **OpenCV**.

Este repositorio unifica las pruebas que anteriormente estaban separadas para **Google Cloud Run** y **Fly.io**.

## Tecnologías

- Python
- FastAPI
- YOLOv8 / Ultralytics
- OpenCV
- NumPy
- Jinja2
- Docker
- Google Cloud Run
- Fly.io

## Funcionalidades

- Detección de objetos mediante YOLO
- Procesamiento de imágenes con OpenCV
- API REST con FastAPI
- Interfaz web con Jinja2
- Configuración CORS mediante variables de entorno
- Contenerización con Docker
- Configuración de despliegue para Cloud Run y Fly.io

## Estructura

```text
app/
├── main.py
├── models/
├── routers/
└── utils/

static/
templates/
Dockerfile
cloudbuild.yaml
fly.toml
requirements.txt
```

## Instalación

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Ejecución local

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible normalmente en:

```text
http://localhost:8000
```

La documentación interactiva de FastAPI puede consultarse en:

```text
http://localhost:8000/docs
```

## Configuración CORS

Los orígenes adicionales pueden definirse mediante la variable:

```text
FRONTEND_ORIGINS=https://frontend1.com,https://frontend2.com
```

## Despliegue

### Google Cloud Run

El repositorio incluye `cloudbuild.yaml` para el flujo de construcción y despliegue.

### Fly.io

El repositorio incluye `fly.toml` y utiliza la variable `PORT` proporcionada por la plataforma.

## Muestra

![Ejemplo de detección](./animales.jpeg)

## Nota

Este proyecto es un prototipo técnico y no representa un sistema utilizado en producción.

---

**Autor:** Miguel Martínez
