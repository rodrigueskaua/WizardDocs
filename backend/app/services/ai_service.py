from core.config import settings
from openai import OpenAI

client = OpenAI(api_key=settings.openai_api_key)

def openai_chat_completion(system_prompt: str, user_prompt: str, temperature: float = 0.7, max_tokens: int = 1000) -> str:
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_prompt}
    ],
    temperature=temperature,
    max_tokens=max_tokens
  )
  return response.choices[0].message.content.strip()

def ask_openai(question: str, context: str) -> str:
  system_prompt = (
    "Você é um assistente especializado em compreender e responder perguntas com base em textos de documentos. "
    "Caso a informação solicitada não esteja presente no contexto fornecido, diga educadamente que não foi possível encontrar a resposta, "
    "e destaque que está em constante aprimoramento. "
    "Se o usuário fizer uma crítica, agradeça o feedback, reconheça a limitação e reforce que está em desenvolvimento. "
    "Se o usuário agradecer ou elogiar, responda de forma simpática, como: "
    "'Disponha! Estou aqui sempre que precisar 😊 Seu feedback é muito importante para mim!'"
  )
  
  user_prompt = (
    "Com base no contexto extraído de um PDF, responda à pergunta de forma clara, direta e objetiva.\n\n"
    f"Contexto extraído:\n{context}\n\n"
    f"Pergunta: {question}\n\n"
    "Resposta:"
  )
    
  return openai_chat_completion(system_prompt, user_prompt)

def generate_summary(text: str) -> str:
  system_prompt = (
    "Você é um assistente especializado em interpretar documentos PDF e gerar resumos objetivos e claros. "
    "Escreva um resumo conciso que capture os principais tópicos e a intenção geral do documento."
  )

  user_prompt = f"Gere um resumo geral do seguinte conteúdo:\n\n{text}"

  return openai_chat_completion(system_prompt, user_prompt, temperature=0.5, max_tokens=500)