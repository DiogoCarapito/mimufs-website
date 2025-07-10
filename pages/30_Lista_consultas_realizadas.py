import streamlit as st

st.title("Lista de consultas realizadas")

st.markdown(
    """É uma lista fundamentais para a elaboração de um curriculo. Na realidade, algumas fontes dão apenas números de consulta como o BI-CSP, outras dão a informação de quem foram os utentes, como o MIM@UF, SIARS e SClinico (spoiler alert, o Sclinico Administrativo é o melhor local para tirar esta informação...)

É habitual as contagens serem ligeiramente diferentes. Para adicionar lenha à fogueira, não da para saber bem quais as discrepâncias porque é dificil comparar os dados entre as diferentes fonte, pois nem sempre têm a mesma estrutura de dados.

Voltando à questão: não basta saber só a lista de untetes que se fez consulta, é necessário saber o **tipo de consulta**/programa associado, **presecial ou não presencial**, se o utente compareceu ou não, de quem foi a **iniciativa** e um número identificador (perferivelmente o Nº de utente, opcionalmente o NOP) para poder cruzar com outras listas relevantes.""",
    unsafe_allow_html=True,
)

st.info(
    """Para isto, só há um sitio que consegue extrair esta informação com este detalhe: o **SClinico Administrativo**."""
)

st.markdown(
    """Isso, nem o MIM@UF dá este detalhe - especificamente o tipo de consulta - porque provalvelmente não está implementado (mas o SIARS e o BI-CSP têm essa informação...). A questão é que a informação do tipo de consulta não é universal para todos os centros de saúde - cada centro de saúde pode dar os nomes que entender aos tipos de consulta. As vezes até há vários nomes para o mesmo tipo de consulta...

Felizmente o SClinico Administrativo têm. **E é muito simples tirar**. Só tem um senão - o ficheiro extraido é um PDF com tabelas e não um ficheiro .xlsx, portanto precisa de ser convertido depois, mas julgo que o próprio Excel faz essa conversão.

Então, peçam a um administrativo da vossa unidade para abrir a sua sessão de Sclinico para os seguintes passos:

1. Ir ao menu de **Listagens**""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/consultas_sclinico_administrativo_1.jpeg",
    caption="Sclinico Administrativo - Listagens",
)

st.markdown("""2. Selecionar a opção **L009 Eventos**""", unsafe_allow_html=True)

st.image(
    "content/images/consultas_sclinico_administrativo_2.jpeg",
    caption="Sclinico Administrativo - Eventos",
)

st.markdown(
    """3. Selecionar a data de inicio e fim, grupo profissional e nome do profissional""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/consultas_sclinico_administrativo_3.jpeg",
    caption="Sclinico Administrativo - Eventos",
)

st.markdown("""4. Clicar no botão **Calcular**""", unsafe_allow_html=True)

st.image(
    "content/images/consultas_sclinico_administrativo_4.jpeg",
    caption="Sclinico Administrativo - Calcular",
)

st.markdown(
    """5. É gerado um PDF com a lista de consultas realizadas com informação detalhada, que pode ser aberto em Excel e convertido para .xlsx""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/consultas_sclinico_administrativo_5.jpeg",
    caption="Sclinico Administrativo - PDF",
)
