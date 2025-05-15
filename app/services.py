import os
import joblib
from app.utils import process_text_conteudo

base_dir = os.path.dirname(__file__)
modelo = joblib.load(open(os.path.join(base_dir, '../models/modelo.joblib'), 'rb'))
vectorizer = joblib.load(open(os.path.join(base_dir, '../models/tfidf_vectorizer.joblib'), 'rb'))

def verificar_fraude(descricao: str) -> str:
  texto_processado = process_text_conteudo(descricao)
  texto_transformado = vectorizer.transform([texto_processado])
  predicao = modelo.predict(texto_transformado)
  return "FRAUDE" if predicao[0] == 1 else "LEGÍTIMO"