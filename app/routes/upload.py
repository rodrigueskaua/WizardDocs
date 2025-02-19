from fastapi import APIRouter, UploadFile, File, HTTPException
from services.pdf_extractor import extract_text_from_pdf
from services.file_saver import save_text_to_json
from fastapi.responses import JSONResponse

router = APIRouter()

def validate_pdf(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF são permitidos.")

@router.post("/pdf", summary="Upload de PDF e extração de texto")
async def upload_pdf(file: UploadFile = File(...)):
    validate_pdf(file)
    text = extract_text_from_pdf(file)
    filepath = save_text_to_json(file.filename, text)
    return JSONResponse(content={"filename": file.filename, "filepath": filepath})
