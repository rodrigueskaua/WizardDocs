from core.config import settings
from openai import OpenAI

client = OpenAI(api_key=settings.openai_api_key)

def ask_openai(question: str, context: str) -> str:
  prompt = (
    "Com base no contexto extraído de um PDF, responda à pergunta de forma clara, direta e objetiva.\n\n"
    f"Contexto extraído:\n{context}\n\n"
    f"Pergunta: {question}\n\n"
    "Resposta:"
  )

  response = client.chat.completions.create(model="gpt-3.5-turbo",
  messages = [
    {
      "role": "system",
      "content": (
        "Você é um assistente sempre , especializado em compreender e responder perguntas com base em textos de documentos. "
        "Caso a informação solicitada não esteja presente no contexto fornecido, diga de forma clara e educada que não foi possível encontrar a resposta no documento, "
        "ou que talvez não tenha conseguido interpretá-la corretamente, reforçando que o assistente está em constante aprimoramento. "
        "Se o usuário fizer uma crítica sobre a resposta, agradeça pelo feedback, reconheça a limitação e informe que este assistente está em desenvolvimento e aprendendo continuamente. "
        "Se o usuário apenas agradecer ou elogiar, responda de forma simpática e breve, como: "
        "'Disponha! Estou aqui sempre que precisar 😊 Ainda estou em aprimoramento, então seu feedback é muito importante para mim!'"
      )
    },
    {
      "role": "user",
      "content": prompt
    }
  ],
  temperature=0.7,
  max_tokens=1000)

  return response.choices[0].message.content.strip()

def generate_summary(text: str) -> str:
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": (
          "Você é um assistente especializado em interpretar documentos PDF e gerar resumos objetivos e claros. "
          "Escreva um resumo conciso que capture os principais tópicos e a intenção geral do documento."
        )
      },
      {
        "role": "user",
        "content": f"Gere um resumo geral do seguinte conteúdo:\n\n{text}"
      }
    ],
    temperature=0.5,
    max_tokens=500
  )

  return response.choices[0].message.content.strip()