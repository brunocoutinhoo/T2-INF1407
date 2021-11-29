# T2 INF1407 - 2021.2

Professor: Alexandre Meslin

Integrantes: -Luiz Fellipe da Silveira Câmara Augusto - 1711256 -Bruno Coutinho Moretta Monteiro - 1910392

Nosso projeto consiste em um site para exibição e consulta de produtos de feiras. A ideia é que usuários do
tipo feirantes atualizem os produtos em oferta nas suas barracas para que os clientes, que compõem outro tipo
de usuário, possam visualizar todos os produtos e adicionar seus itens favoritos à lista de compras.

Os feirantes são responsáveis por zero ou mais barracas, e podem alterar as informações apenas das que lhes
pertencem. Feiras têm um endereço fixo e um dia/horário de funcionamentos, e são compostas por uma ou mais barracas. Cada barraca tem sua própria oferta de produtos, que podem ser adicionados, editados ou removidos.

Usamos o framework Bootstrap, versão 4.6, além de customizarmos alguns campos no nosso próprio arquivo de estilos. Fizemos uso, também, de JQuery, AJAX, e da biblioteca de fontes "FontAwesome". Temos operações de CRUD para as feiras, barracas, listas de compra e produtos (nem todas essas tabelas têm todas as 4 operações).

Dentre as funcionalidades do sistema, destacamos o "auto-complete" do campo "nome" na página de adicionar produto feito usando AJAX e JQuery, que sugere ao usuário nomes de produtos baseados nos produtos já existentes no banco de dados. Além disso, fizemos a validação de alguns campos chave dos formulários através de scripts em javascript, possibilitando informar o usuário durante o preenchimento do formulário.

Ao adicionar um produto a uma barraca, um bug conhecido foi que, apesar de termos feito o redirecionamento para outra página, ele não está sendo redirecionado.

---------------------------------------------------------------------------------------------------------

GUIA DO MOCHILEIRO DAS GALÁXIAS (MANUAL DO USUÁRIO)

Usuário deslogado:
Sem fazer login, o usuário pode consultar as feiras, barracas e produtos disponíveis nelas, sem poder, contudo, criar lista de compras.

Usuário Cliente:
O cliente inicia sua navegação pelo estoque clicando no link "Feiras", disponível no painel da esquerda. Clicando no nome de uma das feiras da tabela, o usuário tem acesso à lista de barracas daquela feira e, similarmente, ao clicar no nome de uma das barracas da lista, chegamos a uma página com mais detalhes sobre a barraca, junto com a lista de todos os produtos vendidos pela barraca (produtos esses informados pelo feirante responsável por ela). Aí, o usuário tem a opção de adicionar os produtos exibidos à sua lista de compras. Ele pode, também, consultar a sua lista de compras clicando no link "Minha lista", na sidebar. Nessa página, é possível consultar todos os produtos que já foram adicionados pelo usuário, podendo também excluir os indesejados.

Usuário Feirante:
O feirante pode usar todas as funcionalidades do cliente (afinal de contas, todos nós temos nossos dias de cliente), mas também pode gerenciar a(s) sua(s) barraca(s). Para isso, basta clicar em "Minhas barracas" e, ao clicar no nome de uma delas, temos as informações da barraca, junto com a opção de editá-las. Além disso, temos a tabela com os produtos e as opções de CRUD.

Usuário Admin:
O admin é o único usuário com o poder de adicionar, editar e/ou deletar as feiras. Tirando isso, tem a mesma navegação do feirante.
