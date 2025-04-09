from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import string
import unicodedata
import os
import uvicorn

app = FastAPI()

def process_text_conteudo(conteudo: str) -> str:
    nopont = ''.join([char for char in conteudo if char not in string.punctuation])
    nopont = nopont.lower()
    nopont = unicodedata.normalize("NFKD", nopont).encode("ASCII", "ignore").decode("ASCII")
    return nopont

def tokenize_text(conteudo):
  return conteudo.split()
    
base_dir = os.path.dirname(__file__)
modelo = joblib.load(open(os.path.join(base_dir, 'modelo.joblib'), 'rb'))
vectorizer = joblib.load(open(os.path.join(base_dir, 'tfidf_vectorizer.joblib'), 'rb'))

class Mensagem(BaseModel):
    descricao: str

@app.get("/")
def read_root():
    return {"mensagem": "API de verificação de fraude online"}

@app.post("/verificar")
def verificar_mensagem(mensagem: Mensagem):
    texto_processado = process_text_conteudo(mensagem.descricao)
    texto_transformado = vectorizer.transform([texto_processado])
    predicao = modelo.predict(texto_transformado)
    return {"resultado": "FRAUDE" if predicao[0] == 1 else "OK"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
