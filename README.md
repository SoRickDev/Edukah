# Edukah
PIM - Curso Básico de Python para Iniciantes

# Curso Básico de Python com Streamlit

Projeto educacional desenvolvido para oferecer uma experiência completa de aprendizado básico em Python, com autenticação de usuários, conteúdo interativo e avaliação final. O progama foi desenvolvido por uma equipe colaborativa, dividindo responsabilidades para manter organização, escalabilidade e qualidade.

---

## Visão Geral

Este sistema é uma aplicação web feita em **Python** utilizando o framework **Streamlit**, ideal para quem deseja aprender Python de forma prática, segura e gamificada. O projeto conta com:

- Sistema de login e cadastro com senhas criptografadas (SQLite + SQLAlchemy + bcrypt).
- Conteúdo didático interativo (conceitos, exercícios e mini-códigos para praticar).
- Prova final com avaliação e visualização dos resultados em gráficos.
- Salvamento dos resultados de prova em arquivos JSON para futuras análises.

---

## Estrutura do Projeto

| Arquivo              | Responsável  | Função principal                                             |
|----------------------|--------------|--------------------------------------------------------------|
| `main.py`            | Rick         | Ponto de entrada, executa a interface principal              |
| `Rick_interface.py`  | Rick         | Controla a navegação entre páginas: login, estudos e prova   |
| `Rafa_login.py`      | Rafa         | Gerencia banco de dados SQLite, cadastro e autenticação      |
| `Gabriel_conteudo.py`| Gabriel      | Página de estudos com aulas, exercícios e execução de código |
| `Pedromelo_provinha.py`| Pedro Melo | Página da prova, coleta respostas e exibe resultados gráficos|
| `PIM-1ºS-Documentação`| Letícia | responsável pela Documentação completa do programa|

---

## Tecnologias Utilizadas

- Python 3.x
- Streamlit (Interface Web)
- SQLAlchemy (ORM para SQLite)
- bcrypt (hash de senhas)
- matplotlib (gráficos na prova)
- JSON (armazenamento de resultados)

---

## Como Executar

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd nome-do-repositorio
