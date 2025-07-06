# Lista de consultas realizadas

É uma lista fundamentais para a elaboração de um curriculo. Na realidade, algumas fontes dão apenas números de consulta como o BI-CSP, outras dão a informação de quem foram os utentes, como o MIM@UF, SIARS e SClinico (spoiler alert, o Sclinico Administrativo é o melhor local para tirar esta informação...)

É habitual as contagens serem ligeiramente diferentes. Para adicionar lenha à fogueira, não da para saber bem quais as discrepâncias porque é dificil comparar os dados entre as diferentes fonte, pois nem sempre têm a mesma estrutura de dados.

Voltando à questão: não basta saber só a lista de untetes que se fez consulta, é necessário saber o **tipo de consulta**/programa associado, **presecial ou não presencial**, se o utente compareceu ou não, de quem foi a **iniciativa** e um número identificador (perferivelmente o Nº de utente, opcionalmente o NOP) para poder cruzar com outras listas relevantes.

> Para isto, só há um sitio que consegue extrair esta informação com este detalhe: o SClinico Administrativo.

Isso, nem o MIM@UF dá este detalhe - especificamente o tipo de consulta - porque provalvelmente não está implementado (mas o SIARS e o BI-CSP têm essa informação...). A questão é que a informação do tipo de consulta não é universal para todos os centros de saúde - cada centro de saúde pode dar os nomes que entender aos tipos de consulta. As vezes até há vários nomes para o mesmo tipo de consulta...

Felizmente o SClinico Administrativo têm. **E é muito simples tirar**. Só tem um senão - o ficheiro extraido é um PDF com tabelas e não um ficheiro .xlsx, portanto precisa de ser convertido depois, mas julgo que o próprio Excel faz essa conversão.

Então, peçam a um administrativo da vossa unidade para abrir a sua sessão de Sclinico e vão a este menu:
