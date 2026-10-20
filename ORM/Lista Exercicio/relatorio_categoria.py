from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db")

with Session(engine) as session:
    stmt = (
        select(
            Produto.categoria_id,
            func.avg(Produto.preco),
            func.count(Produto.id)
        )
        .group_by(Produto.categoria_id)
        .having(func.avg(Produto.preco) > 250.00)
    )

    resultados = session.execute(stmt).all()

    print("=== Relatório Gerencial por Categoria (Preço Médio > R$ 250,00) ===")
    for cat_id, preco_medio, total_produtos in resultados:
        print(f"Categoria ID: {cat_id} | Preço Médio: R$ {preco_medio:.2f} | Total Produtos: {total_produtos}")