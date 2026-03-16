import random 
numero1= random.randrange(0,21)
numero2=random.randrange(0,21)
print(f"calcule {numero1} x {numero2}")
resultado= numero1 * numero2
resposta= int(input("digite a resposta: "))
if resposta == resultado:
    print(f"voce acertou, o resultado é: {resultado}" )
else:
    print("voce errou, tente de novo")
