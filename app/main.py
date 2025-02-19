from fastapi import FastAPI
from routes.upload import router as upload_router

app = FastAPI(
    title="Intelligent Processing API",
    description="API para processamento WizardDocs",
    version="0.0.1"
)

API_PREFIX = "/api/v1"

# Rotas
app.include_router(upload_router, prefix=f"{API_PREFIX}/upload", tags=["Upload"])

# Rota de verificação de status
@app.get("/", summary="Verificar status da API", tags=["Status"])
def health_check():
    return {"status": "running"}
