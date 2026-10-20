from datetime import date
from sqlalchemy import create_engine, select, or_
from sqlalchemy.orm import Session
from modelos_escola import Aluno, Turma

engine = create_engine("sqlite:///escola.db")

with Session(engine) as session:
    turma = session.scalars(
        select(Turma).filter_by(nome_turma="3º Ano A")
    
).first()

    print("=== Turma ===")
    print(turma)

    alunos = session.scalars(
        select(Aluno).filter(
            or_(
                Aluno.data_nascimento > date(2005, 12, 31),
                Aluno.email.like("%@escola.com")
            )
        )
    ).all()

    print("\n=== Alunos ===")
    for aluno in alunos:
        print(aluno)