# A estratégia:

# O jogo é executado em um loop enquanto game_over for False.
# O jogador é solicitado a digitar uma palavra com 5 letras.
# A entrada é convertida em maiúsculas e limitada a 5 letras.
# As chances são reduzidas em 1.
# O jogo verifica se o jogador ficou sem chances ou adivinhou corretamente a palavra.
# Se nenhuma das condições acima for atendida, o código verifica cada letra do chute do jogador e fornece as pistas corretas, incorretas e inexistentes.
# As palavras digitadas são armazenadas em palavras_digitadas.
# O teclado é exibido com letras corretas destacadas.


# Detalhamento das Estruturas:

# random: importada para gerar números aleatórios, usados para escolher uma palavra secreta aleatória da lista de palavras.
# cores: Isso permite destacar letras corretas na posição correta (verde), letras corretas na posição errada (amarelo) e letras inexistentes (fundo preto).
# palavras_frutas: Uma lista de palavras de 5 letras que podem ser usadas como palavras secretas no jogo.
# game_over: Uma variável booleana que controla o estado do jogo.
# chances: O número de tentativas que o jogador tem.
# palavras_digitadas: Uma lista para armazenar as palavras já digitadas pelo jogador.
# letras_certas: Um conjunto para armazenar as letras corretas já adivinhadas.
# teclado_layout: Uma matriz que representa o layout do teclado, agrupando letras por linhas.
# exibir_teclado: Função que exibe o teclado com letras corretas destacadas em verde.

import random  # Importa a biblioteca random para gerar números aleatórios.

reset_cor = '\033[0;0m'  # Código para redefinir a cor do texto e fundo para o padrão.
letra_inexiste = '\033[40m'     # Código para definir o fundo preto para letras inexistentes.
letra_pos_errado = '\033[43m'   # Código para definir o fundo amarelo para letras na posição errada.
letra_pos_correta = '\033[42m'  # Código para definir o fundo verde para letras na posição correta.

# Lista de palavras de 5 letras
palavras_frutas = ["sagaz","âmago","negro","êxito","termo","mexer","nobre","senso","afeto","algoz","ética","plena","mútua","tênue","fazer","assim","sutil","vigor","aquém","porém","seção","fosse","sanar","audaz","poder","ideia","cerne","inato","moral","desde","sobre","justo","muito","honra","torpe","quiçá","sonho","fútil","razão","ícone","etnia","anexo","amigo","égide","tange","lapso","expor","haver","mútuo","dengo","tempo"]

termo = random.choice(palavras_frutas).upper()  # Escolhe aleatoriamente uma palavra secreta e a converte para maiúsculas.
game_over = False  # Variável para controlar o estado do jogo.
chances = 6  # Número de chances que o jogador tem para adivinhar a palavra.
palavras_digitadas = []  # Lista para armazenar as palavras já digitadas pelo jogador.
letras_certas = set()  # Conjunto para armazenar letras corretas já adivinhadas.

# Layout do teclado
teclado_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]

# Função para exibir o teclado com letras corretas destacadas.
def exibir_teclado(acertos):
    print("Teclado:")
    for linha in teclado_layout:
        for letra in linha:
            if letra in acertos:
                print(f"{letra_pos_correta}{letra}{reset_cor} ", end='')  # Imprime letras corretas com fundo verde.
            else:
                print(f"{letra} ", end='')  # Imprime letras do teclado.
        print()

# Exibe instruções do jogo.
print("------------------------------------ INSTRUÇÕES ------------------------------------")
print("Descubra a palavra certa em 6 tentativas. Depois de cada tentativa, as peças mostram o quão perto você está da solução.")
print(letra_pos_correta + "T" + reset_cor + "URMA \nA letra " + letra_pos_correta + "T" + reset_cor + " faz parte da palavra e está na posição correta")
print("VI" + letra_pos_errado + "O" + reset_cor + "LA \nA letra " + letra_pos_errado + "O" + reset_cor + " faz parte da palavra mas em outra posição")
print("PUL" + letra_inexiste + "G" + reset_cor + "A \nA letra " + letra_inexiste + "G" + reset_cor + " não faz parte da palavra")
print("------------------------------------------------------------------------------------\n")

# Loop principal do jogo
while not game_over:
    display = []  # Lista para exibir o progresso da adivinhação.
    chute = str(input("Digite uma palavra com 5 letras: "))  # Solicita uma palavra ao jogador.
    chute = chute.upper()[:5]  # Converte a entrada para maiúsculas e limita a 5 letras.
    chances -= 1  # Reduz o número de chances restantes.

    if chances == 0:
        print("Acabaram as chances")
        print(f"A palavra correta era: {letra_pos_correta}{termo}{reset_cor}\n")
        game_over = True  # Encerra o jogo se o jogador ficar sem chances.

    elif chute == termo:
        print("Parabéns, você acertou o termo!")
        print(letra_pos_correta + chute + reset_cor)
        game_over = True  # Encerra o jogo se o jogador adivinhar corretamente a palavra.

    else:
        i = 0
        for c in chute:
            display.append(c)
            if c not in termo:
                display[i] = letra_inexiste + display[i] + reset_cor  # Marca letras inexistentes.
            elif c == termo[i]:
                display[i] = letra_pos_correta + display[i] + reset_cor  # Marca letras corretas na posição correta.
                letras_certas.add(c)  # Adiciona a letra correta à lista de letras certas.
            else:
                display[i] = letra_pos_errado + display[i] + reset_cor  # Marca letras corretas na posição errada.
            i += 1

        palavras_digitadas.append("".join(display))  # Adiciona a palavra digitada à lista de palavras digitadas.

        print("Palavras já digitadas:")
        for palavra in palavras_digitadas:
            print(palavra)
        print("\n")

    exibir_teclado(letras_certas)  # Exibe o teclado com letras corretas destacadas.
