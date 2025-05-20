from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import bcrypt

# Conexão com banco SQLite — por Rafa
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Definição da tabela de usuários
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    nome = Column(String, nullable=False)

# Criação da tabela no banco de dados
Base.metadata.create_all(engine)

# Função para cadastrar novo usuário
# Criptografa a senha e salva no banco
def registro_user(email, senha, nome):
    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    novo_user = User(nome=nome, email=email, senha=hashed_password)
    try:
        session.add(novo_user)
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False

# Função para autenticar usuário existente
# Verifica email e senha criptografada
def login_user(email, senha):
    user = session.query(User).filter_by(email=email).first()
    if user and bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        return user.nome
    return None
