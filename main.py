from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pathlib

app = FastAPI()

BASE_DIR = pathlib.Path(__file__).resolve().parent


@app.get("/", response_class=HTMLResponse)
def landing():
    html_path = BASE_DIR / "index.html"
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))