from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
  """
  Extrai o texto de um arquivo PDF.
  """
  reader = PdfReader(pdf_file)
  text = ""
  for page in reader.pages:
      text += page.extract_text()
  return text

def split_text_into_chunks(text, chunk_size=500, overlap=50):
  """
  Divide o texto em chunks menores com sobreposição para garantir continuidade.
  """
  chunks = []
  for i in range(0, len(text), chunk_size - overlap):
      chunk = text[i:i + chunk_size]
      chunks.append(chunk)
  return chunks