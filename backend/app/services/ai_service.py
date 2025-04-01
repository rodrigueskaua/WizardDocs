import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer_with_openai(question, context):
    """
    Gera uma resposta usando a API da OpenAI.
    """
    prompt = f"Contexto: {context}\n\nPergunta: {question}\nResposta:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response["choices"][0]["text"].strip()
