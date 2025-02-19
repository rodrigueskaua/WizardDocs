from fastapi import APIRouter, UploadFile, File
from services.pdf_extractor import extract_text_from_pdf
from services.file_saver import save_text_to_json
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload/pdf", summary="Upload de PDF e extração de texto")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    filepath = save_text_to_json(file.filename, text)
    return JSONResponse(content={"filename": file.filename, "filepath": filepath})
