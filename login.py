import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

# Configuração do banco de dados usando SQLite
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Criando a classe Usuario
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    nome = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Função de registro de usuário
def registro_user(email, senha, nome):
    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    novo_user = User(nome=nome, email=email, senha=hashed_password)
    try:
        session.add(novo_user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return False

# Função de verificação de login
def login_user(email, senha):
    user = session.query(User).filter_by(email=email).first()
    if user and bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        return True
    return False

# Interface Streamlit
st.title('Bem-Vindo(A) ao Curso Básico de Python!!')
st.subheader('Selecione Login ou Cadastro')

menu = st.sidebar.selectbox('Escolha uma opção:', ['Login', 'Cadastro'])

if menu == 'Cadastro':
    st.subheader('* Criar nova conta')
    nome = st.text_input('Digite seu nome: ').strip()
    email = st.text_input('Digite um email: ').strip()
    senha = st.text_input('Crie uma senha: ', type='password')
    if st.button('Registrar'):
        if registro_user(email, senha, nome):
            st.success('Seu registro foi concluído com sucesso!!')
            st.title('Bem-Vindo(A)')
        else:
            st.error('Esse email já foi registrado anteriormente!')

elif menu == 'Login':
    st.subheader('* Acessar conta')
    email = st.text_input('Email: ')
    senha = st.text_input('Senha: ', type='password')
    if st.button('Logar'):
        if login_user(email, senha):
            st.success('Login correto!')
            st.title('Bem vindo(A)')
        else:
            st.error('Login incorreto, tente novamente!')

#-------------------------------------- MENU FEITO PELO RAFAEL --------------------------------------#
