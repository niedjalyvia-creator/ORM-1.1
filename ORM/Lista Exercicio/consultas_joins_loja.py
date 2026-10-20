from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_loja import Categoria, Produto

engine = create_engine("sqlite:///loja_virtual.db")

with Session(engine) as session:
    stmt_inner = select(Produto.nome, Categoria.nome).join(
        Categoria, Produto.categoria_id == Categoria.id
    )
    produtos_categorias = session.execute(stmt_inner).all()

    print("=== Produtos e suas Categorias ===")
    for prod_nome, cat_nome in produtos_categorias:
        print(f"Produto: {prod_nome} | Categoria: {cat_nome}")

    stmt_anti = (
        select(Categoria)
        .outerjoin(Produto, Categoria.id == Produto.categoria_id)
        .where(Produto.id == None)
    )
    categorias_orfas = session.scalars(stmt_anti).all()

    print("\n=== Categorias Órfãs ===")
    for cat in categorias_orfas:
        print(cat)