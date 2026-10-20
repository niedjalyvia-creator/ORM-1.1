from sqlalchemy import create_engine
from modelos_loja import Base, Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("\nBanco de dados 'loja_virtual.db' e tabelas criados com sucesso!")