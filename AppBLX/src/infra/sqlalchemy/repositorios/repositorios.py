from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas.schemas import Produto, Usuario, Pedido


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass


class RepositorioUsuario():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: Usuario):
        db_usario = models.Usuario(
            nome=usuario.nome,
            telefone=usuario.telefone
        )
        self.db.add(db_usario)
        self.db.commit()
        self.db.refresh(db_usario)
        return db_usario

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios

    def obter(self):
        pass

    def remover(self):
        pass


class RepositorioPedido():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, pedido: Pedido):
        db_pedido = models.Pedido(
            quantidade=pedido.quantidade,
            entrega=pedido.entrega,
            endereco=pedido.endereco,
            observacoes=pedido.observacoes
        )

        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)
        return db_pedido

    def listar(self):
        pedidos = self.db.query(models.Pedido).all()
        return pedidos

    def obter(self):
        pass

    def remover(self):
        pass