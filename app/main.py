from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from app.routers import detect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware  # ← AÑADIR ESTO

app = FastAPI()

# ← AÑADIR CORS AQUÍ
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4321",  # Tu frontend Astro
        "http://127.0.0.1:4321",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://zw8p15j6-4321.brs.devtunnels.ms"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Incluir router de detección
app.include_router(detect.router)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})