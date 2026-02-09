from fastapi import FastAPI
from routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(title="Radiology Reporting Platform")

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
