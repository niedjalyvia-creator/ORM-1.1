from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db")

with Session(engine) as session:
    aluno = session.get(Aluno, 1)
    if aluno:
        print(f"1. Aluno id=1 -> Matrícula: {aluno.matricula}, Nome: {aluno.nome}")
    else:
        print("1. Aluno de id=1 não encontrado.")

    print("\n2. Todos os alunos (via session.query):")
    alunos = session.query(Aluno).all()
    for a in alunos:
        print("  -", a)

    print("\n3a. Sem .scalars():")
    sem_scalars = session.execute(select(Aluno)).all()
    print("Retorno:", sem_scalars)

    print("\n3b. Com .scalars():")
    com_scalars = session.execute(select(Aluno)).scalars().all()
    print("Retorno:", com_scalars)