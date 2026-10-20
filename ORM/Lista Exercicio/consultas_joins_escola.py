from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_escola import Aluno, Turma

engine = create_engine("sqlite:///escola.db")

with Session(engine) as session:
    stmt_left = select(Aluno.nome, Turma.nome_turma).outerjoin(
        Turma, Aluno.turma_id == Turma.id
    )
    alunos_turmas = session.execute(stmt_left).all()

    print("=== Alunos e suas Turmas ===")
    for aluno_nome, turma_nome in alunos_turmas:
        print(f"Aluno: {aluno_nome} | Turma: {turma_nome or 'Sem Turma'}")

    stmt_anti = (
        select(Aluno)
        .outerjoin(Turma, Aluno.turma_id == Turma.id)
        .where(Turma.id == None)
    )
    alunos_sem_turma = session.scalars(stmt_anti).all()

    print("\n=== Alunos sem Turma ===")
    for aluno in alunos_sem_turma:
        print(aluno)