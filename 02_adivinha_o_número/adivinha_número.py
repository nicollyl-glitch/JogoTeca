import random


print("""                                                                                                                                        
                        (                 (                            )         
  (        (  (         )\ )          )   )\ )  (    )   (          ( /(     )   
  )\   (   )\))(  (    (()/(  (    ( /(  (()/(  )\  /((  )\   (     )\()) ( /(   
 ((_)  )\ ((_))\  )\    ((_)) )\   )(_))  ((_))((_)(_))\((_)  )\ ) ((_)\  )(_))  
   !  ((_) (()(_)((_)   _| | ((_) ((_)_   _| |  (_)_)((_)(_) _(_/( | |(_)((_)_   
  | |/ _ \/ _` |/ _ \ / _` |/ _ \ / _` |/ _` |  | |\ V / | || ' \))| ' \ / _` |  
 _/ |\___/\__, |\___/ \__,_|\___/ \__,_|\__,_|  |_| \_/  |_||_||_| |_||_|\__,_|  
|__/      |___/                                                                  
""")
print(""" ####################################################
          #    1= NOOB (de 1 á 10)                            #
          #    2= Médio (de 1 á 20 )                          #
          #    3= Profissional ( de 1 á 50)                   #
          #    4= SENAI(De 1 á 200)                           #
          ####################################################
        """)  
nivel= int(input( "escoha o nível:  "))
if nivel>4:
    print("esse nivel não existe")
    #Noob

elif nivel == 1:
    escolha1 = random.randrange(0,11)

    número1 =  int(input("digite um número "))

    if número1 == escolha1:
        print("voce acertou")
    else:   
        print("voce errou")
        print(f"eu estava pensando no número {escolha1}")

#Médio
elif nivel == 2:
    escolha2= random.randrange(0,21)
    número2= int(input(" digite o número: "))

    if número2 == escolha2:
        print("voce acertou")

    else:
        print("voce errou")
        print(f"eu estava pensando no número {escolha2}")

#Profissional
elif nivel == 3:
    escolha3= random.randrange(0,51)
    numero3= int(input("digite o numero: "))

    if numero3 == escolha3:
        print("voce acertou")
    else:
        print("voce errou")
        print(f"eu estava pensando no número {escolha3}")

#SENAI
elif nivel == 4:
    escolha4= random.randrange(0,201)
    numero4= int(input("digite o numero: "))

    if numero4 == escolha4:
            print("voce acertou")
    else:
            print("voce errou")
            print(f"eu estava pensando no número {escolha4}")









