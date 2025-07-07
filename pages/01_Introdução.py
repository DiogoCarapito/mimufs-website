import streamlit as st

st.title("O que é o MIM@UF?")

st.markdown(
    """O **MIM@UF** é uma plataforma de extração de dados desenvolvida para apoiar o trabalho nas unidades funcionais dos cuidados de saúde primários. Permite aceder a muitos dos dados gerados no dia-a-dia da unidade — de forma organizada, acessível e com um nível de detalhe que chega até ao utente.

O **MIM@UF** é particularmente útil para:

- **Projetos de investigação**
- **Auditorias**
- **Trabalhos de governação clínica**,
- **Currículo para internato e grau de consultor**
- **Estudo de lista**

Em vez de andar a fazer registos manuais, o **MIM@UF** oferece uma solução sistematizada, fiável e reprodutível, à escala da unidade."""
)

st.subheader("De onde vêm os dados?")

st.markdown(
    """Os dados vêm de várias fontes, como o **SClínico**, a **PEM**, e plataformas de indicadores e vacinação. A atualização depende do tipo de dado: pode variar entre 1-2 meses até estar disponível quase em tempo real.

O acesso é feito através da **intranet** do centro de saúde ou da ULS. Existem diferentes **perfis de utilizador** — Médico, Enfermeiro e Interno — e o conteúdo disponível varia ligeiramente conforme o perfil. Neste tutorial, vamos explorar a plataforma com o perfil **Médico**.

Apesar de a plataforma já estar em funcionamento há vários anos, os relatórios continuam a poder sofrer atualizações. Por isso, este tutorial refere-se especificamente à versão em uso em 2025."""
)

st.subheader("Começar com perguntas")

st.markdown(
    """A melhor forma de usar o **MIM@UF** é pensar em perguntas especificas. Alguns exemplos simples de perguntas que podem ser respondidas com o MIM@UF:

- Quantos agregados familiares tenho na minha lista? E quantos membros por agregado?
- Quais as nacionalidades, profissões e habilitações das pessoas inscritas?
- Quais os resultados dos indicadores por equipa?
- Quem não está a cumprir determinados indicadores?
- Quem teve consulta no último trimestre e que tipo de consulta foi?
- Quantas consultas fiz no 1.º semestre deste ano?
- Qual é o “TOP” de diagnósticos na minha lista de problemas?
- Quantos novos diagnósticos fiz no último trimestre?
- Quem tem diagnóstico de HTA?
- Que comorbilidades têm os utentes com HTA?
- Que medicamentos tenho prescrito?
- Qual o valor mais recente da TA ou da HbA1c de cada utente?

Se quisermos ir mais longe, é possivel fazer analises mais complexas como, que necessitam de extração de várias tabelas e cruzamento:

- Fazer uma lista completa de problemas por utente da unidade toda ou dos utentes que consultei
- Calcular a taxa de filtração glomerular dos utentes todos
- Calcular o **SCORE2** para toda a unidade
- Realizar auditorias de indicadores e isolar diferentes tipos de não cumpridores
- Analisar de número de pedidos receituários por utente
- Analisar custos de MCDTs e/ou Medicamentos"""
)

st.subheader("Conclusão")

st.markdown(
    """O verdadeiro poder do **MIM@UF** está na capacidade de transformar perguntas em conhecimento. É esse processo que nos ajuda a entender a prática clínica de forma mais profunda e a promover melhorias sustentadas e informadas."""
)
