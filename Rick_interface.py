import streamlit as st
from Rafa_login import registro_user, login_user
from Gabriel_conteudo import pagina_estudos
from Pedromelo_provinha import pagina_prova

# Controlador principal das páginas do app
# Lida com login, cadastro, estudos e prova

def run_interface():
    if 'page' not in st.session_state:
        st.session_state.page = 'login'

    # Página de login/cadastro
    if st.session_state.page == 'login':
        st.title('Bem-Vindo(A) ao Curso Básico de Python!')
        st.subheader('Selecione Login ou Cadastro')

        menu = st.sidebar.selectbox('Escolha uma opção:', ['Login', 'Cadastro'])

        if menu == 'Cadastro':
            # Formulário de cadastro de novo usuário
            st.subheader('* Criar nova conta')
            nome = st.text_input('Nome: ').strip()
            email = st.text_input('Email: ').strip()
            senha = st.text_input('Senha: ', type='password')
            if st.button('Registrar'):
                if not nome or not email or not senha:
                    st.error("Todos os campos são obrigatórios.")
                elif registro_user(email, senha, nome):
                    st.success('Registrado com sucesso!')
                else:
                    st.error('Esse email já está cadastrado.')

        elif menu == 'Login':
            # Formulário de login do usuário existente
            st.subheader('* Acessar conta')
            email = st.text_input('Email:', key="login_email")
            senha = st.text_input('Senha:', type='password', key="login_senha")

            if st.button("Logar"):
                nome = login_user(email, senha)
                if nome:
                    st.session_state.page = 'estudos'  # Redireciona para estudos após login
                    st.session_state.nome = nome
                    st.rerun()
                else:
                    st.error('Email ou senha incorretos.')

    # Página de conteúdo
    elif st.session_state.page == 'estudos':
        pagina_estudos(st.session_state.nome)

    # Página da prova
    elif st.session_state.page == 'prova':
        pagina_prova()
