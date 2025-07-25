# Introdução ao curriculo

O MIM@UF tem o potencial de poupar muito trabalho de colheita de dados na elaboração do curriculo. Permite a colheita de dados em larga escala, reprodutível e consisitente que um registo manual não permite (e sim, estou a incluir um excel onde se registam consultas à mão com a ajuda de um teclado).

Pode ser a até a base para análises mais complexas, como calculo do SCORE2 em larga escala ou Taxa de filtração glomerular.

Infelizmente nem toda a informação que desejavamos está disponível, o que significa que mesmo com o MIM@UF é necessário colher alguns dados manualmente.

![Referencias de relatorios e listagens úteis para currículo](images/sources_mimuf_curriculo.png)

## Situações onde o MIM@UF é claramente superior na construção do curriculo

Onde claramente o MIM@UF é uma vantagem face a qualquer outro método disponivel no momento:

- Lista de inscritos da unidade/utente
- Idade, datas de nascimento, Médico de Família, isenções, nacionalidades
- Numero de pessoas por agregado familiar
- Resultados de indicadores para médicos e unidade
- Listas de cumpridores e imcumpridores por indicador
- Top problemas da Unidade e Lista
- Lista completa de problemas ativos de cada utente\* -  carece de uma extração de mais de 20 tabelas e junção em ps-processamento - dificil mas vale a pena.
- Risco de diabetes
- Avaliação pela escala de Barthel
- Peso, altura, IMC, TAs e TAd
- Resultado de analises comuns (C. total, HDL, Trig., LDL, HbA1c, Creatinina, Albuminúria) - embora seja confuso econtrar o codigo correto na Query...
- Medicamentos prescritos com DCI, nome comercial e grupo farmacológico\* - dado a grande quantidade de nomes de medicamentos no mercado, a analise pode ser difícil, pois o mesmo medicamento pode estar registado com nomes diferentes

## Situações onde o MIM@UF pode ajudar mas não dá uma resposta direta

Há informações (Ex: óbitos) que não estão disponíveis diretamente no MIM@UF, mas as suas listagens e relatórios permitem fazer uma aproximação da realidade:

- Medicação crónica de cada utente - obtendo a lista de medicametos prescritos, podemos supor se foi prescrito (por qualquer médico no CS) provavelmente serão medicamentos habituais do utente
- Lista de problemas de doença aguda diagnosticados\* - dá o número de diagnósticos (registados no A do SOAP) feitos por médico mas não dá a que utentes

Pode ainda auxiliar a afunilar o trabalho de consulta manual:

- Óbitos (extraindo listas no início e fim do periodo de análise, e utentes que existam no início e não estão no fim sairam da lista, e certamente alguns serão óbitos)

## Situações onde o MIM@UF é omisso na construção do curriculo

Infelizmente o MUM@UF não disponibiliza, até a data, dados relevantes para curriculo - embora nalguns casos bastava apenas um pequeno ajuste no formato do relatório interno:

- Lista de códigos ICPC2 colocados no A do SOAP para cada consulta
- Texto excrito no SOAP de cada consulta
- Tipo de Família
- Todos\* os resultados de analises e relatórios de exames registados (excepto os mencionados antes)
- Profissões \* e Habilitações \* - tecnicamente dá para tirar mas a minha experiencia é que >99% dos utentes não tem preenchido, mas admito que possa variar entre Centros de Saúde
