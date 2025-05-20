import streamlit as st
import io
import contextlib

# Função para interpretar mensagens de erro
def interpretar_erro(e):
    if isinstance(e, SyntaxError):
        return "Erro de sintaxe. Verifique parênteses ou aspas."
    elif isinstance(e, NameError):
        return "Variável ou função não definida."
    elif isinstance(e, ZeroDivisionError):
        return "Divisão por zero."
    elif isinstance(e, TypeError):
        return "Erro de tipo."
    else:
        return f"Erro desconhecido: {str(e)}"

# Página de estudos com conteúdos básicos
def pagina_estudos(nome):
    st.title(f'Bem-vindo(a), {nome} à sua Jornada Python!')
    st.header('📘 Introdução ao Python')

    # LGPD - noções iniciais sobre proteção de dados
    with st.expander("Noções Básicas da LGPD"):
        st.markdown("""
        A **LGPD** regula dados pessoais no Brasil. Empresas devem proteger esses dados.

        - Dado pessoal: identifica a pessoa
        - Princípios: finalidade, necessidade, segurança
        - Direitos: acessar, corrigir, excluir, revogar
        """)

    # Aula sobre strings e métodos básicos
    with st.expander("1. Strings"):
        st.markdown("""
        ```python
        nome = "João"
        print(nome.upper())
        ```
        """)
        entrada = st.text_input("Digite uma palavra:")
        if entrada:
            st.write(f"Maiúsculas: {entrada.upper()}")
            st.write(f"Minúsculas: {entrada.lower()}")
            st.write(f"Número de caracteres: {len(entrada)}")

    # Aula de operadores matemáticos
    with st.expander("2. Operadores Aritméticos"):
        num1 = st.number_input("Número 1", value=0)
        num2 = st.number_input("Número 2", value=0)
        st.write(f"Soma: {num1 + num2}")
        st.write(f"Subtração: {num1 - num2}")
        st.write(f"Multiplicação: {num1 * num2}")
        if num2 != 0:
            st.write(f"Divisão: {num1 / num2}")
        else:
            st.write("Divisão por zero não é permitida.")

    # Execução de código com print()
    with st.expander("3. Pratique com print()"):
        user_code = st.text_area("Digite seu código aqui:")
        if st.button("Executar código"):
            if "print" in user_code:
                try:
                    user_code = user_code.strip()
                    if user_code.count('"') % 2 != 0 or user_code.count("'") % 2 != 0:
                        st.error("Aspas não fechadas.")
                    elif user_code.count('(') != user_code.count(')'):
                        st.error("Parênteses não fechados.")
                    else:
                        f = io.StringIO()
                        with contextlib.redirect_stdout(f):
                            exec(user_code, {"__builtins__": {"print": print}})
                        output = f.getvalue()
                        st.code(output)
                except Exception as e:
                    st.error(f"Erro: {e}")
                    st.info(interpretar_erro(e))
            else:
                st.warning("Use print().")

    # Mini calculadora com código livre
    with st.expander("4. Calculadora com código"):
        conta = st.text_area("Digite sua conta Python aqui:", key="conta")
        if st.button("Calcular"):
            if "print" in conta:
                try:
                    f = io.StringIO()
                    with contextlib.redirect_stdout(f):
                        exec(conta, {"__builtins__": {"print": print}})
                    output = f.getvalue()
                    st.code(output)
                except Exception as e:
                    st.error(f"Erro: {e}")
                    st.info(interpretar_erro(e))
            else:
                st.warning("Use print().")

    # Conceitos básicos de matemática
    with st.expander("5. Matemática Básica"):
        st.markdown("""
        Operações básicas:

        - Soma: `+`
        - Subtração: `-`
        - Multiplicação: `*`
        - Divisão: `/`
        - Potência: `**`
        """)

    # Noções iniciais de estatística
    with st.expander("6. Estatística Básica"):
        st.markdown("""
        - Média: soma dos valores / quantidade
        - Moda: valor que mais se repete
        - Mediana: valor central da lista
        """)

    # Navegação entre páginas
    if st.button("Ir para a Prova"):
        st.session_state.page = 'prova'
        st.rerun()
    elif st.button("Sair"):
        st.session_state.page = 'login'
        st.rerun()
