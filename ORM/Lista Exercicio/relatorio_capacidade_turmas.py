from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db")

with Session(engine) as session:
    stmt = (
        select(
            Aluno.turma_id,
            func.count(Aluno.id)
        )
        .group_by(Aluno.turma_id)
        .having(func.count(Aluno.id) > 30)
    )

    resultados = session.execute(stmt).all()

    print("=== Relatório de Capacidade de Turmas (> 30 Alunos) ===")
    for turma_id, total_alunos in resultados:
        print(f"Turma ID: {turma_id} | Total de Alunos: {total_alunos}")