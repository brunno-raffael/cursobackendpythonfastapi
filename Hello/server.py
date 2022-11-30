from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Olá FastAPI - TDS 2022.2"}


@app.get("/profile")
async def profile():
    return {"nome": "Brunno Raffael"}


@app.post("/profile")
async def criar():
    return {"message": "Perfil criado com sucesso!"}


@app.put("/profile")
async def atualizar():
    return {"message": "Perfil atualizado com sucesso!"}


@app.delete("/profile")
async def remover():
    return {"message": "Perfil removido com sucesso!"}


@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, tudo me paz?!'
    return {"message": texto}


@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    valor_quadrado = numero * numero
    texto = f'O quadrado de {numero} é {valor_quadrado}!'
    return {"message": texto}


@app.get('/dobro/')
def dobro(valor: int):
    valor_dobro = valor + valor
    texto = f'O dobro de {valor} é {valor_dobro}!'
    return {"message": texto}


@app.get('/area-retangulo/')
def area_retangulo(largura: int, altura: int = 1):
    valor_area = largura * altura
    texto = f'A area do retangulo da largura {largura} e altura {altura} é {valor_area}!'
    return {"message": texto}


class Produto(BaseModel):
    nome: str
    valor: float


@app.post('/produtos')
def produtos(produto: Produto):
    return {"message": 'Produto ({} - R$ {}) cadastrado com sucesso!'.format(produto.nome, produto.valor)}
