from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .database import db

app = FastAPI()

# Definindo o modelo de dados do produto com Pydantic
class Produto(BaseModel):
    nome: str
    quantidade: int
    preco: float

@app.post("/produtos")
def adicionar_produto(produto: Produto):
    # Adiciona o produto ao banco de dados
    db.adicionar_produto(produto.dict())
    return {"message": "Produto adicionado com sucesso"}

@app.get("/produtos")
def listar_produtos():
    produtos = db.listar_produtos()
    return produtos

@app.get("/produtos/{nome}")
def buscar_produto(nome: str):
    produto = db.buscar_produto(nome)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
