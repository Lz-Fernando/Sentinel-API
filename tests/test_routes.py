from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"mensagem": "API de verificação de fraude online"}
  
def test_verificar_mensagem():
  payload = {"descricao": "Este é um teste de fraude"}
  response = client.post("/verificar", json=payload)
  assert response.status_code == 200
  assert "resultado" in response.json()