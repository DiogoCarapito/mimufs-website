import streamlit as st

st.title("Refinamento")

st.markdown(
    """Depois da Query, o MIM@UF apresenta-nos o resultado sob a forma de uma tabela, com opções para a podemos modificar. É nesta fase que podemos refinar os dados, filtrando, ordenando e transformando a tabela de acordo com as nossas necessidades.""",
    unsafe_allow_html=True,
)

st.info(
    """É aqui que residem as maiores potencialidades do MIM@UF que desbloqueiam várias funções de manipulação de dados, mas que não são imediatamente aparentes à primeira vista."""
)

st.markdown(
    """Imaginemos que queremos a minha lista de utentes inscritos para isso podemos utilizar o relatório **P01.01.L01 Inscritos**""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/refinamento_P01_01_L01.jpg",
    caption="Depois de executar a query da listagem P01.01.L01 (a cinzentoa zona da tabela)",
)

st.markdown(
    """Ao executar a query obtemos uma tabela em que cada linha é um utentes e várias colunas com dados de cada utente como o sexo e a idade.

---""",
    unsafe_allow_html=True,
)

st.header("Barra do topo")

st.markdown(
    """Nesta secção o superior com 4 menus, sendo que se clicarmos em cada um a barra por baixo vai-nos mostrar opções diferentes: Home, Ferramentas, Dados e Planilha.

Os botões mais importantes são do menu **Home** são:

- **Exportar**: permite exportar a tabela
- **Novo Prompt**: permite voltar atrás à query mas ainda com as escolhas da query ainda preenchidas, útil para fazer uma nova query com pequenas alterações (tipicamente mudar o mês, MCDTs ou ICPCs), em vez de voltar a fazer tudo de novo.""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_P01_01_L01_home.jpg", caption="Menu Home")

st.markdown(
    """No menu **Planilha**:

- **Mesclar cabeçalhos de colunas** e **Mesclar cabeçalhos de linhas**: permitem unir ou separar células que estão unidas, o que é útil para quando existem celulas unidas, permitindo evitar formatação desnecessária e tornar a tabela mais facil de trabalhar em processamento.""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_P01_01_L01_planilha.jpg", caption="Menu Planilha")

st.markdown("""---""", unsafe_allow_html=True)

st.header("Detalhes do Prompt")

st.markdown(
    """Metadados da query. Informação que pode estar presente no ficherio final se na exportação escolhermos incluirmos os metadados. É uma informação que pode ser útil para percebermos o que é que estamos a ver, e que nos pode ajudar a identificar o relatório.""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/refinamento_P01_01_L01_detalhes_prompt.jpg",
    caption="Detalhes do Prompt",
)

st.markdown("""---""", unsafe_allow_html=True)

st.header("Barra dos filtros")

st.markdown(
    """Por baixo temos o PAGINAR POR, que na realidade são filtros.""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/refinamento_P01_01_L01_paginar_por.jpg", caption="Barra dos filtros"
)

st.markdown(
    """Estes são particularmente interessantes porque permitem manipular os dados de acordo com a nossa necessidade, especilamente porque o filtro escolhido por definição pode não ser o que queremos. Neste caso temos aqui vários filtros que temos de mudar no caso de queresmos a lista completa dos utentes da unidade toda.

Antes de começar a mudar filtros, gostava de mostrar alguns truques.

Uma forma de entender rapidamente de saber se os dados que temos estão adequados ou não é por esta secção à direita, entre os filtros e a tabela, onde diz quantas linhas tem a tabela.""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/refinamento_P01_01_L01_paginar_por_linhas_dados.jpg",
    caption="Contagem de linhas",
)

st.markdown(
    """Neste caso temos 64 linhas, sendo que uma linha corresponde a um utente. Significa de certeza não temos a listagem toda.

Outra forma de verificar é olharmos para a tabela e para os dados: na secção da idade vemos que temos apenas 0 a 4 anos e apenas tem os frequentadores, ou seja, não temos a lista completa de utentes.""",
    unsafe_allow_html=True,
)

st.image(
    "content/images/refinamento_P01_01_L01_paginar_por_freq_grupo_etario.jpg",
    caption="Idade e Frequentadores",
)

st.markdown(
    """Com estas duas pistas, podemos verificar que os dados não estão completos pelo menos relacionado com com estres filtros. Se alterarmos estes dois filtros para *TODOS* já ficamos com uma tabela com a lista completa de utentes para o Médico de Família selecionado.

---""",
    unsafe_allow_html=True,
)

st.header("Filtro -> coluna")

st.markdown(
    """Agora imaginemos que queriamos a lista da Unidade toda. sem saber mais nada, significaria que tinhamos de tirar 10 vezes esta lista no caso do nosso centro de saude ter 10 medicos e depois juntar tudo no fim?

Era uma hipotese, mas há uma forma melhor: que é juntar todos os médicos na mesma tabela. Este é um dos truques mais poderosos que o MIM@UF permite, e que abre um mar de possibilidades.

Basicamente vamos transformar um dos filtros, neste caso Médico Familia, numa coluna:""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_filtro_coluna_1.png", caption="Filtro para coluna")

st.markdown(
    """1. Movemos o rato entre o nome de duas colunas e aparece esta linha vertical amarela e uma lupa.""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_filtro_coluna_2.png", caption="Filtro para coluna")

st.markdown("""2. Clicamos na Lupa""", unsafe_allow_html=True)

st.image("content/images/refinamento_filtro_coluna_3.png", caption="Filtro para coluna")

st.markdown(
    """3. Aparece outra Lupa, clicamos nessa lupa e procuramos o nome do filtro que queremos tranformar para coluna - neste caso escrevemos *Méd*""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_filtro_coluna_4.png", caption="Filtro para coluna")

st.markdown("""4. Clicamos em Médico Familia""", unsafe_allow_html=True)

st.image("content/images/refinamento_filtro_coluna_5.png", caption="Filtro para coluna")

st.markdown(
    """E vejam, o filtro desapareceu e reapareceu em coluna. Não só temos a lista de utentes do centro de saude inteiro como temos o nome do Médico de Família para cada utente!""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_filtro_coluna_6.png", caption="Filtro para coluna")

st.markdown(
    """Podemos fazer o mesmo com qualquer filtro, temos de ter cuidado em escrever e exatamente o nome do filtro""",
    unsafe_allow_html=True,
)

st.header("Coluna -> filtro")

st.markdown(
    """O inverso também é possivel: podemos passar uma coluna para filtro. Basta escrever o nome da coluna no campo de pesquisa da barra de filtros e clicar.""",
    unsafe_allow_html=True,
)

st.image("content/images/refinamento_coluna_filtro.png", caption="Coluna para filtro")

st.markdown("""---""", unsafe_allow_html=True)

st.header("Tabelas de dupla entrada")

st.markdown(
    """A localização onde colocamos o rato para fazer a transformação de filtro para coluna também é importante, pois se colocarmos o rato depois da coluna **Métrica** (só funciona nas tabelas que têm uma coluna Métrica), em vez de criarmos uma nova coluna simples, criamos uma tabela de dupla entrada, que é uma tabela onde temos duas colunas de filtros, e cada célula é o resultado da combinação dos dois filtros. pode ser particularmente útil para ver a distribuição de dados entre duas variáveis.

![Tabela de dupla entrada]()""",
    unsafe_allow_html=True,
)
