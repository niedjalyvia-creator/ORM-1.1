from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db")

tamanho_pagina = 5
pagina_desejada = 2
offset_valor = (pagina_desejada - 1) * tamanho_pagina

with Session(engine) as session:
    total_produtos = session.scalar(select(func.count(Produto.id)))
    print(f"Total de produtos cadastrados: {total_produtos}")

    categorias_distintas = session.scalars(
        select(Produto.categoria_id).distinct()
    ).all()
    print(f"IDs de categorias distintas: {categorias_distintas}")

    produtos_pagina_2 = session.scalars(
        select(Produto)
        .order_by(Produto.preco.desc())
        .limit(tamanho_pagina)
        .offset(offset_valor)
    ).all()

    print(f"\n=== Produtos da Página {pagina_desejada} (Do mais caro ao mais barato) ===")
    for prod in produtos_pagina_2:
        print(prod)