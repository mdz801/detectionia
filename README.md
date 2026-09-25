# Prototipo de Detección con IA

> **Tipo de proyecto:** Prototipo técnico / proyecto de aprendizaje

Prototipo desarrollado para experimentar con detección de objetos usando **FastAPI**, **YOLOv8** y **OpenCV**.

El objetivo principal fue practicar integración de visión por computadora con una API web, contenerización y despliegue cloud.

## Tecnologías

- Python
- FastAPI
- YOLOv8 / Ultralytics
- OpenCV
- NumPy
- Jinja2
- Docker
- Google Cloud Build / Cloud Run

## Funcionalidades

- Detección de objetos
- Inferencia con YOLO
- Procesamiento de imágenes con OpenCV
- API mediante FastAPI
- Interfaz web con Jinja2
- Recursos estáticos
- Configuración CORS
- Dockerfile para contenerización

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

Luego puede abrirse:

```text
http://localhost:8000
```

La documentación interactiva de FastAPI está disponible normalmente en:

```text
http://localhost:8000/docs
```

## Muestra

![Ejemplo de detección](./animales.jpeg)

## Nota

Este repositorio es un prototipo técnico y no representa un sistema utilizado en producción.

---

**Autor:** Miguel Martínez
