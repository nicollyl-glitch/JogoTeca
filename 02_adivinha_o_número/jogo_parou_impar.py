
import random     

pergunta= input("par ou impar? ")
if pergunta == "par":
    print("eu sou impar")
if pergunta == "impar": 
    print("eu sou par")
escolha = random.randrange(0,11)
numero1= int(input("escolha um número: "))
print(f"minha escolha:{escolha}")
conta= (escolha + numero1) % 2 

if numero1 > 10:
    print(" voce não tem essa quantidade de dedos!!!")
    exit()

if conta == 0 and escolha =="par":
    print("Voce ganhou")
elif conta == 0 and escolha =="impar":
    print("voce perdeu")
elif conta != 0 and escolha =="impar":
     print("Voce ganhou")
else:
    print("Voce perdeu")