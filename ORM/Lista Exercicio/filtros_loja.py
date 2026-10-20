from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db")

with Session(engine) as session:
    produtos_em_estoque = session.scalars(
        select(Produto).filter_by(em_estoque=True)
    ).all()

    print("=== Produtos em Estoque ===")
    for prod in produtos_em_estoque:
        print(prod)

    print("\n" + "=" * 30 + "\n")

    produtos_gamer_caros = session.scalars(
        select(Produto).filter(
            Produto.preco > 100.00,
            Produto.nome.ilike("%Gamer%"))).all()

    print("=== Produtos Gamer acima de R$ 100,00 ===")
    for prod in produtos_gamer_caros:
        print(prod)