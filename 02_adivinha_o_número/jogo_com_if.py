import random
escolhacomputador= random.choice(["pedra" ,"papel" , "tesoura"])


escolhadapessoa= input(" Digite : pedra, pepel ou tesoura: ")
print(f" minha escolha foi:{escolhacomputador}")
if escolhacomputador == escolhadapessoa:
    print(" escolhemos o mesmo item ")

elif escolhadapessoa == "papel" and escolhacomputador == "tesoura":
    print("voce  perdeu, tesoura corta papel")
elif escolhadapessoa == "tesoura" and escolhacomputador == "papel":
    print("voce ganhou, tesoura corta papel")
elif escolhadapessoa == "pedra" and escolhacomputador == "papel":
    print("voce perdeu, papel enbrulha a pedra  ")
elif escolhadapessoa == "papel" and escolhacomputador == "pedra":
    print("voce perdeu, papel embrulha pedra")
elif escolhadapessoa == "tesoura" and escolhacomputador == "pedra":
    print(" voce perdeu, pedra bate na tesoura ")
elif escolhadapessoa == "pedra" and escolhacomputador == "tesoura":
    print("voce ganhou, pedra bate na tesoura")


