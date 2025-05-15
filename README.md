# Sentinel-API

## Descrição
O **Sentinel-API** é uma API desenvolvida em Python com o framework FastAPI para verificar mensagens e identificar possíveis fraudes. O projeto utiliza um modelo de aprendizado de máquina previamente treinado para realizar a classificação.

---

## Estrutura do Projeto

```
Sentinel-API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── utils.py
│
├── models/
│   ├── modelo.joblib
│   └── tfidf_vectorizer.joblib
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   └── test_utils.py
│
├── requirements.txt
└── README.md
```

---

## Instalação Local

### Pré-requisitos
- Python 3.10 ou superior
- pip instalado

### Passos

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd Sentinel-API
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Certifique-se de que os arquivos `modelo.joblib` e `tfidf_vectorizer.joblib` estão na pasta `models/`.**

5. **Execute a aplicação localmente:**
   ```bash
   python app/main.py
   ```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Hospedagem no Render

### Como implantar no Render

1. **Crie um novo serviço Web Service no Render**
   - Conecte o repositório do projeto ao Render.
   - Escolha o runtime do Python.

2. **Configuração do Build e Start Command**
   - **Build Command:**  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**  
     ```bash
     uvicorn app.main:app --host 0.0.0.0 --port $PORT
     ```

3. **Variáveis de Ambiente**
   - Adicione a variável de ambiente `PORT` se necessário (o Render normalmente define automaticamente).

4. **Modelos**
   - Certifique-se de que os arquivos `modelo.joblib` e `tfidf_vectorizer.joblib` estão na pasta `models/` do repositório.

5. **Deploy**
   - O Render fará o deploy automaticamente após a configuração.

6. **Acessando a API**
   - Após o deploy, a API estará disponível em uma URL gerada pelo Render, como:
     ```
     https://sentinel-api.onrender.com
     ```
   - Substitua pela URL gerada para o seu serviço.

---

## Endpoints

### `GET /`
- **Descrição:** Retorna uma mensagem de boas-vindas.
- **Resposta:**
  ```json
  {
    "mensagem": "API de verificação de fraude online"
  }
  ```

### `POST /verificar`
- **Descrição:** Verifica se uma mensagem é fraude.
- **Corpo da Requisição:**
  ```json
  {
    "descricao": "Texto da mensagem a ser verificada"
  }
  ```
- **Resposta:**
  ```json
  {
    "resultado": "FRAUDE" ou "OK"
  }
  ```

---

## Testes

### Executar os testes localmente

Para rodar os testes unitários, execute:

```bash
python -m unittest discover -s tests
```

Os testes cobrem:
- Funções utilitárias (`utils.py`)
- Rotas da API (`routes.py`)

---

## Dependências

As principais dependências do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalá-las antes de executar o projeto:

- fastapi
- uvicorn
- joblib
- httpx

---

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature/bugfix:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Descrição da alteração"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---