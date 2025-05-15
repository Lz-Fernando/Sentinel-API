import string
import unicodedata

def process_text_conteudo(conteudo: str) -> str:
  nopont = ''.join([char for char in conteudo if char not in string.punctuation])
  nopont = nopont.lower()
  nopont = unicodedata.normalize("NFKD", nopont).encode("ASCII", "ignore").decode("ASCII")
  return nopont

def tokenize_text(conteudo):
  return conteudo.split()