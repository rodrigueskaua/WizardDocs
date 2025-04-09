from PyPDF2 import PdfReader
import re

def extract_text_from_pdf(pdf_file) -> str:
  reader = PdfReader(pdf_file)
  full_text = ""
  for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
      full_text += page_text + "\n"
  return full_text.strip()
  
def split_text_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
  words = re.split(r'(\s+)', text)  # Mantém os espaços entre as palavras
  chunks = []
  current_chunk = ""
  
  for word in words:
    if len(current_chunk) + len(word) <= chunk_size:
      current_chunk += word
    else:
      chunks.append(current_chunk.strip())
      # Próximo chunk com a sobreposição
      overlap_part = current_chunk[-overlap:] if overlap < len(current_chunk) else current_chunk
      current_chunk = overlap_part + word

  if current_chunk:
    chunks.append(current_chunk.strip())
  
  return chunks