from sqlalchemy import create_engine
from modelos_escola import Base

engine = create_engine('sqlite:///escola.db', echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("\nBanco de dados 'escola.db' e tabelas criados com sucesso!")