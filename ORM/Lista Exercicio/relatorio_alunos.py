from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db")

pagina_atual = 3
tamanho_pagina = 10
offset_valor = (pagina_atual - 1) * tamanho_pagina

with Session(engine) as session:
    total_alunos = session.scalar(select(func.count(Aluno.id)))
    print(f"Total de alunos matriculados: {total_alunos}")

    alunos_paginados = session.scalars(
        select(Aluno)
        .order_by(Aluno.nome.asc())
        .limit(tamanho_pagina)
        .offset(offset_valor)
    ).all()

    print(f"\n=== Alunos da Página {pagina_atual} ===")
    for aluno in alunos_paginados:
        print(aluno)