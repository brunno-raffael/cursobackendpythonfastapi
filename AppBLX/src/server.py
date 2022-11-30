from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, Usuario, Pedido
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorios import RepositorioProduto, RepositorioUsuario, RepositorioPedido

criar_bd()

app = FastAPI()


@app.post('/produtos')
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuarios')
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios')
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.post('/pedidos')
def criar_pedidos(pedido: Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    return pedido_criado


@app.get('/pedidos')
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos
