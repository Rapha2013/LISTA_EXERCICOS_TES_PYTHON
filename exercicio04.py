# A estratégia:

# Inicie solicitando ao usuário que insira os campos obrigatórios, separados por vírgula. 
# Em seguida, entre em um loop de menu que permita ao usuário escolher entre as opções de cadastro, listagem com filtro por nomes, campos e valores, nomes e campos, e encerramento do programa. 
# Cada seleção acionará uma função correspondente para execução.


# Detalhamento das Estruturas:

# banco_usuarios: Armazena os dicionários de usuários em uma lista.
# cadastrar_usuario: Permite cadastrar um novo usuário e adicional um campo se for necessário.
# imprimir_usuarios: Imprime os usuários com opções de filtro.
# banco_palavras: Função principal onde fica em um loop continúo até o usuário queria sair. 

# Dicionário global para armazenar os usuários
banco_usuarios = []

# Função para cadastrar um usuário
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    # Itera sobre os campos obrigatórios e solicita valores ao usuário
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    
    # Solicita campos adicionais até que o usuário digite 'sair'
    while True:
        campo_adicional = input("Digite um campo adicional ou 'sair' para finalizar: ")
        if campo_adicional.lower() == 'sair':
            break
        valor_adicional = input(f"Digite o valor para o campo '{campo_adicional}': ")
        usuario[campo_adicional] = valor_adicional
    
    # Adiciona o usuário ao banco de usuários
    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para imprimir usuários
def imprimir_usuarios(*args, **kwargs):
    if not args and not kwargs:
        # Se nenhum argumento ou parâmetro for fornecido, imprime todos os usuários
        for usuario in banco_usuarios:
            print(usuario)
    elif args:
        # Se nomes forem fornecidos como argumentos, filtra e imprime os usuários correspondentes
        nomes_filtrados = args
        for usuario in banco_usuarios:
            if usuario['nome'] in nomes_filtrados:
                print(usuario)
    elif kwargs:
        # Se parâmetros de filtro forem fornecidos, filtra e imprime os usuários correspondentes
        usuarios_filtrados = []
        for usuario in banco_usuarios:
            condicoes_satisfeitas = True
            for campo, valor in kwargs.items():
                if campo not in usuario or usuario[campo] != valor:
                    condicoes_satisfeitas = False
                    break
            if condicoes_satisfeitas:
                usuarios_filtrados.append(usuario)
        for usuario in usuarios_filtrados:
            print(usuario)

# Função principal
def banco_palavras():
    # Solicita os campos obrigatórios ao usuário e os separa por vírgula
    campos_obrigatorios = input("Digite os campos obrigatórios separados por vírgula: ").split(',')
    
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            # Chama a função para cadastrar um usuário com os campos obrigatórios definidos
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            print("1 - Imprimir todos")
            print("2 - Filtrar por nomes")
            print("3 - Filtrar por campos")
            print("4 - Filtrar por nomes e campos")
            sub_opcao = input("Escolha uma sub-opção: ")
            
            if sub_opcao == '1':
                # Chama a função para imprimir todos os usuários
                imprimir_usuarios()
            elif sub_opcao == '2':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                # Chama a função para imprimir usuários filtrando por nomes
                imprimir_usuarios(*nomes)
            elif sub_opcao == '3':
                campos = input("Digite os campos separados por vírgula: ").split(',')
                valores = {}
                for campo in campos:
                    valor = input(f"Digite o valor para o campo '{campo}': ")
                    valores[campo] = valor
                # Chama a função para imprimir usuários filtrando por campos e valores
                imprimir_usuarios(**valores)
            elif sub_opcao == '4':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                campos = input("Digite os campos separados por vírgula: ").split(',')
                valores = {}
                for campo in campos:
                    valor = input(f"Digite o valor para o campo '{campo}': ")
                    valores[campo] = valor
                # Chama a função para imprimir usuários filtrando por nomes e campos
                imprimir_usuarios(*nomes, **valores)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal para iniciar o programa
banco_palavras()
