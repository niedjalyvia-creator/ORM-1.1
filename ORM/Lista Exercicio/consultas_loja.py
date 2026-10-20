from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db")

with Session(engine) as session:
    produto = session.get(Produto, 1)
    print("1. Por ID:", produto or "Produto não encontrado")

    primeiro = session.scalars(select(Produto)).first()
    print("2. Primeiro:", primeiro)

    todos = session.scalars(select(Produto)).all()
    print("3. Todos:", todos)