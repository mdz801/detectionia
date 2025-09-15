
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
import numpy as np
import cv2
import io
import os

router = APIRouter()

# Ruta al modelo entrenado
MODEL_PATH = os.path.join("app", "models", "yolov8n.pt")
model = YOLO(MODEL_PATH)

@router.post("/detect/")
async def detect_circles_ai(file: UploadFile = File(...)):
    # Leer imagen
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Predicción YOLO
    results = model.predict(img)

    # Dibujar cajas
    for r in results[0].boxes:
        x1, y1, x2, y2 = map(int, r.xyxy[0])
        cls = int(r.cls[0])
        conf = float(r.conf[0])

        label = f"{model.names[cls]} {conf:.2f}"
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    _, img_encoded = cv2.imencode(".jpg", img)
    return StreamingResponse(io.BytesIO(img_encoded.tobytes()), media_type="image/jpeg")
