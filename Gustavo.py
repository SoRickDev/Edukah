import streamlit as st
import matplotlib.pyplot as plt
import json
import os

# Função para salvar resultados em JSON
def salvar_resultado_json(nome_usuario, acertos, total_questoes):
    resultado = {
        "nome": nome_usuario,
        "acertos": acertos,
        "total_questoes": total_questoes
    }
    os.makedirs("resultados_json", exist_ok=True)
    caminho = f"resultados_json/{nome_usuario.replace(' ', '_')}.json"
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)

# Página da prova com múltiplas perguntas
def pagina_prova():
    st.title('Prova de Python')
    if st.button("⬅ Voltar para os Estudos"):
        st.session_state.page = 'estudos'
        st.rerun()

    # Lista de perguntas e alternativas
    questoes = [
        {"pergunta": "O que é uma string em Python?",
         "opcoes": ["a) Um número inteiro", "b) Um tipo de dados que representa textos", "c) Um tipo de dados usado para cálculos", "d) Um erro no código"],
         "resposta_correta": "b) Um tipo de dados que representa textos"},
        {"pergunta": "Qual princípio da LGPD fala sobre usar só os dados essenciais?",
         "opcoes": ["a) Segurança", "b) Necessidade", "c) Transparência", "d) Finalidade"],
         "resposta_correta": "b) Necessidade"},
        {"pergunta": "Quanto é 2 + 2 * 2 em Python?",
         "opcoes": ["a) 6", "b) 8", "c) 4", "d) 10"],
         "resposta_correta": "a) 6"},
        {"pergunta": "Qual é a média de [2, 4, 6, 8]?",
         "opcoes": ["a) 4", "b) 5", "c) 6", "d) 7"],
         "resposta_correta": "b) 5"}
    ]

    respostas_usuario = []
    for i, questao in enumerate(questoes):
        st.subheader(f"Pergunta {i+1}: {questao['pergunta']}")
        resposta = st.radio("Escolha a alternativa:", questao['opcoes'], key=f"q{i+1}")
        respostas_usuario.append(resposta)

    if st.button("Finalizar Prova"):
        acertos = sum(1 for i, q in enumerate(questoes)
                      if respostas_usuario[i] == q["resposta_correta"])
        st.write(f"Você acertou {acertos} de {len(questoes)} questões!")
        salvar_resultado_json(st.session_state.nome, acertos, len(questoes))

        # Exibe gráfico com acertos e erros
        fig, ax = plt.subplots()
        ax.pie([acertos, len(questoes) - acertos], labels=['Acertos', 'Erros'], autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)