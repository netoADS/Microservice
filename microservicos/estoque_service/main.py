# estoque_service/main.py
from fastapi import FastAPI, HTTPException
from .database import db
import requests

app = FastAPI()
PRODUTO_SERVICE_URL = "http://localhost:8000/produtos"

@app.put("/estoque/{nome}")
def atualizar_quantidade(nome: str, quantidade: int):
    # Verifica se o produto existe no microsserviço de produtos
    response = requests.get(f"{PRODUTO_SERVICE_URL}/{nome}")
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.atualizar_quantidade(nome, quantidade)
    return {"message": f"Quantidade de '{nome}' atualizada para {quantidade}"}

@app.delete("/estoque/{nome}")
def remover_produto(nome: str):
    # Verifica se o produto existe no microsserviço de produtos
    response = requests.get(f"{PRODUTO_SERVICE_URL}/{nome}")
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.remover_produto(nome)
    return {"message": f"Produto '{nome}' removido do estoque"}
