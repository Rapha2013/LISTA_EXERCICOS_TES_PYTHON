
# A estratégia:

# A uma função principal que se repete continuamente até que haja um vencedor ou um empate. 
# Em cada repetição, o tabuleiro é exibido para mostrar o estado atual do jogo. 
# O jogador atual é então solicitado a escolher uma linha e uma coluna para fazer uma jogada. 
# Essas jogadas são verificadas para garantir que estejam dentro dos limites permitidos e que a posição escolhida esteja vazia. 
# Após serem validadas, a posição no tabuleiro é preenchida com o símbolo do jogador atual, e o contador de jogadas é incrementado. 
# Após cada jogada, o código verifica se o jogador atual venceu o jogo ou se houve um empate. Se alguma das condições for satisfeita, o jogo termina.


# Detalhamento das Estruturas:

# tabuleiro: É o tabuleiro do jogo, representado por uma matriz 4x4, inicialmente vazio.
# jogador_atual: Mantém o símbolo do jogador atual, começando com "X".
# jogadas: Conta o número de jogadas feitas.
# imprimir_tabuleiro(tabuleiro): Função para mostrar o tabuleiro na tela.
# verificar_vitoria(tabuleiro, jogador): Função que verifica se o jogador venceu.
# jogo_da_velha(): Função principal que controla o fluxo do jogo. Ela inicializa o tabuleiro, permite que os jogadores façam jogadas, verifica o vencedor ou empate e alterna os jogadores até que o jogo termine.

# Define uma função para imprimir o tabuleiro.
def imprimir_tabuleiro(tabuleiro):
    # Itera pelas linhas do tabuleiro.
    for linha in tabuleiro:
        # Imprime uma linha da grade do tabuleiro.
        print(" | ".join(linha))
        # Imprime uma linha horizontal para separar as linhas do tabuleiro.
        print("-" * 15)

# Define uma função para verificar se um jogador venceu o jogo.
def verificar_vitoria(tabuleiro, jogador):
    # Verifica se o jogador venceu nas linhas ou colunas.
    for i in range(4):
        if all(tabuleiro[i][j] == jogador for j in range(4)) or all(tabuleiro[j][i] == jogador for j in range(4)):
            return True

    # Verifica se o jogador venceu nas diagonais.
    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    # Retorna False se o jogador não venceu.
    return False

# Define a função principal do jogo.
def jogo_da_velha():
    # Inicializa o tabuleiro 4x4 com espaços vazios.
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    jogador_atual = "X"  # Define o jogador atual como "X".
    jogadas = 0  # Inicializa o contador de jogadas.

    while True:  # Loop principal do jogo.
        imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro atual.

        # Solicita ao jogador atual que escolha uma linha e coluna para fazer uma jogada.
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (1-4): ")) - 1
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1-4): ")) - 1  

        # Verifica se a linha e coluna escolhidas estão dentro do intervalo permitido.
        if 0 <= linha <= 3 and 0 <= coluna <= 3:
            # Verifica se a posição no tabuleiro está vazia.
            if tabuleiro[linha][coluna] == " ":
                # Preenche a posição com o símbolo do jogador atual e incrementa o contador de jogadas.
                tabuleiro[linha][coluna] = jogador_atual
                jogadas += 1
            else:
                print("Essa posição já está ocupada. Tente novamente.")
                continue
        else:
            print("Linha ou coluna fora do intervalo permitido. Tente novamente.")
            continue

        # Verifica se o jogador atual venceu o jogo.
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro final.
            print(f"Jogador {jogador_atual} venceu!")
            break
        # Verifica se o jogo empatou (todas as posições preenchidas).
        elif jogadas == 16:
            imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro final.
            print("O jogo empatou!")
            break

        # Alterna o jogador atual para o próximo.
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Chama a função principal para iniciar o jogo da velha.
jogo_da_velha()