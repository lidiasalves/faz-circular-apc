Título:
# Faz Circular

## Descrição do Projeto

  O projeto Faz_Circular propõe a ideia de promover sustentabilidade e reutilização de roupas dentro do ciclo universitário, conectando a comunidade acadêmica para doações de peças do vestuário que ainda estejam em condições de uso e sejam úteis a outras pessoas.

  O descarte inadequado de peças de vestuário no meio ambiente está entre os grandes desafios ambientais da atualidade. A maior parte das roupas descartadas acaba em aterros sanitários, lixões ou em locais inapropriados, onde podem levar décadas para se decompor, liberando substâncias químicas nocivas ao solo e à água. No início da cadeia produtiva têxtil, a produção exerce impacto ambiental substancial, consumindo vastas quantidades de recursos naturais, como água e energia, além de gerar emissões de gases de efeito estufa e poluir rios ou lençóis freáticos com resíduos químicos provenientes do tingimento e tratamento dos tecidos.

  Nesse contexto, surge o projeto Faz_Circular, uma plataforma para estudantes, professores e trabalhadores da nossa universidade que conecta quem quer doar com quem quer receber roupas em condições de uso. A ideia do projeto é promover a redução do impacto ambiental para incentivar a ressignificação de peças do vestuário, diminuindo a geração de lixo.


## Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Armazenamento dos dados**: em arquivos JSON, organizado internamente em três bibliotacas:
  - `legenda`: armazena os códigos utilizados no cadastramento de usuários e de roupas como chaves e os significados como valores.
  - `usuarios`: armazena os nomes dos usuários cadastrados como chaves e as informações dos usuários (nome completo, e-mail institucional, telefone, tipo do vínculo e senha) como valores em uma biblioteca aninhada.
  - `roupas`: armazena os IDs das roupas cadastradas por usuários logados como chaves e as informações da roupa (ID, descrição, categoria, cor, tamanho, gênero, estilo, faixa etária, conservação, doador e reserva) como valores em uma biblioteca aninhada.
- **Bibliotecas**: 
  - `random` (para tornar aleatório os itens exibidos nos relatórios)
  - `json` (para criar, ler e editar arquivos JSON).
- **Deploy**: GitHub

## Estrutura do Projeto

|Arquivos e diretórios| Finalidade
|--|--|
|/img/| Armazena  as imagens da documentação do projeto
|main.py| Script principal do projeto
|dados.json| Banco de dados em formato JSON
|README.md| Documentação do projeto

## Como executar o Projeto Faz_Circular

1. Certifique-se de ter o Phyton 3.x instalado.
2. Clone o repositório ou baixe os arquivos.
3. Execute o script principal: `main.py`
4. Siga as instruções do menu principal e do menu de controle para interagir com o sistema.

## Funcionalidades e especificações do Projeto

Ao executar o script principal do Projeto Faz_Circular (`main.py`) o usuário visualizará uma mensagem de boas-vindas, conforme imagem a seguir: 

  ![Imagem de boas-vindas.](/img/abertura.png "Imagem de boas-vindas")

Ao teclar "Enter" o usuário será imediatamente direcionado para o menu principal, conforme imagem a seguir:

  ![Imagem do menu principal.](/img/menu_principal.png "Imagem do menu principal")

Dentre as funcionalidades do Menu Principal estão:

1. **Conheça o nosso projeto**: o sistema exibirá um texto de apresentação do Projeto Faz_Circular ao usuário. O texto contém de forma resumida os objetivos do Projeto e quais problemas ambientais podem ser minimizados a partir da adesão ao projeto. Após a leitura o sistema redireciona o usuário ao Menu Principal.
   
2.  **Faça o login**: o sistema solicitará o nome do usuário e senha previamente cadastrados. As informações dos usuários cadastrados no sistema ficam armazenadas no arquivo `dados.json`. Caso o usuário não seja encontrado ou a senha esteja errada, o sistema informará o problema e redirecionará o usuário ao Menu Principal. Após a efetivação do login o usuário terá acesso ao seu Menu de Controle.
   
3.  **Cadastre-se**: o sistema realizará o cadastro de novos usuários. Só é possível utilizar o sistema, caso o usuário tenha um cadastro. Os campos solicitados para cadastramento de um novo usuário são:
   
    1.  **Nome do usuário**: obrigatoriamente com letras minúsculas ou números, não pode haver outros caracteres. Caso o usuário insira caracteres inválidos ou informe o nome de um usuário já existe o sistema solicitará outro nome de usuário.
   
    2.  **Nome Completo**: o usuário deverá informar seu nome completo. É obrigatório informar no mínimo duas palavras e apenas caracteres alfabéticos, caso contrário o sistema repetirá a pergunta até que seja fornecida uma resposta válida.
   
    3.  **E-mail institucional**: o usuário deverá informar o e-mail institucional. Como o Projeto é voltado a comunidade da Universidade de Brasília (UnB), só serão aceitos e-mail terminados em `@aluno.unb.br` ou `@unb.br`. Caso o usuário informe algo diferente do esperado, a pergunta será requerida novamente.
   
    4.  **Telefone para contato**: o usuário deverá informar o telefone para contato. O sistema exige que o telefone informado seja completo, isto é, comece com `+`, seguido de código do país, código da região e numero de telefone, caso contrário, a pergunta será requerida novamente.
   
    5.  **Tipo de vínculo com a UnB**: o usuário é obrigado a escolher entre Professor (`P`), Aluno (`A`), Funcionário (`F`) ou Outro (`O`), caso contrário, o sistema repetirá a pergunta.
   
    6.  **Senha**: o usuário deve informar uma senha de acesso ao sistema.
   
    7.  **Confirmação de senha**: o usuário deve confirmar a senha digitada na pergunta anterior. Caso as senhas não coincidam, o usuário retornará para a pergunta anterior `Digite um senha:`.
   
    8.  **Confirmação de cadastro**: o sistema perguntará ao usuário se ele realmente deseja concluir o cadastro. O sistema só aceita as respostas `S` (Sim) ou `N` (Não), qualquer outro caractere é inválido e a pergunta será repetida. Se o usuário escolher `S`, as informações do novo usuário são salvas no arquivo `dados.json`. Se o usuário escolher `N`, o cadastro é cancelado e o usuário redirecionado ao Menu Principal.
   
4.  **Recupere seu usuário ou senha**: caso o usuário não consiga lembrar qual o nome do seu usuário e/ou a senha de acesso, o sistema apresentará a seguinte mensagem na tela:
   
    > ATENÇÃO: Para recuperar o seu usuário ou senha entre em contato com a equipe do projeto através do e-mail faz.circular@unb.br e solicite a recuperação. Aguardaremos o seu contato.

5.  **Sair do Sistema**: caso o usuário decida sair do sistema, será exibida uma mensagem de despedida (conforme imagem a seguir), encerrando a execução do script `main.py`.

  ![Mensagem de despedida.](/img/saida.png "Mensagem de despedida")

A partir do login do usuário, o sistema habilitará o Menu de Controle do usuário (conforme imagem a seguir), disponibilizando outras funcionalidades ao usuário logado.

  ![Imagem do Menu de Controle.](/img/menu_controle.png "Imagem do Menu de Controle")

Entre as funcionalidades do Menu de Controle estão:

1. **Cadastrar roupas para doação**: o usuário logado poderá realizar o cadastro de peças de roupas para doação. A veracidade das informações é de responsabilidade o usuário logado. Para o cadastramento de peças de roupas, serão requeridas as seguintes informações:

   1. **Qual peça será doada**: o usuário deverá indicar um texto curto de até 50 caracteres, apontando de forma muito objetiva qual é a qual que será doada. Por exemplo: saia, blusa, calça jeans, macacão, camiseta regata, camisa polo, vestido, longo estampado, etc.
   
   2. **Categoria da peça para doação**: o usuário deverá escolher uma das oito opções disponíveis e informar o respectivo código, caso o código seja inválido a pergunta será repetida. As categorias e códigos são: Parte de Cima (`PC`), Parte de Baixo (`PB`), Corpo Inteiro (`CI`), Moda Praia (`MP`), Pijamas (`PJ`), Acessórios (`AC`), Roupas de Frio (`RF`) e Roupas Esportivas (`RE`).
   
   3. **Cor predominante da peça para doação**: o usuário deverá informar uma cor predominante. Este campo só aceita letras e hífen. Logo, não é possível informar mais de uma cor. Cores com nome composto devem obrigatoriamente ser escritas com hífen entre as palavras, por exemplo: verde-escuro, azul-petróleo, etc.
   
   4. **Tamanho da peça para doação**: o usuário deverá informar o tamanho da peça conforme etiqueta do fabricante.
   
   5. **Gênero da peça para doação**: o usuário deverá escolher uma das quatro opções de gênero e informar o respectivo código. Caso o código informado seja inválido, a pergunta será repetida. São opções de gênero para a peça cadastrada: Feminino (`F`), Masculino (`M`), Ambos (`A`) ou Sem Gênero (`S`).
   
   6. **Estilo da peça para doação**: o usuário deverá escolher uma das dez opções de estilo e informar o respectivo código. Caso o código informado seja inválido, o sistema repetirá a pergunta. São opções de estilo disponíveis no sistema: Casual (`CS`), Street (`ST`), Romântico (`RM`), Clássico (`CL`), Sexy (`SX`), Hippie (`HP`), Grunge (`GR`), Vintage (`VT`), Rock & Punk (`RK`) e Geek (`GK`).
   
   7. **Faixa etária da peça para doação**: o usuário deverá escolher uma das quatro opções de faixa etária e informar o respectivo código. Caso o código informado seja inválido, a pergunta será repetida. São opções de faixa etária disponíveis no sistema: Bebê (`BB`), Criança (`CR`), Adolescente (`TN`) e Adulto (`AD`).
   
   8. **Estado de conservação da peça para doação**: o usuário deverá descrever muito resumidamente (em 50 caracteres) o estado de conservação da peça a ser doada.
   
   9.  **Confirmação de cadastro da peça para doação**: o usuário deverá confirmar o cadastramento da peça para doação. O sistema só permite duas respostas: ou `S` (Sim) ou `N` (Não). Caso o usuário informe algo diferente, a pergunta será repetida. Se o usuário escolher `S`, a peça para doação será salva no arquivo `dados.json`. Caso o usuário escolha a opção `N`, o cadastro é cancelado. Após a resposta válida, o usuário retorna ao Menu de Controle.
   
2. **Consultar se outro usuário reservou alguma peça que o usuário logado cadastrou para doação**: caso nenhum usuário tenha realizado reserva, aparecerá a mensagem: "Nenhuma roupa reservada.". Caso algum outro usuário tenha reservado peças que o usuário logado tenha cadastrado para doação, as peças reservadas serão exibidas na tela em formato de relatório. O relatório apresentará as seguintes informações de cada peça reservada: ID, Descrição, Categoria, Cor, Tamanho, Gênero, Estilo, Faixa etária, Conservação, Quem reservou, E-mail de quem reservou, Telefone de quem reservou. A ordem de exibição das peças é randomizada. No final do relatório informa o total de peças reservadas e a seguinte mensagem:
   
  > ATENÇÃO: Entre em contato com as pessoas interessadas para combinar os detalhes da doação.

  A imagem a seguir apresenta um exemplo de relatório de ropas reservadas por outros usuários:
  ![Imagem de um relatório de reservas.](/img/reservas.png "Imagem de um relatório de reservas")

3. **Gerenciar as roupas cadastradas**: ao selecionar a opção de gerenciar as roupas cadastradas, o sistema disponibilizará seis opções de gestão ao usuário logado:

   1. **Consultar roupas reservadas**: trata-se de um outro caminho para a mesma funcionalidade da opção `2` do Menu de Controle, isto é, consultar se outro usuário reservou alguma peça que o usuário logado cadastrou para doação.

   2. **Remover reserva de uma roupa**: o sistema removerá a reserva de peças. A remoção da reserva só pode ser feita para peças cadastradas pelo usuário logado. Para iniciar a remoção da reserva é necessário informar o ID da peça. Caso o ID não seja localizado ou o ID seja de peça cadastrada por outro usuário a operação é cancelada e o usuário logado retorna ao Menu de Controle.
   
   3. **Editar o cadastro de uma roupa**: o sistema abrirá o cadastro da peça para edição. Podem ser editados os campos Descrição, Categoria, Cor, Tamanho, Gênero, Estilo, Faixa etária e Conservação. As regras de validação são as mesmas aplicadas ao cadastro da peça. Não é possível editar peças cadastradas por outros usuários. Para iniciar a edição o usuário logado deverá informar o ID da peça. Caso o ID da peça não seja localizado ou a peça cadastrada pertença por outro usuário, a operação é cancelada e o usuário logado será redirecionado para o Menu de Controle.
   
   4. **Deletar uma roupa cadastrada**: o sistema excluirá do arquivo `dados.json` uma roupa cadastrada. O sistema só permite a exclusão de peças cadastradas pelo usuário logado. Para excluir uma peça, o sistema solicitará o ID. Caso o ID informado seja inválido ou a peça cadastrada pertença a outro usuário, a operação é cancelada e o usuário logado será redirecionado ao Menu de Controle.
   
   5. **Consultar todas as roupas cadastradas**: o sistema emite um relatório com todas as peças cadastradas pelo usuário logado. Caso não haja peças cadastradas, será exibida a mensagem "Nenhuma roupa cadastrada". Para cada peça cadastrada serão exibidas as seguintes informações: ID, Descrição, Categoria, Cor, Tamanho, Gênero, Estilo, Faixa etária e Conservação. O final do relatório indica o número de peças cadastradas. Em seguida o usuário logado é redirecionado para o Menu de Controle.
    
      A imagem a seguir apresenta um exemplo de relatório de peças cadastradas por um usuário:
      ![Imagem das peças cadastradas pelo usuário logado.](/img/pecas_cadastradas.png "Imagem das peças cadastradas pelo usuário logado")

   6. **Cancelar operação**: o usuário logado é redirecionado para o Menu de Controle.
   
4. **Procurar roupas que estejam em doação**: o sistema emitirá um relatório com todas as peças disponíveis para doação, isto é, peças que não foram cadastradas pelo usuário logado e que não estejam reservadas por outros usuários. A ordem de exibição das peças cadastradas é randômica. Antes de exibir o relatório, o sistema perguntará ao usuário logado se ele deseja aplicar algum filtro, sendo possível responder apenas `S` (Sim) ou `N` (Não). Caso o usuário responda outra opção, a pergunta é repetida; caso o usuário responda `N`, todas as peças disponíveis para reserva serão exibidas; caso o usuário responda `S`, perguntas do tipo `S` (Sim) ou `N` (Não) serão requeridas para cada especificação da peça (Categoria, Cor, Tamanho, Gênero, Estilo, Faixa etária) e, para cada `S` respondido, será necessário especificar o filtro conforme orientação do sistema. O final do relatório indica quantas roupas foram localizadas.
   
   A imagem a seguir apresenta um exemplo de relatório de peças de roupas disponíveis para doação.
   ![Imagem do relatório de peças disponíveis para doação.](/img/relacao_doar.png "Imagem do relatório de peças disponíveis para doação")

5. **Reservar roupas que estejam em doação**: o sistema reservará uma peça cadastrada para o usuário logado. Não é possível reservar roupas cadastradas pelo próprio usuário logado ou roupas que já estejam reservadas por outra pessoa. Para fazer uma reserva, o sistema solicitará o ID da peça. Caso o ID não exista ou a peça esteja indisponível para reserva, a operação é cancelada e o usuário logado será redirecionado ao Menu de Controle. Caso a peça esteja disponível, um resumo da peça contendo IID, Descrição, Categoria, Cor, Tamanho, Gênero, Estilo, Faixa etária e Conservação serão exibidos na tela, seguido de uma pergunta de confirmação da reserva. A confirmação só aceita as respostas `S` (Sim) ou `N` (Não). Caso o usuário informe algo diferente, a pergunta será repetida. Caso o usuário escolha a opção `N`, a reserva é cancelada e o usuário e redirecionado ao Menu de Controle. Caso o usuário escolha `S`, a reserva será salva no arquivo `dados.json` e o sistema mostrará na tela o contato de quem cadastrou a peça para que o interessado entre em contato. 

6. **Editar o cadastro**: o sistema abre o cadastro do usuário logado para que ele realiza atualizações cadastrais. Antes de iniciar a edição, o sistema pergunta se o usuário logado realmente deseja inicia a edição, sendo possível apenas as respostas `S` (Sim) ou `N` (Não). Caso o usuário digite algo diferente, a pergunta é repetida. Caso o usuário informe `N`, a operação é cancelada e o usuário redirecionado ao Menu de Controle. Caso a resposta seja `S`, a edição é iniciada. A edição do cadastro de usuário permite alterar o nome completo do usuário, o e-mail institucional, o telefone para contato e o tipo de vínculo com a Universidade de Brasília. Não é possível alterar o nome de login do usuário. Para cada campo editado, as regras de validação são as mesmas aplicadas para o cadastro de usuário. Após a atualização cadastral o usuário logado é redirecionado para o Menu de Controle.

7. **Exclusão de cadastro**: o sistema fará a exclusão do cadastro do usuário. Está é uma operação irreversível. O sistema também excluirá todas as peças de roupa cadastradas pelo mesmo usuário logado e retirará a reserva de peças feitas pelo usuário logado.

8. **Sair do sistema**: o usuário logado sair do sistema. É exibida uma mensagem de despedida, encerrando a execução do script `main.py`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e novas funcionalidades.

## Contatos

Caso tenha dúvidas ou precise de suporte, entre em contato com a equipe do projeto:

|Membros|E-mail|
|--|--|
|Francisco Júnior|242027442@aluno.unb.br|
|Gabrielle Santos|242027451@aluno.unb.br|
|Lídia Alves|242027489@aluno.unb.br|
|Luan Moura|242012154@aluno.unb.br|