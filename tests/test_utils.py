import unittest
from app.utils import process_text_conteudo, tokenize_text

class TestUtils(unittest.TestCase):
  def test_process_text_conteudo(self):
    texto = "Olá, mundo! Isso é um teste."
    resultado = process_text_conteudo(texto)
    esperado = "ola mundo isso e um teste"
    self.assertEqual(resultado, esperado)
    
  def test_tokenize_text(self):
    texto = "Isso é um teste simples"
    resultado = tokenize_text(texto)
    esperado = ["Isso", "é", "um", "teste", "simples"]
    self.assertEqual(resultado, esperado)
    
if __name__ == "__main__":
  unittest.main()