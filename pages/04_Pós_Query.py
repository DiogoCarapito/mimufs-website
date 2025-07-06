import streamlit as st

st.title("Pós-Query")

st.markdown(
    """Depois da query o MIM@UF apresenta-nos o resultado sob a forma de uma tabela. Neste interface temos várias opções para explorar.

> É aqui que residem as maiores potencialidades do MIM@UF que a maior parte das pessoas não sabe, uma vez que não são nada obvias à primeira vista.

Imaginemos que queremos a minha lista de utentes inscritos para isso podemos utilizar o relatório **P01.01.L01 Inscritos**

Vamos executar um query, pode ser nesta data
Aqui nesta parte do query vamos escolher -nenhum-, para evitar algumas limitações chatas e Executamos o relatório

Aqui já começamos a ter resultados, com uma tabela em que cada linha é um utentes e várias colunas com dados de cada utente como o sexo e a idade.

Mas antes ir para os dados vou apresentar como é que esta pagina está organizada:

Nesta secção o superoior com 4 menus, sendo que se clicarmos em cada um a barra por baixo vai-nos mostrar opções diferentes
Os mais importantes são o botão Exportar no menu HOME, Novo Prompt no menu dados (particularmente util quando queremos tirar vários relatórios seguidos que precisam de pequenas alterações no prompt) ou no Menu Planilha os botões Mesclar colunas e linhas

Depois temos os detalhes do Promp, onde tem a metainformaçao relativas ao Query -  na exportação da tabela temos a opção de incluir ou não esta informação.

Por baixo temos o PAGINAR POR, que na realidade são mias do que filtros. Estes são particularmente interessantes porque permitem manipular os dados de acordo com a nossa necessidade, especilamente porque o filtro escolhido por definição pode não ser o que queremos. Neste caso temos aqui vários filtros que temos de mudar no caso de queresmos a lista completa dos utentes da unidade toda.

Antes de começar a mudar filtros, gostava de mostrar alguns truques

Uma forma de entender rapidamente de saber se os dados que temos estão adequados ou não é por esta secção à direita, entre os filtros e a tabela, onde duz quantas linhas tem a tabela. neste caso temos 64 linhas, sendo que uma linha corresponde a um utente. significa de certeza não temos a listagem toda.

Outra forma de verificar é olharmos apra a tabela e para os dados: na secção da idade vemos que temos apenas 0 a 4 anos, e se ordenarmos vemos que não aparecem idades superiores a 4.

Com estas duas pistas, no minimo os dados não estão completos pelo menos relacionado com quaquer coisa com a idade.

então vamos Explorar a barra dos filtrod

M~es parece bem, so temos uma opção na realidade.
O mesmo com a unidade funcuinal e Flag Medico Família só temos uma hipotese, nada para mudar

No Médico Familia aqui sim, podemos mudar para o Médico que queremos.

Frequentador também podemos mudar para total em vez de incluir apenas os Frequentadores
E o ultimo filtro é o grupo etário: é este que esta a limiar as coisas. está sleecionado por 0-4 anos confere, aqui nas idades so tinhasmos 0-4 anos
Mudamos para Todos e ja vemos que o numero de linhas, ou seja numero de untentes que faça sentido

Boa.

Esta é a lista de utentes inscritos para este medico de familia no mês que selecionamos. Já podiamos exportar"""
)

st.subheader("Filtro -> coluna")

st.markdown(
    """Agora imaginemos que queriamos a lista da UNIDADE TODA
Singifica que tinjamos de tirar 10 vezes esta lista no caso do nosso centro de saude ter 10 medicos?

Era uma hipotese, mas há uma forma desejável, que é juntar tudo na mesma tabela. Este é um dos truques mais poderosos que o MIM@UF permite, e que abre um mar de possibilidades.

Basicamente vamos transformar um dos filtros, neste caso Médico Familia, numa coluna

Se formos com o rato entre o nome de duas colunas, aparece esta linha vertical amarela e uma lupa.

Clicamos na Lupa

Aparece outra Lupa, clicamos nessa lupa e procuramos o nome do filtro que queremos tranformar para coluna:  Méd..

Aqui está, Médico Familia. e clicamnos
E vejam, o filtro desapareceu e reapareceu em coluna
Não só temos a lista de utentes do centro de saude inteiro como temos o nome do Médico de Família para cada utente!

Podemos fazer o mesmo com qualquer filtro, temos de ter cuidado em escrever e exatamente o nome do filtro

O inverso também é possivel: podemos passar uma coluna para filtro
Basta escrever o nome da coluna aqui neste campo de pesuisa da barra de filtros e clicar

Neste caso a frequesia de habitação. Neste caso o novo filtro de freguesia de habitação bão tem uma opçao de todos, portanto podemos voltar a trás."""
)

st.subheader("Tabelas de dupla entrada")

st.markdown(
    """Vamos para outro relatório para demonstrar quão interessante podem ser estes 2 movimentos, em que podemos transformar a tabela por completo
Vamos para A listagem P03.01.L01 Consultas > Utente"""
)

st.subheader("Novo prompt")

st.markdown(
    """Imaginem que queriamos exatamente esta estrutura de tabela mas em vez do mes de maio, queriamos tirar do inicio do ano. podiamos clicar na seta de retroceder, mas teriamos de fazer estas transformações todas outra vez.
Existe um botão que premite fazer uma nova query sem alterar a formatação atual dos dados

Vamos ao menu DADOS e clicamos no botão com um ponto de interrogação verde

E voltamos ao menu do query, que está pre-selecionado com o nosso query original

Alteramos a data para janeiro e executamos o relatório

E aqui está tabela com a mesma estrutura mas com uma data diferente."""
)

st.subheader("Eliminar celulas unidas unidas")

st.markdown(
    """Ainda no mesmo relatório, se cikicarnis medico de familia

vemos que criamos"""
)

st.subheader("Exportação")
