from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse

from analyse import analyse
import logging


logging.basicConfig(
    level=logging.INFO,  # Show INFO and higher
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse("static/index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/analyse")
async def analyse_endpoint(request: Request):
    data = await request.json()
    logs = analyse(
        data.get("video_url"),
        data.get("brand"),
        data.get("brand_variations"),
        data.get("products"),
        data.get("categories"),
        data.get("cta"),
    )
    return JSONResponse(content=logs)
