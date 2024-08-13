#Vamos construir um jogo de forca. O programa escolherá
#aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
#secreta será representada por espaços em branco, um para cada letra
#da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
#tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
#na palavra secreta, ela será revelada nas posições correspondentes.
# Se  a letra não estiver na palavra, uma mensagem de erro deverá ser
# informada. Após um número máximo de erros, o jogador perde.
# O jogo continua até que o jogador adivinhe a palavra ou exceda o número
# máximo de tentativas.  Dica: Você precisará importar uma biblioteca para resolver esse exercício
import random

def escolher_palavra():
    palavras = ["python", "programacao", "jogo", "womaker", "desafio", "computador", "tecnologia"]
    return random.choice(palavras)

def jogar():
    palavra_secreta = escolher_palavra()
    letras_corretas = ["_" for _ in palavra_secreta]
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao jogo da forca!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
    print(" ".join(letras_corretas))

    while tentativas > 0 and "_" in letras_corretas:
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1:
            print("Por favor, insira apenas uma letra.")
            continue

        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if tentativa in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_corretas[index] = letra
            print("Correto!")
        else:
            tentativas -= 1
            letras_erradas.append(tentativa)
            print(f"Errado! Você tem {tentativas} tentativas restantes.")
        
        print(" ".join(letras_corretas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")

    if "_" not in letras_corretas:
        print("Parabéns! Você adivinhou a palavra!")
    else:
        print(f"Você perdeu! A palavra era '{palavra_secreta}'.")

# Iniciar o jogo
jogar()
