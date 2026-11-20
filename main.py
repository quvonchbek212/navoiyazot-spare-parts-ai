"""Navoiyazot Logistics: Spare Parts Control Service."""
import logging
import uvicorn
from fastapi import FastAPI
from parts_control.router import router as parts_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

app = FastAPI(
    title="Navoiyazot Logistics · Spare Parts Control API",
    description="Automated parts lifecycle management, cross-compatibility validation, and theft prevention for Navoiyazot.",
    version="1.0.0"
)

app.include_router(parts_router)

@app.get("/healthz", tags=["Health"])
async def healthz():
    return {"status": "ok", "service": "parts-control"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=False)
