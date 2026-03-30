import random


print("""        _____                                 _____                      
  / ____|                               / ____|                     
 | |     __ _ _ __ __ _    ___  _   _  | |     ___  _ __ ___   __ _ 
 | |    / _` | '__/ _` |  / _ \| | | | | |    / _ \| '__/ _ \ / _` |
 | |___| (_| | | | (_| | | (_) | |_| | | |___| (_) | | | (_) | (_| |
  \_____\__,_|_|  \__,_|  \___/ \__,_|  \_____\___/|_|  \___/ \__,_|
                                                                      
                                                                    """)




escolha= input("primeiro jogador: escolha cara ou coroa: ")
escolhacomputador= random.choice([ "cara" , "coroa"])
if escolha == escolhacomputador:
    print(" vc ganhou")
    print(f"caiu {escolhacomputador}")
elif escolha != escolhacomputador:
    print("voce perdeu")
    print(f"caiu {escolhacomputador}")

