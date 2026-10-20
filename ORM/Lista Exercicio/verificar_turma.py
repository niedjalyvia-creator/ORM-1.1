from sqlalchemy import create_engine, exists, select
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db")

turma_id_alvo = 5

with Session(engine) as session:
    stmt = select(exists().where(Aluno.turma_id == turma_id_alvo))
    tem_alunos = session.scalar(stmt)

    if tem_alunos:
        print(f"Existem alunos matriculados na turma {turma_id_alvo}.")
    else:
        print(f"Não existem alunos matriculados na turma {turma_id_alvo}.")