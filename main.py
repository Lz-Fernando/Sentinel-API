from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import nltk
import unicodedata
import string
import os

# Inicializando a aplicação FastAPI
app = FastAPI()

# Função para pré-processamento de texto
def process_text_conteudo(conteudo: str) -> str:
  
  # Remove pontuação
  nopont = ''.join([char for char in conteudo if char not in string.punctuation])
  
  # Converte para minúsculas
  nopont = nopont.lower()
  
  # Remove acentos
  nopont = unicodedata.normalize("NFKD", nopont).encode("ASCII", "ignore").decode("ASCII")
  
  return nopont

# Função de tokenização (opcional para vetorizador)
def tokenize_text(conteudo):
  return conteudo.split()

# Carregando o modelo treinado e o vetor TF-IDF na inicialização da API
base_dir = os.path.dirname(__file__)
modelo = pickle.load(open(os.path.join(base_dir, 'modelo.pk1'), 'rb'))
vectorizer = pickle.load(open(os.path.join(base_dir, 'tfidf_vectorizer.pk1'), 'rb'))

# Definição do esquema de entrada para a API
class Mensagem(BaseModel):
  descricao: str

# Endpoint para verificar se uma mensagem é fraude ou não
@app.post("/verificar")
def verificar_mensagem(mensagem: Mensagem):
  # Pré-processa a mensagem recebida
  texto_processado = process_text_conteudo(mensagem.descricao)
  
  # Transforma a mensagem para o formato esperado pelo modelo
  texto_transformado = vectorizer.transform([texto_processado])
  
  # Faz a previsão
  predicao = modelo.predict(texto_transformado)
  
  # Retorna o resultado
  return {"resultado": "FRAUDE" if predicao[0] == 1 else "OK"}


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  uvicorn.run("main:app", host = "127.0.0.1", port = port)