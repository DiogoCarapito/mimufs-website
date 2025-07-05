import streamlit as st

st.header("Preâmbulo - Tecnicas de extração de dados", anchor=False)

st.markdown(
    """O processo de extrair dados do **MIM@UF** pode ser dividido em vários passos.

1. Primeiro temos de escolher o relatório ou listagem que se adapta mais a pergunta que queremos responder. Se não conhecemos o **MIM@UF**, os títulos e descrições dos relatórios são uma ajuda

2. Escolher o relatório que queremos, aparecenos uma interface para fazer o pedido de dados à base de dados. Este processo chama-se uma Query ou Prompt

3. Depois da Query, é produzida uma tabela. nesta fase temos a hipotese de aplicar modificações à tabela de acodrdo com a nossa necessidades: retirar ou selecionar filtros, adicionar ou remover colunas, fazer algum tipo de limpeza dos dados.

4. Contentes com a tabela, vamos menu de exportação, em que podemos selecionar formato do ficherio, de forma a ser lido nos programas de processamento (Excel, python...)

5. No fim, abrimos o ficheiro num prgrama para fazer o processamento final. É neste passo que fazemos a transformação destes dados em tabelas ou graficos úteis para responder à nossa pergunta inicial.

Todas estas etapas têm truques e especificidades que, quando bem utilizados, permitem que sejamos mais rápidos nas extrações ou a aceder a mais dados que à primeira vista não aparecem.

Aqui vamos falar das particularidades do passo 2 --- **a Query**."""
)
st.title("Query", anchor=False)

st.markdown(
    """A Query é é o menu que permite fazer instrução para o pedido de dados inicial ao **MIM@UF**.

![Exemplo do Menu de Query do relatório P...]()

Fazemos a seleção nas caixas da esquerda para a direita e o botão para executar a query encontra-se no cano inferior esquerdo. Se faltar agluma coisa ao executar a query, o **MIM@UF** dá erro e diz o que falta.

Vou mostrar os diferentes tipos de menus possiveis"""
)

st.header("Unidade Funcional", anchor=False)

st.markdown(
    """![Menu de escolha de Unidade Funcional (P...)]()

Começamos pela a unidade Fucnional.
Este é fácil, é so escolher a nossa unidade. Nem sempre aparece mas quando aparece é so passar para o lado esquerdo e está feito."""
)

st.header("Escolha temporal", anchor=False)

st.markdown(
    """Uma que invariavelmente aparece sempre é uma opção de escolha temporal, que pode ser:

- data (habitualmente através das escolha de um mês)
- periodo de tempo (que pode ter uma sleeção simples de um ano, semestre, trimestre, um mês, ou então composta, como com vários meses que não precisam de ser consecutivos. é particularmente util

Para que serve a data e o periodo de tempo?"""
)

st.info(
    """A data quando o relatório proprciona "fotografia" de um momento específico, Habitualmente são dados que mudam apenas mensalmente, que ser por exemplo para ver a lista de untentes inscritos ou resultados de indicadores. Outro exemplo em que visão "fotografia" se aplica são resutlados de MCDTs ou biometrias, onde o **MIM@UF** nos dá o valor mais recente registado à data da "fotografia"."""
)
st.info(
    """O periodo temporal faz sentido quando a infomração que procuramos acontece com registos com elevada frequência, como por exemplo consultas ou prescições de MCDTs e medicamentos, que acontencem dezenas a centenas de vezes por dia. então ai escolhemos uma janela de tempo no qual queremos analisar."""
)
st.markdown(
    """Habitualmente o **MIM@UF** apresenta-nos uma interface adequada ao tipo de referencia temporal que o relatório permite, mas nem sempre está correto

Por exemplo, logo no primeiro relatório de todos, no **P01.R01. Inscritos > Sexo e Grupo Etário** a interface que nos aparece é de um periodo temporal. 

![Query do P01.R01. Inscritos > Sexo e Grupo Etário]()

Imaginemos que o nosso centro de saude cerca de 10.000 utentes inscritos selecionarmos ano no periodo temporal, o **MIM@UF** vai nos dar o somatório de todos os meses, ou seja, cerca de 120.000 utentes inscritos. Isto não faz muito sentido. Se colocarmos só um mês já dá valores corretos. Assim, apesar do menu deste relatório menu permita selecionar periodos temporais, num contexto de contagem de inscrios o que faz sentido é uma data pleo que devemos optar por um mês

O contrário também pode acontecer, o relatório só deixar escolher um mês de cada vez, e se temos o azar de querermos um periodo de 1 ano, temos de repetir a extração do relatório 12 vezes, um para cada mês...

Um exempo o relatório **P04.R07. Novos Problemas > Sexo e Grupo Etário**. se queremos tirar os Novos probelmas diagnosticado ao longo do ano, temos de tirar 1 mês de cada vez...

![Query do P04.R07. Novos Problemas > Sexo e Grupo Etário]()

Ha ainda outra variante: há relatórios em que, podendo extrair 1 ano duma só vez, não é boa ideia. Isto acontence quando a quantidade de dados de 1 ano é tão grande que, ou o **MIM@UF** demora uma eternidade a executar o query, ou o query é executado mas depois não dá para exportar por ser tão grande.

Isto acontece, por exemplo, se tentarmos obter as nas listagens de medicamentos prescritos de todos os médicos durante um ano (**P06.01.01.L03. Listagem de Medicamentos Prescritos por Utente - Marca e DCI**), em que facilmente pode resultar numa tabela com 100.000 linhas.

![Query do P06.01.01.L03. Listagem de Medicamentos Prescritos por Utente - Marca e DCI]()

A solução é partir o elefante às fatias. Experimenta-se com 1 ano, se não funcionar então faz-se em semestres ou trimestres, e junta-se à posteriori."""
)

st.header("Ano contratual", anchor=False)

st.markdown(
    """Agora vamos aos indicadores, onde é costume pedir o ano contratual
Este também é muito simples.
Basta selecionar o ano refernte aos indicadores que queremos analisar. Por definição nunca vem com o ano correto, portanto é preciso mudar sempre.
Está feito!

![Query do P02. ...]()"""
)

st.header("Indicadores e Grupo de indicadores", anchor=False)

st.markdown(
    """Ainda nos indicadores, se executarmos a query é costume apraecer um segundo menu com seleção e indicadores ou grupo de indicadores.

![Query do P02. ...]()

Existe uma barra de pesquisa permite encontar os indicadores pelo ID ou pelo nome.

Habitualmente estão diponiveis mais de 200 indicadores e podem ser selecionados até 10 ao mesmo tempo, que nos pode poupar tempo quando queremos fazer uma analise mais abrangente dos indicadores

Cuidado a escolher entre FX e FL - respetivamente, fixo e flutuante. E alguns dos indicadores apenas têm uma das versões disponíveis.

Com escolhemos entre flutuante e fixo? Depende do tipo de analise que queremos fazer com os indicadores"""
)

st.info(
    """O flutuante serve para ver estado atual do cumprimento, ou seja, permite perceber se as as estratégias implementadas estão estão ou não a ter resultados."""
)
st.info(
    """O fixo permite projetar qual será o cumprimento do indicador no final do ano. É útil para descobrir utentes que serão futuros não cumpridores se nada acontecer."""
)
st.markdown(
    """Vamos usar o exemplo do indicador 37 - **Proporção de utentes com diabetes com consulta de enfermagem no último ano**

Assumindo que estamos em Maio, os cumpridores deste indicador pelo Flutuante tiveram pelo menos uma consutla de vigialncia de diabetes de enferamgem nos ultimos 12 meses: portanto, entre maio deste ano e junho do ano anterior.

Se virmos o fixo do mesmo indicador, só serão cumpridores quem teve a mesma consulta de vigilancia a partir de 1 de janeiro deste ano.

Ou seja, se um utente for cumpridor no flutuante e incumpridor no fixo, pode significar que habitualmente ele costuma ser cumpridor (o ano passado foi) mas ainda não teve a consulta este ano (pode já estar marcada ou não, mas isso não sabemos pelo indicador...)

Naturalmente, se tirarmos este indiacador fixo em janeiro, o quase todos os utentes serão não cumpridores, porque a maior parte ainda não teve oportunidade de ter consulta.

Por outro lado tirando em em dezembro, o fixo e o flutuante devem ser exatamente iguais.

No fim, o flutuante e o fixo complementa-se: o primeiro mostra o estado actual, o segundo é util para planeamento

Nota: não esquecer que o resultado dos indiadores no **MIM@UF** costumam ter 1 a 2 meses de atraso)

Boa, voltamos ao **MIM@UF**. Outro menu referetes a indicadores é o grupo de indicadores. este caso é relativamente simples, porque por definição estão todos selecionados. Raramente é necessário mudar, portanto é avançar sem fazer nada."""
)

st.header("ICPCs", anchor=False)

st.markdown(
    """Vamos à escolha de ICPCs

Apesar da interface parecer realtivamente linear, não é muito prático escolher para encontrar o que queremos rapidamente, especialmente porque a ferramenta de pesquisa não fuinciona aqui e a solução aparente é andar a navegar numa lista de 1500 diagnósticos diferentes com setinhas.

Vou explicar como fazer isto muito mais rápido:

A minha dica é iniclamente escolher o primeiro código que nos aparecer dentro da pasta dos ICPC, pode ser  o -1:NE ou A:GERAL E INESPECIFICO ou A01:DOR GENERALIZADA / MÚLTIPLA e selecionar para a caixa da direita, não interessa qual

Depois, na caixa da direita, clicamos no codigo selecionado, que faz aparecer uma janela onde agora sim, já temos um campo de pesquisa por nome ou código ICPC

Removemos o codigo inciial e passamos para o campo direito o código que queremos, por exemplo o K86

Nesta janela até podemos adicionar mais do que um código ao mesmo tempo. Mas resultado vai depender especificamente o relatório em questão, pois nalguns relatórios podemos distinguir os codigos, noutros relatórios ele junta sem dizer quem é quem. Falarei destas especificidades no episódio sobre o Módulos de Probelemas e Doenças. Aqui o meu objetivo é apenas mostrar como utilizar corretamente esta parte da escolha dos ICPCS na Query.

os relatórios que permitem ver cormobilidadestêm têm 2 sitios diferentes para ICPCs, ICPC1 e ICPC2. Funcionam ambos da mesma forma, podemos colocar um ou vários. códigos ao mesmo tempo"""
)

st.header("MCDTS e área de MCDT", anchor=False)

st.markdown(
    """Para os relatórios referentes a Prescrição ou resultados de MCDTs, habitualmente é necessário escolher a àrea de MCDT ou o MCDT espeficico na Query.

Por exemplo, quando queremos resultados de Colesterol total temos de econtrar codigo certo nesta interface se pesquisar por colesterol (tenho de retirar este tick de maiusculas e minusculas), vemos que há vários tipos de colesterol repetidos...

Aqui temos que ir por tentativa e erro, pois depende  do codigo de prescrição e da forma exame ficou registado no SCLINICO, que pode variar entre centros de saúde e entre laboratórios.
Para agravar as coisas, só podemos selecionar um de cada vez.

Aqui também podemos tirar o LDL, mas queria deixar uma nota: dependedo outra vez dos hábitos de prescrição e registo de cada centro de saúde e laboratório, pode ser necessário tirar também o Colesterol total, HDL e Triglicéridos. Isto porque há laboratórios que calculam o LDL a partir do perfil e migra para o SCLINICO, outros não, e se calcularmos nós à posteriori o LDL a partir do perfil lipido com a formula de Friedewald, garantido que valores são referentes à mesma data de registo, aumentamos a rede e apanhamos mais LDLs.

Quando falamos de listagens de prescrição de MCDTs, a forma de escolher é por àrea de MCDT. neste caso, se queremos as prescrições de MCDTs por utente de todas as areas temos de fazer 1 a 1. Mas se apenas precisamos saber contagens, o relatórios já nãpo têm essa limitação."""
)

st.header("Biometrias", anchor=False)

st.markdown(
    """As biometrias funcionam  de forma muito parecida aos MCDTs.
Uma novidade recente é que também já dá para tirar o indice de BARTEL que tenha sido registado no SCLINICO. e o DM deste e o registo a data de diagnóstico de DM, que é muito util para caracterização de diabeticos no curriculo ou para o calculo de SCORE 2 dad diabetes. Ainda assim Este menu permite apenas 1 seleção de cada vez."""
)

st.header("Menus especiais", anchor=False)

st.markdown(
    """Existe ainda menus especifícos que permitem adicionam filtros ou seleção de metricas ainda na query, mas não têm grande utilidade. Ainda assim, é necessário fazer uma seleção para poder avançar com a query"""
)

st.subheader("Filtros", anchor=False)

st.markdown(
    """Um exemplo de filtro é na listagem P01.01.L01 de inscritos onde paraece uma seleção de intervalo de idades.

Por definição o **MIM@UF** seleciona este filtro mas na realidade vai introduzir limitações indesejadas, pelo que sugiro sempre alterar para -nenhum-

![P01.01.L01]()"""
)

st.subheader("Métricas", anchor=False)

st.markdown(
    """
Outro exemplo é nos TOP de faturação de MCDTs (**P07.02.R03. TOP MCDTs Aceites > Médico**) ou Medicamentos (**P06.02.R03. TOP Medicamentos Aceites > Médico**), onde aparece um menu para escolher qual metrica utilizar para ordenar o TOP. No fim vamos ter acesso a todas as metricas, portanto não é dramático esta seleção.

![P07.02.R03. TOP MCDTs Aceites > Médico]()

Nas Biometrias (**P10.01.L01. Resultados Biométricos > Utente**) também existe uma seleção do tipo de resultado com possibilidade de adicionar filtros. Costumo não selecionar, uma vez que prefiro obter os dados todos e filtrar depois do que aplicar um limite à partida.

![P10.01.L01. Resultados Biométricos > Utente]()"""
)

st.divider()

st.markdown(
    '<div style="text-align: center;">'
    '<p style="font-size: 16px;">Dúvidas, sugestões? Envia-nos um email para <a href="mailto:mgfhub.suporte@gmail.com" style="text-decoration: underline; font-size: 16px;">mgfhub.suporte@gmail.com</a></p>'
    "</div>",
    unsafe_allow_html=True,
)
