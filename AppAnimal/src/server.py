from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

origins = [
    "http://localhost",
    'http://localhost:5500',
    'http://127.0.0.1:5500',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: str
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List[Animal] = []

def get_animal(animal_id):
    for animal in banco:
        if animal_id == animal.id:
            return animal
    return None   

def get_animal_index(animal_id):
    for index, animal in enumerate(banco):
        if animal_id == animal.id:
            return index
    return -1    

@app.get('/animais')
def listar_animais():
    return banco

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    animal = get_animal(animal_id)
    return animal if animal is not None else {"erro":"Animal não encontrado!"}

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = get_animal_index(animal_id)

    if posicao != -1:
        banco.pop(posicao)
        return {"message":"Animal removido com sucesso!"}
    else:
        return {"message":"Animal não localizado!"}   


@app.post('/animais')
def criar_animais(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return {"message":f"Animal cadastro com sucesso! Id: {animal.id}"}  


