from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.register import router as register_router
from app.config.settings import settings

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION,

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)

app.include_router(
    register_router,
    prefix="/api/v1/register",
    tags=["Register"]
)
@app.get("/")
def root():
    return {
        "application": "InvoiceAI Backend",
        "version": "0.1.0",
        "status": "running",
        "documentation": "/docs"
    }