from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db")

turma_id_alvo = 1

with Session(engine) as session:
    stmt_base = select(Aluno).filter(Aluno.turma_id == turma_id_alvo)
    stmt_com_idade = stmt_base.add_columns(
        (func.strftime("%Y", "now") - func.strftime("%Y", Aluno.data_nascimento)).label("idade_aproximada")
    )

    resultados = session.execute(stmt_com_idade).all()

    print(f"=== Alunos da Turma {turma_id_alvo} ===")
    for aluno, idade in resultados:
        print(f"Aluno: {aluno.nome} | Matrícula: {aluno.matricula} | Idade Aproximada: {idade} anos")