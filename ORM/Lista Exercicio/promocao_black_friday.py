from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db")

with Session(engine) as session:
    stmt_base = select(Produto).filter_by(em_estoque=True)
    stmt_promocao = stmt_base.add_columns((Produto.preco * 0.85).label("preco_promocional"))

    resultados = session.execute(stmt_promocao).all()

    print("=== Promoção Black Friday (15% OFF) ===")
    for prod, preco_promo in resultados:
        print(f"Produto: {prod.nome} | Preço Original: R$ {prod.preco:.2f} | Preço Promocional: R$ {preco_promo:.2f}")