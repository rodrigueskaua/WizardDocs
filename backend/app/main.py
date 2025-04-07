from fastapi import FastAPI
from api.pdf import router as pdf_router
from api.query import router as query_router

app = FastAPI(
    title="WizardDocs API",
    description="Descrição da minha API",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
app.include_router(pdf_router, prefix="/api", tags=["PDF"])
app.include_router(query_router, prefix="/api", tags=["QUERY"])