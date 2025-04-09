import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(question: str, context: str) -> str:
  prompt = (
    "Com base no contexto extraído de um PDF, responda à pergunta de forma clara, direta e objetiva.\n\n"
    f"Contexto extraído:\n{context}\n\n"
    f"Pergunta: {question}\n\n"
    "Resposta:"
  )

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
      {
        "role": "system",
        "content": (
          "Você é um assistente especializado em compreender e responder perguntas com base em textos de documentos. "
          "Seja claro, direto e objetivo nas respostas, evitando repetições e floreios desnecessários. "
          "Caso a informação solicitada não esteja presente no contexto fornecido, diga que não foi possível encontrar a resposta."
        )
      },
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=0.7,
    max_tokens=500,
  )

  return response.choices[0].message.content.strip()