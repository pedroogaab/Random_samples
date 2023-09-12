from random import randint

opc = ["PEDRA", "PAPEL", "TESOURA"]


escolha = opc[randint(0, 2)]

my_play = "pedra"
mp = my_play.upper().strip()

ganhou = True

print(f"voce escolheu {mp}\n")

if mp == "PEDRA" and escolha == "TESOURA":
    ...

elif mp == "PAPEL" and escolha == "PEDRA":
    ...

elif mp == "TESOURA" and escolha == "PAPEL":
    ...


elif mp == "PEDRA" and escolha == "PAPEL":
    ganhou = False

elif mp == "PAPEL" and escolha == "TESOURA":
    ganhou = False

elif mp == "TESOURA" and escolha == "PEDRA":
    ganhou = False


if mp == escolha:
    print(f"EMPATOU, o bot tambem escolheu {escolha}")
elif ganhou:
    print(f"GANHOU, o bot escolheu {escolha}")

else:
    print(f"PERDEU, o bot escolheu {escolha}")
