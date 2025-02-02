# A biblioteca json permite criar, ler e editar arquvos json, que será usado como banco de dados de usuários e peças. 
# A biblioteca random permite aleatorizar de peças que serão exibidas no relatório.
import json, random

# Caminho do arquivo JSON. Caso o arquivo não exista, o programa o criará após o primeiro cadastro de usuário.
ARQUIVO_JSON = 'dados.json'

# Conjunto de funções para manipular os dados do arquivo JSON.
def carregar_dados():
    '''Faz a leitura do arquvo JSON. Caso o arquivo não exista, retorna um dicionário vazio para cadastro de usuários e roupas.'''
    try:
        with open(ARQUIVO_JSON, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {"usuarios": {}, "roupas": {}}

def salvar_dados(dados):
    '''Edita os dados do arquivo JSON.'''
    with open(ARQUIVO_JSON, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

# Conjunto de funções que retornam mensagens recorrentes aos usuários.
def descricao_projeto():
    '''Imprime os objetivos do Projeto faz_circular na tela.'''
    print('''
=========================================================================
    Projeto Faz_Circular
=========================================================================

    O projeto Faz_Circular propõe a ideia de promover sustentabilidade e 
reutilização de roupas dentro do ciclo universitário, conectando a comu-
nidade acadêmica para doações de peças do vestuário que ainda estejam em 
condições de uso e sejam úteis a outras pessoas.\n
    O descarte inadequado de peças de vestuário no meio ambiente repre-
senta está entre os grandes desafios ambientais da atualidade. A maior 
parte das roupas descartadas acaba em aterros sanitários, lixões ou em 
locais inapropriados, onde podem levar décadas para se decompor, liberando
substâncias químicas nocivas ao solo e à água. No início da cadeia produ-
tiva têxtil, a produção exerce impacto ambiental substancial, consumindo 
vastas quantidades de recursos naturais, como água e energia, além de ge-
rar emissões de gases de efeito estufa e poluir rios ou lençóis freáticos 
com resíduos químicos provenientes do tingimento e tratamento dos tecidos.\n
    Nesse contexto, surge o projeto Faz_Circular, uma plataforma para 
estudantes, professores e trabalhadores da nossa universidade que conecta 
quem quer doar com quem quer receber roupas em condições de uso. A ideia 
do projeto é promover a redução do impacto ambiental para incentivar a res-
significação de peças do vestuário, diminuindo a geração de lixo.\n
    O que mais nosso projeto promove?
    - Economia Circular: Ele incentiva o reuso e a reutilização, prolongan-
      do a vida útil de peças de vestuário e evitando que sejam descartados
      prematuramente.
    - Consciência Ambiental: Estimula as pessoas a pensarem em soluções 
      sustentáveis antes de comprar algo novo, reduzindo a demanda por pro-
      dução industrial, que consome recursos naturais e gera poluição.
    - Comunidade e Conexões: O projeto cria um senso de pertencimento, co-
      nectando estudantes, professores e trabalhadores da universidade em 
      uma rede que facilita trocas e interações.
    - Acessibilidade e Inclusão: Promove o acesso a peças de vestuário 
      úteis, especialmente para pessoas com menor poder aquisitivo, que po-
      dem adquirir o que precisam de maneira gratuita.
    - Educação e Sustentabilidade: Além de ressignificar as roupas, ele en-
      sina sobre o impacto positivo que pequenas ações podem ter no meio 
      ambiente e na comunidade.
    - Redução do Desperdício: Minimiza a quantidade de lixo enviada para 
      aterros sanitários, lixões ou outros lugares inadequados, contribu-
      indo para a diminuição de poluição e emissão de gases de efeito 
      estufa.

=========================================================================\n''')
    sair = input('Tecle Enter para retornar ao menu principal. ')

def menu_principal():
    '''Imprime o menu principal na tela.'''
    print('''
=========================================================================
    MENU PRINCIPAL
=========================================================================
    
    Selecione uma das opções numéricas a seguir:
    
    1 - Conheça o nosso projeto.
    2 - Faça o login.
    3 - Cadastre-se.
    4 - Recupere seu usuário ou senha.
    5 - Sair do sistema.

=========================================================================''')

def menu_controle():
    '''Imprime o menu de controle na tela.'''   
    print("""
=========================================================================
    MENU DE CONTROLE
=========================================================================

    Selecione uma das opções numéricas a seguir:

    1. Cadastre uma roupa para doação.
    2. Consulte usuários interessados em receber suas roupas cadastradas.
    3. Gerencie as roupas que você pôs para doação.
    4. Procure por roupas que estejam em doação.
    5. Reserve roupas que estejam em doação.
    6. Edite o seu cadastro.
    7. Exclua o seu cadastro.
    8. Sair do sistema.

=========================================================================""")

def msg_recuperacao_senha():
    print("""
=========================================================================
                                ATENÇÃO
=========================================================================

Para recuperar o seu usuário ou senha entre em contato com a equipe do 
projeto através do e-mail faz.circular@unb.br e solicite a recuperação.
Aguardaremos o seu contato.

=========================================================================
""")

# Função para validar entrada de nome de usuário
def validar_usuario(usuario):
    for char in usuario:
        if not ("a" <= char <= "z" or "0" <= char <= "9"):
            return False
    return True

# Função para validar nome completo
def validar_nome(nome):
    return len(nome.split()) >= 2

# Função para validar e-mail institucional
def validar_email(email):
    if "@" not in email:
        return False
    prefixo, dominio = email.split("@", 1)
    if dominio not in ["unb.br", "aluno.unb.br"]:
        return False
    for char in prefixo:
        if not ("a" <= char <= "z" or char in "._0123456789"):
            return False
    return True

# Função para validar telefone
def validar_telefone(telefone):
    if not telefone.startswith("+"):
        return False
    return telefone[1:].isdigit() and 10 <= len(telefone) <= 15

# Função para login de usuários
def login_usuario(dados):
    print("""
=========================================================================
    Efetue o Login
=========================================================================\n""")
    usuario = input("Digite o nome do usuário: ")
    if usuario not in dados["usuarios"]:
        print("\nUsuário não encontrado.")
        sair = input("Tecle Enter para retornar ao menu principal. ")
        return "#"
    senha = input("Digite sua senha: ")
    if dados["usuarios"][usuario]["senha"] == senha:
        print(f'\nLogin efetuado com sucesso! Bem-vindo, {dados["usuarios"][usuario]["nome_usuario"]}.')
        sair = input("Tecle Enter para continuar. ")
        return usuario
    else:
        print("\nSenha inválida. Caso tenha esquecido sua senha, entre em contato com a equipe do projeto através do email faz_circular@gmail.com.")
        sair = input("Tecle Enter para retornar ao menu principal. ")
        return "#"

# Função para cadastro de usuários
def cadastrar_usuario(dados):
    print("""
=========================================================================
    Cadastro de Usuário
=========================================================================\n""")
    while True:
        usuario = input("Escolha um nome para o seu usuário (use apenas letras minúsculas e números): ")
        if not validar_usuario(usuario):
            print("Usuário inválido. Tente novamente.")
            continue
        if usuario in dados["usuarios"]:
            print("Este usuário já existe. Escolha outro nome de usuário.")
            continue
        break

    while True:
        nome_usuario = input("Digite o seu nome completo: ")
        if not validar_nome(nome_usuario):
            print("Nome inválido. Seu nome deve conter no mínimo duas palavras.")
            continue
        break

    while True:
        email_inst = input("Digite seu e-mail institucional: ")
        if not validar_email(email_inst):
            print("E-mail institucional inválido. Cadastre um e-mail terminado em @unb.br ou @aluno.unb.br.")
            continue
        break

    while True:
        telefone = input("Digite seu telefone para contato (exemplo: +5561987654321): ")
        if not validar_telefone(telefone):
            print("Telefone inválido. Tente novamente.")
            continue
        break

    while True:
        vinculo = input("Escolha o seu vínculo com a UnB (P - Professor, A - Aluno, F - Funcionário, O - Outro): ").upper()
        if vinculo not in ["P", "A", "F", "O"]:
            print("Opção inválida. Tente novamente.")
            continue
        break

    while True:
        senha = input("Digite uma senha: ")
        confirma_senha = input("Digite novamente sua senha: ")
        if senha != confirma_senha:
            print("As senhas não coincidem. Tente novamente.")
            continue
        break

    # Confirmar cadastro
    while True:
        confirmacao = input(f"Você confirma o cadastro do usuário {usuario}? (S - Sim, N - Não): ").upper()
        if confirmacao == "S":
            dados["usuarios"][usuario] = {
                "nome_usuario": nome_usuario,
                "email_inst": email_inst,
                "telefone": telefone,
                "vinculo": vinculo,
                "senha": senha
            }
            salvar_dados(dados)
            print("\nUsuário cadastrado com sucesso!")
            sair = input("Tecle Enter para retornar ao menu principal. ")
            return
        elif confirmacao == "N":
            print("Cadastro cancelado.")
            sair = input("Tecle Enter para retornar ao menu principal.\n")
            return
        else:
            print("Opção inválida. Tente novamente.")

# Função para editar o usuário logado.
def editar_usuario(dados, usuario):
    print("""
=========================================================================
    Editar Cadastro de Usuário
=========================================================================\n""")
    
    print("    Informações atuais do usuário\n")
    print(f'         Nome do usuário: {dados["usuarios"][usuario]["nome_usuario"]}')
    print(f'    E-mail institucional: {dados["usuarios"][usuario]["email_inst"]}')
    print(f'                Telefone: {dados["usuarios"][usuario]["telefone"]}')
    print(f'                 Vínculo: {dados["legenda"]["vinculo"][dados["usuarios"][usuario]["vinculo"]]}')
    print('\n-------------------------------------------------------------------------\n')

    while True:
        confirmacao = input("Você realmente deseja iniciar a edição deste cadastro? \nEsta ação será irreversível (S - Sim, N - Não): ").upper()
        if confirmacao == "N":
            print("Edição cancelada.")
            sair = input("Tecle Enter para retornar ao menu de controle. ")
            return
        elif confirmacao == "S":
            while True:
                nome_usuario = input(f"\nReescreva o nome completo que substituirá [{dados['usuarios'][usuario]['nome_usuario']}] ou pressione Enter para manter o valor atual: ") or dados["usuarios"][usuario]["nome_usuario"]
                if not validar_nome(nome_usuario):
                    print("Nome inválido. Deve conter no mínimo duas palavras.")
                    continue
                break
            while True:
                email_inst = input(f"\nReescreva o e-mail institucional que substituirá [{dados['usuarios'][usuario]['email_inst']}] ou pressione Enter para manter o valor atual: ") or dados["usuarios"][usuario]["email_inst"]
                if not validar_email(email_inst):
                    print("E-mail institucional inválido. Deve terminar em @unb.br ou @aluno.unb.br.")
                    continue
                break
            while True:
                telefone = input(f"\nReescreva o telefone que substituirá [{dados['usuarios'][usuario]['telefone']}] ou pressione Enter para manter o valor atual: ") or dados["usuarios"][usuario]["telefone"]
                if not validar_telefone(telefone):
                    print("Telefone inválido. Deve começar com + e conter de 10 a 15 dígitos.")
                    continue
                break
            while True:
                vinculo = input(f"\nSelecione o código do vínculo que substituirá [{dados['usuarios'][usuario]['vinculo']}] ou pressione Enter para manter o valor atual. \n(P - Professor, A - Aluno, F - Funcionário, O - Outro): ").upper() or dados["usuarios"][usuario]["vinculo"]
                if vinculo not in ["P", "A", "F", "O"]:
                    print("Vínculo inválido. Deve ser P (Professor), A (Aluno), F (Funcionário) ou O (Outro).")
                    continue
                break
            dados["usuarios"][usuario].update({
                "nome_usuario": nome_usuario,
                "email_inst": email_inst,
                "telefone": telefone,
                "vinculo": vinculo
            })
            salvar_dados(dados)
            print("\nCadastro atualizado com sucesso!")
            sair = input("Tecle Enter para retornar ao menu de controle. ")
            return
        else:
            print("\nOpção inválida, tente novamente.")


# Função para excluir o usuário logado.
def excluir_usuario(dados, usuario):
    '''Exclui o usuário logado, as peças por ele cadastradas e as reservas por ele realizadas.'''
    print("""
=========================================================================
    Exclusão de Usuário
=========================================================================""")
    
    while True:
        confirmacao = input(f"\nATENÇÃO: Tem certeza que deseja excluir o usuário '{usuario}'? \nEssa ação é irreversível e também apagará as roupas cadastradas e as \nreservas realizadas. (S - Sim, N - Não): ").upper()
        if confirmacao == "S":
            
            # cancela as reservas
            for chaave, valor in dados["roupas"].items():
                if valor.get("reserva") == usuario:
                    valor["reserva"] = ""

            # deleta as roupas cadastradas
            dados["roupas"] = {
                chave: valor for chave, valor in dados["roupas"].items() if valor.get("doador") != usuario # esta linha faz uma filtragem no dicionário, mantendo apenas aquilo que interessa.
            }

            # deleta o usuário            
            del dados["usuarios"][usuario]
            
            # salva as alterações no arquivo json
            salvar_dados(dados)
            print("\nUsuário excluído com sucesso.")
            sair = input("Tecle Enter para sair do sistema. ")
            return "S"
        elif confirmacao == "N":
            print("\nOperação cancelada.")
            sair = input("Tecle Enter para retornar ao menu. ")
            return "N"
        else:
            print("\nOpção inválida.")

# Função para gerar um id sequenciado
def gerar_id_automatico(roupas):
    """Gera um novo ID baseado no maior ID existente."""
    if roupas:
        return max(int(roupa["id"]) for roupa in roupas.values()) + 1
    return 1

# Função para validar a descrição.
def validar_descricao():
    """Valida a descrição da peça."""
    while True:
        descricao = input("Que peça de roupa você deseja doar? (ex.: camisa, short, casaco, maiô, etc.): ").lower()
        if len(descricao) <= 50:
            return descricao
        print("Você excedeu o limite de 50 caracteres. Tente novamente.")

# Função para validar a entrada da categoria
def validar_categoria():
    """Valida a entrada da categoria."""
    categorias_validas = ["PC", "PB", "CI", "MP", "PJ", "AC", "RF", "RE"]
    while True:
        categoria = input('''
=========================================================================
    Selecione uma categoria para a sua peça de vestuário
=========================================================================

    PC – Parte de Cima
    PB – Parte de Baixo
    CI – Corpo Inteiro (vestidos, macacões, body, etc.)
    MP – Moda Praia
    PJ – Pijamas
    AC – Acessórios
    RF – Roupas de Frio
    RE - Roupas Esportivas 

=========================================================================
Informe sua opção: ''').upper()
        if categoria in categorias_validas:
            return categoria
        print("Opção inválida, tente novamente.")

def validar_cor():
    """Valida a entrada da cor."""
    while True:
        cor = input("Informe a cor predominante da roupa: ").lower()
        if all(char.islower() or char == '-' for char in cor):
            return cor
        print("Resposta inválida. Use apenas letras minúsculas e hífen.")

def validar_tamanho():
    """Valida a entrada do tamanho."""
    while True:
        tamanho = input("Informe o tamanho da peça: ").upper()
        if all(char.isalnum() for char in tamanho):
            return tamanho
        print("Resposta inválida. Use apenas letras maiúsculas ou números.")

def validar_genero():
    """Valida a entrada do gênero."""
    generos_validos = ["F", "M", "A", "S"]
    while True:
        genero = input('''
=========================================================================
    Selecione um gênero para a peça de roupa
=========================================================================

    F – Feminino
    M – Masculino
    A – Ambos
    S – Sem gênero

=========================================================================

Informe sua opção: ''').upper()
        if genero in generos_validos:
            return genero
        print("Opção inválida, tente novamente.")

# Função para validar a entrada do estilo de roupa.
def validar_estilo():
    """Valida a entrada do estilo."""
    estilos_validos = ["CS", "ST", "RM", "CL", "SX", "HP", "GR", "VT", "RK", "GK"]
    while True:
        estilo = input('''
=========================================================================
    Selecione o estilo da peça: 
=========================================================================

    CS – Casual
    ST – Street
    RM – Romântico
    CL – Clássico
    SX – Sexy
    HP – Hippie
    GR – Grunge
    VT – Vintage
    RK – Rock & Punk
    GK – Geek

=========================================================================
Informe sua opção: ''').upper()
        if estilo in estilos_validos:
            return estilo
        print("Opção inválida, tente novamente.")

# Função para validar a faixa etária
def validar_faixa_etaria():
    """Valida a faixa etária."""
    faixas_validas = ["BB", "CR", "TN", "AD"]
    while True:
        faixa = input('''
=========================================================================
    Selecione uma faixa etária: 
=========================================================================

    BB – Bebê
    CR – Criança
    TN – Adolescente
    AD – Adulto

=========================================================================

Informe sua opção: ''').upper()
        if faixa in faixas_validas:
            return faixa
        print("Opção inválida, tente novamente.")

# Função para validação do estado de conservação da roupa
def validar_conservacao():
    """Valida a descrição do estado de conservação."""
    while True:
        conservacao = input("Descreva resumidamente o estado de conservação da peça: ").lower()
        if len(conservacao) <= 50:
            return conservacao
        print("Você excedeu o limite de 50 caracteres. Tente novamente.")

def gestao_roupas(dados, usuario_logado):
    '''Exibe o menu de gerenciamento das roupas cadastradas pelo usuário logado.'''

    print('\n=========================================================================\n')
    print("    Selecione uma das opções:\n")
    print("    C - Consultar roupas reservadas")
    print("    R - Remover reserva de uma roupa")
    print("    E - Editar o cadastro de uma roupa")
    print("    D - Deletar uma roupa cadastrada")
    print(f"    T - Consultar todas as roupas cadastradas por {usuario_logado}")
    print("    X - Cancelar operação")
    print('\n=========================================================================\n')
    
    while True:
        opcao = input("Digite sua opção: ").upper()
        
        if opcao == "C":
            consultar_roupas_reservadas(dados, usuario_logado)
            return
        elif opcao == "R":
            remover_reserva_roupa(dados, usuario_logado)
            return
        elif opcao == "E":
            editar_roupa(dados, usuario_logado)
            return
        elif opcao == "D":
            deletar_roupa(dados, usuario_logado)
            return
        elif opcao == "T":
            consultar_roupas_usuario(dados, usuario_logado)
            return
        elif opcao == "X":
            print("Operação cancelada.")
            sair = input('Tecle Enter para retornar ao menu de controle. ')
            return
        else:
            print("Opção inválida. Tente novamente.")
            continue

def consultar_roupas_reservadas(dados, usuario_logado):
    '''Gera uma relação das roupas reservadas.'''
    
    # ATENÇÃO: esta é uma sintaxe bastante resumida para criar uma lista de roupas que cadastrada pelo usuário logado e reservas feitas.
    # 'r for r in dados["roupas"].values()' adicionará os códigos da roupas na lista 'roupas_reservadas'.
    # 'if r["doador"] == usuario_logado and r["reserva"]' condiciona quais códigos entrarão na lista 'roupas_reservadas'.
    # 'r["reserva"]' é um a sintaxe resumida para verificar se r["reserva"] é diferente de vazio.
    roupas_reservadas = [r for r in dados["roupas"].values() if r["doador"] == usuario_logado and r["reserva"]]
        
    if not roupas_reservadas:
        print("Nenhuma roupa reservada.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    print("\n=========================================================================")
    print(" RELAÇÃO DE ROUPAS RESERVADAS")
    print("=========================================================================\n")

    # Embaralha o dicionário de roupas
    random.shuffle(roupas_reservadas)
    
    for roupa in roupas_reservadas:
        print(f"           ID: {roupa['id']}")
        print(f"    Descrição: {roupa['descricao']}")
        print(f"    Categoria: {dados["legenda"]["categoria"][roupa['categoria']]}")
        print(f"          Cor: {roupa['cor']}")
        print(f"      Tamanho: {roupa['tamanho']}")
        print(f"       Gênero: {dados["legenda"]["genero"][roupa['genero']]}")
        print(f"       Estilo: {dados["legenda"]["estilo"][roupa['estilo']]}")
        print(f" Faixa etária: {dados["legenda"]["faixa_etaria"][roupa['faixa_etaria']]}")
        print(f"  Conservação: {roupa['conservacao']}")
        print(f"Reservado por: {dados['usuarios'].get(roupa['reserva'], {}).get('nome_usuario', 'Desconhecido')}")
        print(f"       E-mail: {dados['usuarios'].get(roupa['reserva'], {}).get('email_inst', 'Não informado')}")
        print(f"     Telefone: {dados['usuarios'].get(roupa['reserva'], {}).get('telefone', 'Não informado')}")
        print("\n-------------------------------------------------------------------------\n")

    print(f' Total de roupas reservadas: {len(roupas_reservadas)}')
    print(' ATENÇÃO: Entre em contato com as pessoas interessadas para combinar os detalhes da doação.')
    sair = input(' Tecle Enter para retornar ao menu de controle. ')
    print("\n=========================================================================\n")

def remover_reserva_roupa(dados, usuario_logado):
    '''Remove a reserva de uma roupa, desde que a roupa tenha sido dacastrada pelo usuário logado.'''

    codigo = input("Digite o código da roupa: ")
    
    if codigo not in dados["roupas"]:
        print("Código não localizado.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    roupa = dados["roupas"][codigo]
    if roupa["doador"] != usuario_logado:
        print(f"Você não pode remover a reserva de peças cadastradas por outros usuários.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    if not roupa["reserva"]:
        print("Esta roupa não está reservada.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    print("\n-------------------------------------------------------------------------\n")
    print('Confira as informações da reserva antes de continuar o cancelamento:\n')
    print(f"           ID: {roupa['id']}")
    print(f"    Descrição: {roupa['descricao']}")
    print(f"    Categoria: {dados["legenda"]["categoria"][roupa['categoria']]}")
    print(f"          Cor: {roupa['cor']}")
    print(f"      Tamanho: {roupa['tamanho']}")
    print(f"       Gênero: {dados["legenda"]["genero"][roupa['genero']]}")
    print(f"       Estilo: {dados["legenda"]["estilo"][roupa['estilo']]}")
    print(f" Faixa etária: {dados["legenda"]["faixa_etaria"][roupa['faixa_etaria']]}")
    print(f"  Conservação: {roupa['conservacao']}")
    print(f"Reservado por: {dados['usuarios'].get(roupa['reserva'], {}).get('nome_usuario', 'Desconhecido')}")
    print(f"       E-mail: {dados['usuarios'].get(roupa['reserva'], {}).get('email_inst', 'Não informado')}")
    print(f"     Telefone: {dados['usuarios'].get(roupa['reserva'], {}).get('telefone', 'Não informado')}")
    print("\n-------------------------------------------------------------------------\n")

    while True:
        confirmacao = input("Deseja realmente cancelar a reserva? (S - Sim, N - Não): ").upper()
        if confirmacao == "S":
            roupa["reserva"] = ""
            salvar_dados(dados)
            print("Reserva removida com sucesso.")
            sair = input('Tecle Enter para retornar ao menu de controle.')
            return
        elif confirmacao == "N":
            print("Operação cancelada.")
            sair = input('Tecle Enter para retornar ao menu de controle.')
            return
        else:
            print("Opção inválida.")
            sair = input('Tecle Enter para tentar novamente.')
            continue

def editar_roupa(dados, usuario_logado):
    '''Edita o cadastro de uma peça e roupa cadastrada pelo usuário logado.'''
    
    codigo = input("Digite o código da roupa: ")
    
    if codigo not in dados["roupas"]:
        print("Código inválido.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    roupa = dados["roupas"][codigo]
    if roupa["doador"] != usuario_logado:
        print("Você não pode editar roupas cadastradas por outros usuários.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    print("\n-------------------------------------------------------------------------\n")
    print('Confira as informações da peça cadastrada antes de continuar com a edição:\n')
    print(f"           ID: {roupa['id']}")
    print(f"    Descrição: {roupa['descricao']}")
    print(f"    Categoria: {dados["legenda"]["categoria"][roupa['categoria']]}")
    print(f"          Cor: {roupa['cor']}")
    print(f"      Tamanho: {roupa['tamanho']}")
    print(f"       Gênero: {dados["legenda"]["genero"][roupa['genero']]}")
    print(f"       Estilo: {dados["legenda"]["estilo"][roupa['estilo']]}")
    print(f" Faixa etária: {dados["legenda"]["faixa_etaria"][roupa['faixa_etaria']]}")
    print(f"  Conservação: {roupa['conservacao']}")
    print("\n-------------------------------------------------------------------------\n")
    
    id = str(roupa['id'])
    while True:
        confirmacao = input("Você realmente deseja iniciar a edição desta peça? \nEsta ação será irreversível (S - Sim, N - Não): ").upper()
        if confirmacao == "N":
            print("Edição cancelada.")
            sair = input("Tecle Enter para retornar ao menu de controle.")
            return
        elif confirmacao == "S":
            
            descricao = validar_descricao()
            categoria = validar_categoria()
            cor = validar_cor()
            tamanho = validar_tamanho()
            genero = validar_genero()
            estilo = validar_estilo()
            faixa_etaria = validar_faixa_etaria()
            conservacao = validar_conservacao()

            #salvar os dados
            dados["roupas"][id].update({
                "descricao": descricao, 
                "categoria": categoria,
                "cor": cor, 
                "tamanho": tamanho,
                "genero": genero,
                "estilo": estilo,
                "faixa_etaria": faixa_etaria,
                "conservacao": conservacao
            })
            salvar_dados(dados)
            print("\nCadastro atualizado com sucesso!")
            sair = input("Tecle Enter para retornar ao menu de controle. ")
            return
        else:
            print("\nOpção inválida, tente novamente.")
    
    #salvar_dados(dados)
    #print("Roupa editada com sucesso.")

def deletar_roupa(dados, usuario_logado):
    '''Deleta a peça de vestuário cadastrada pelo usuário logado.'''
    
    codigo = input("Digite o código da roupa: ")
    
    if codigo not in dados["roupas"]:
        print("Código inválido.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    roupa = dados["roupas"][codigo]
    if roupa["doador"] != usuario_logado:
        print("Você não pode excluir roupas cadastradas por outros usuários.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    while True:
        confirmacao = input("Deseja realmente excluir esta peça? (S - Sim, N - Não): ").upper()
        if confirmacao == "S":
            del dados["roupas"][codigo]
            salvar_dados(dados)
            print("Roupa excluída com sucesso.")
            sair = input('Tecle Enter para retornar ao menu de controle.')
            return
        elif confirmacao == "N":
            print("Operação cancelada.")
            sair = input('Tecle Enter para retornar ao menu de controle.')
            return
        else:
            print("Opção inválida.")
            sair = input('Tecle Enter para tentar novamente.')
            continue

def consultar_roupas_usuario(dados, usuario_logado):
    '''Lista todas as roupas cadastradas pelo usuário logado, independentemente da reserva.'''

    roupas_usuario = [r for r in dados["roupas"].values() if r["doador"] == usuario_logado]
    
    if not roupas_usuario:
        print("Nenhuma roupa cadastrada.")
        sair = input('Tecle Enter para retornar ao menu de controle.')
        return
    
    print("\n=========================================================================")
    print(f" RELAÇÃO DE ROUPAS CADASTRADAS POR {dados['usuarios'].get(usuario_logado).get('nome_usuario', 'Desconhecido').upper()}")
    print("=========================================================================\n")
    
    # Embaralha o dicionário de roupas 
    random.shuffle(roupas_usuario)

    for roupa in roupas_usuario:

        print(f"           ID: {roupa['id']}")
        print(f"    Descrição: {roupa['descricao']}")
        print(f"    Categoria: {dados["legenda"]["categoria"][roupa['categoria']]}")
        print(f"          Cor: {roupa['cor']}")
        print(f"      Tamanho: {roupa['tamanho']}")
        print(f"       Gênero: {dados["legenda"]["genero"][roupa['genero']]}")
        print(f"       Estilo: {dados["legenda"]["estilo"][roupa['estilo']]}")
        print(f" Faixa etária: {dados["legenda"]["faixa_etaria"][roupa['faixa_etaria']]}")
        print(f"  Conservação: {roupa['conservacao']}")
        if roupa['reserva'] != "":
            print(f"Reservado por: {dados['usuarios'].get(roupa['reserva'], {}).get('nome_usuario', 'Desconhecido')}")
            print(f"       E-mail: {dados['usuarios'].get(roupa['reserva'], {}).get('email_inst', 'Não informado')}")
            print(f"     Telefone: {dados['usuarios'].get(roupa['reserva'], {}).get('telefone', 'Não informado')}")
        print("\n-------------------------------------------------------------------------\n")

    print(f' Total de roupas reservadas: {len(roupas_usuario)}')
    sair = input(' Tecle Enter para retornar ao menu de controle.\n')

# Funão para cadastrar a ropas no arquivo json.
def cadastrar_roupa(dados, usuario_logado):
    """Inicia o processo de cadastro de uma roupa."""
    roupas = dados.get("roupas", {})
    
    nova_roupa = {
        "id": gerar_id_automatico(roupas),
        "descricao": validar_descricao(),
        "categoria": validar_categoria(),
        "cor": validar_cor(),
        "tamanho": validar_tamanho(),
        "genero": validar_genero(),
        "estilo": validar_estilo(),
        "faixa_etaria": validar_faixa_etaria(),
        "conservacao": validar_conservacao(),
        "doador": usuario_logado,
        "reserva": ""
    }

    while True:
        confirmacao = input("Você confirma o cadastro desta peça de roupa? (S - Sim, N - Não): ").upper()
        if confirmacao == "S":
            roupas[nova_roupa["id"]] = nova_roupa
            dados["roupas"] = roupas
            salvar_dados(dados)
            print("Roupa cadastrada com sucesso!")
            break
        elif confirmacao == "N":
            cancelar = input("Tem certeza que deseja cancelar o cadastro? (S - Sim, C - Continuar): ").upper()
            if cancelar == "S":
                print("Cadastro cancelado.")
                break
            elif cancelar == "C":
                continue
        else:
            print("Opção inválida, tente novamente.")

def consultar_roupas_disponiveis(dados, usuario_logado):
    """Consulta todas as roupas disponíveis para doação, aplicando filtros se o usuário desejar. Exibe um relatório das roupas disponíveis no terminal."""
    roupas = dados.get("roupas", {})
    roupas_disponiveis = []


    # Pergunta se o usuário deseja aplicar filtros
    while True:
        aplicar_filtros = input("Deseja aplicar filtros para a consulta? (S - Sim, N - Não): ").strip().upper()
        if aplicar_filtros in ['S','N']:
            break
        else:
            print('Opção inválida.')
            sair = input('Tecle Enter para tentar novamente.')
            continue
    filtros = {}

    if aplicar_filtros == "S":
        while True:
            resposta = input("Deseja filtrar por categoria? (S - Sim, N - Não): ").strip().upper()
            if resposta == "S":
                filtros["categoria"] = validar_categoria()
                break
            elif resposta == "N":
                break
            else:
                print('Opção inválida.')
                sair = input('Tecle Enter para tentar novamente.')
                continue
        while True:
            resposta = input("Deseja filtrar por cor? (S - Sim, N - Não): ").strip().upper()
            if resposta == "S":
                filtros["cor"] = validar_cor()
                break
            elif resposta == "N":
                break
            else:
                print('Opção inválida.')
                sair = input('Tecle Enter para tentar novamente.')
                continue
        while True:
            resposta = input("Deseja filtrar por tamanho? (S - Sim, N - Não): ").strip().upper()
            if resposta == "S":
                filtros["tamanho"] = validar_tamanho()
                break
            elif resposta == "N":
                break
            else:
                print('Opção inválida.')
                sair = input('Tecle Enter para tentar novamente.')
                continue
        while True:
            resposta = input("Deseja filtrar por gênero? (S - Sim, N - Não): ").strip().upper()
            if resposta == "S":
                filtros["genero"] = validar_genero()
                break
            elif resposta == "N":
                break
            else:
                print('Opção inválida.')
                sair = input('Tecle Enter para tentar novamente.')
                continue
        while True:
            resposta = input("Deseja filtrar por estilo? (S - Sim, N - Não): ").strip().upper()
            if resposta == "S":
                filtros["estilo"] = validar_estilo()
                break
            elif resposta == "N":
                break
            else:
                print('Opção inválida.')
                sair = input('Tecle Enter para tentar novamente.')
                continue
        while True:
            resposta = input("Deseja filtrar por faixa etária? (S - Sim, N - Não): ").strip().upper()
            if resposta == "S":
                filtros["faixa_etaria"] = validar_faixa_etaria()
                break
            elif resposta == "N":
                break
            else:
                print('Opção inválida.')
                sair = input('Tecle Enter para tentar novamente.')
                continue

    # Filtra as roupas disponíveis
    for roupa_id, roupa in roupas.items():
        if roupa["reserva"] == "" or roupa["doador"] != usuario_logado:
            # Verifica se a roupa passa pelos filtros aplicados
            atende_filtros = all(roupa.get(chave) == valor for chave, valor in filtros.items())
            if atende_filtros:
                roupas_disponiveis.append(roupa)

    # Embaralha o dicionário de roupas
    random.shuffle(roupas_disponiveis)

    # Exibe o relatório no terminal
    print("\n=========================================================================")
    print(" RELAÇÃO DE ROUPAS DISPONÍVEIS PARA DOAÇÃO")
    print("=========================================================================\n")
    if roupas_disponiveis:
        for roupa in roupas_disponiveis:
            print(f"           ID: {roupa['id']}")
            print(f"    Descrição: {roupa['descricao']}")
            print(f"    Categoria: {dados["legenda"]["categoria"][roupa['categoria']]}")
            print(f"          Cor: {roupa['cor']}")
            print(f"      Tamanho: {roupa['tamanho']}")
            print(f"       Gênero: {dados["legenda"]["genero"][roupa['genero']]}")
            print(f"       Estilo: {dados["legenda"]["estilo"][roupa['estilo']]}")
            print(f" Faixa etária: {dados["legenda"]["faixa_etaria"][roupa['faixa_etaria']]}")
            print(f"  Conservação: {roupa['conservacao']}")
            print("\n-------------------------------------------------------------------------\n")
    else:
        print(" Nenhuma roupa disponível encontrada com os filtros aplicados.\n")
        print("=========================================================================\n")
        sair = input('Tecle Enter para retornar ao menu de controle. ')
        return
    print(f' Total de roupas encontradas: {len(roupas_disponiveis)}')
    print(' Para efetuar reservas, anote o ID das peças e use o menu de controle.')
    sair = input(' Tecle Enter para retornar ao menu de controle. ')
    print("\n=========================================================================\n")

def reservar_roupa(dados, usuario_logado):
    """Permite que um usuário reserve uma roupa disponível para doação."""
    while True:
        codigo = input("Digite o código da roupa que deseja reservar: ")
        
        if codigo not in dados["roupas"]:
            print("Código inválido.")
            sair = input('Tecle Enter para retornar ao menu de controle. ')
            return
        
        roupa = dados["roupas"][codigo]
        
        if roupa["doador"] == usuario_logado:
            print("Esta roupa foi cadastrada por você. Logo, não é possível reservá-la.")
            sair = input('Tecle Enter para retornar ao menu de controle. ')
            return
        elif roupa["reserva"] != "":
            print("Esta roupa já está reservada.")
            sair = input('Tecle Enter para retornar ao menu de controle. ')
            return
        else:
            print("\n=================================================================")
            print(f"            ID: {roupa['id']}")
            print(f"     Descrição: {roupa['descricao']}")
            print(f"     Categoria: {dados["legenda"]["categoria"][roupa['categoria']]}")
            print(f"           Cor: {roupa['cor']}")
            print(f"       Tamanho: {roupa['tamanho']}")
            print(f"        Gênero: {dados["legenda"]["genero"][roupa['genero']]}")
            print(f"        Estilo: {dados["legenda"]["estilo"][roupa['estilo']]}")
            print(f"  Faixa Etária: {dados["legenda"]["faixa_etaria"][roupa['faixa_etaria']]}")
            print(f"   Conservação: {roupa['conservacao']}")
            print("=================================================================\n")
            
            while True:
                confirmar = input("Deseja reservar esta roupa? (S - Sim, N - Não): ").strip().upper()
                if confirmar == "S":
                    roupa["reserva"] = usuario_logado
                    salvar_dados(dados)
                    doador = dados["usuarios"][roupa["doador"]]
                    print(f"\nO(a) doador(a) {doador['nome_usuario']} será informado do seu interesse.")
                    print(f"Entre em contato com ele(a) através do e-mail {doador['email_inst']} ou do telefone {doador['telefone']}.")
                    break
                elif confirmar == "N":
                    print('Reserva cancelada. ')
                    sair = input('Tecle Enter para retornar ao menu de controle. ')
                    return
                else:
                    print('Opção inválida. Tente Novamente.')

            
        while True:
            repetir = input("Deseja reservar outra roupa? (S - Sim, N - Não): ").strip().upper()
            if repetir == "N":
                sair = input('Tecle Enter para retornar ao menu de controle. ')
                return
            elif repetir == "S":
                break
            else:
                print('Opção inválida. Tente Novamente.')

# Esta é a função principal do sistema, ela chamará todas as outras funções.
def main():
    '''Executa o programa.'''
    dados = carregar_dados()

    # Faz a gestão das opções do menu principal.
    while True:
        usuario = ""
        menu_principal()
        opcao = input("\nDigite sua opção: ")

        if opcao == "1":
            descricao_projeto()
        elif opcao == "2":
            usuario = login_usuario(dados)
            if usuario == "#":
                continue
            else:
                break
        elif opcao == "3":
            cadastrar_usuario(dados)
        elif opcao == "4":
            msg_recuperacao_senha()
            sair = input("Precione Enter para retornar ao menu principal.\n")
        elif opcao == "5":
            break #Interrompe o loop while True e finaliza o sistema 
        else:
            print("Opção inválida.")
            sair = input("Tecle Enter para retornar ao menu principal. ")
    
    if usuario != "":
        while True:  
            menu_controle()
            opcao = input("\nDigite sua opção: ")

            if opcao == "1":
                cadastrar_roupa(dados, usuario)
            elif opcao == "2":
                consultar_roupas_reservadas(dados, usuario)
            elif opcao == "3":
                gestao_roupas(dados, usuario)
            elif opcao == "4":
                consultar_roupas_disponiveis(dados, usuario)
            elif opcao == "5":
                reservar_roupa(dados, usuario)
            elif opcao == "6":
                editar_usuario(dados, usuario)
            elif opcao == "7":
                if excluir_usuario(dados, usuario) == "S":
                    break
                else:
                    continue
            elif opcao == "8":
                break
            else:
                print("Opção inválida.")
                sair = input("Tecle Enter para retornar ao menu. ")


print('''
=========================================================================
                 SEJA BEM-VINDO AO PROJETO FAZ_CIRCULAR!
=========================================================================
''')
sair = input('Tecle Enter para acessar o menu principal.')
main()
print("""
=========================================================================
        OBRIGADO PELA VISITA AO PROJETO FAZ_CIRCULAR. ATÉ BREVE!
=========================================================================
""")