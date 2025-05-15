from fastapi import APIRouter
from app.models import Mensagem
from app.services import verificar_fraude

router = APIRouter()

@router.get("/")
def read_root():
  return {"mensagem": "API de verificação de fraude online"}

@router.post("/verificar")
def verificar_mensagem(mensagem: Mensagem):
  resultado = verificar_fraude(mensagem.descricao)
  return {"resultado": resultado}