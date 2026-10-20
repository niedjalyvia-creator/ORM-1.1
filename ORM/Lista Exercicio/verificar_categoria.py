from sqlalchemy import create_engine, exists, select
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db")

categoria_id_alvo = 1

with Session(engine) as session:
    stmt = select(exists().where(Produto.categoria_id == categoria_id_alvo))
    possui_produtos = session.scalar(stmt)

    if possui_produtos:
        print(f"A categoria {categoria_id_alvo} possui produtos associados.")
    else:
        print(f"A categoria {categoria_id_alvo} NÃO possui produtos associados.")