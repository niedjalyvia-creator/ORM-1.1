from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
base = declarative_base()

engine = create_engine('sqlite:///loja_virtual.db', echo=True)
Session = sessionmaker(bind=engine)
base.metadata.create_all(engine)

with engine.connect() as conexao: 
    resultado = conexao.execute(text("SELECT 'Sistema de Loja Virtual Conectado com Sucesso!'") ) 
print(resultado.scalar())