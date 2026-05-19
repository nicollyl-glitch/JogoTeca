import os
import random
def limpar_tela():
    """ Função limpar tela do prompt"""
    os.system ("cls")

def escolher_palavra() -> str:
    """Escolhe e retorna uma aplavra aleatória"""
    palavras = ["melancia",
                "casa",
                "godofredo",
                "raul",
                "diagnostico",
                "metacarpo"
                ]
    palavra_aleatória = random.choice(palavras)
    #retorne a palavra para quem chamou a função
    return palavra_aleatória
    print(palavra_aleatória)

def desenhar_forca(erro:int):
    """Imprime o desenho da forca dependendo da quantikdade de erros"""
    limpar_tela()
    if erro == 0:
        print("""
                    ------
                    |     |
                    |    
                    |
                    |
                    |
    """)
    if erro == 1:
        print("""    ------
                    |     |
                    |    (- -)
                    |
                    |
                    |
    """)
    if erro == 2:
        print("""    ------
                    |     |
                    |    (- -)
                    |      |
                    |
                    |
    """)
        
    if erro == 3:
        print("""    ------
                    |     |
                    |    (- -)
                    |      |
                    |      |
                    |
    """)
        
    if erro == 4:
            print("""    ------
                        |     |
                        |    (- -)
                        |    - |
                        |      |
                        |       
        """)

    if erro == 5:
            print("""    ------
                        |     |
                        |    (- -)
                        |    - | -
                        |      |
                        |       
        """)

    if erro == 6:
            print("""    ------
                        |     |
                        |    (- -)
                        |    - | -
                        |      |
                        |     / 
        """)
            
    if erro == 6:
            print("""    ------
                        |     |
                        |    (- -)
                        |    - | -
                        |      |
                        |     / 
        """)
    
    if erro == 7:
            print(r"""    ------
                        |     |
                        |    (- -)
                        |    - | -
                        |      |
                        |     / \
        """)
            
    if erro == 8:
            print(r"""    ------
                        |     |
                        |    (x x)
                        |    - | -
                        |      |
                        |     / \
        """)

def gerar_tracos(palavra:str) -> list :
    """Gera e retorna uma lista contendo underlines na mesma quantidade que letras das palavras"""
    
    quantidade_de_letras  = len(palavra)
    tracos = []
    # usando while e contador
    contador = 0
    while contador < quantidade_de_letras:
          tracos.append("-")
          contador = contador + 1
    return tracos


def perguntar_letra() ->str:
    resposta = input("Digite UMA letra: ").lower()
    while len(resposta) != 1:
        print("Eu disse UMA letra")
        input("Digite UMA letra: ")
    return resposta    

def jogar_forca():
    #Tela inicial do jogo

        print("""   
        ____     ___  ___ ___                 __ __  ____  ____   ___     ___        ____      _____   ___   ____      __   ____ 
        |    \   /  _]|   |   |               |  |  ||    ||    \ |   \   /   \      /    |    |     | /   \ |    \    /  ] /    |
        |  o  ) /  [_ | _   _ |     _____     |  |  | |  | |  _  ||    \ |     |    |  o  |    |   __||     ||  D  )  /  / |  o  |
        |     ||    _]|  \_/  |    |     |    |  |  | |  | |  |  ||  D  ||  O  |    |     |    |  |_  |  O  ||    /  /  /  |     |
        |  O  ||   [_ |   |   |    |_____|    |  :  | |  | |  |  ||     ||     |    |  _  |    |   _] |     ||    \ /   \_ |  _  |
        |     ||     ||   |   |                \   /  |  | |  |  ||     ||     |    |  |  |    |  |   |     ||  .  \\     ||  |  |
        |_____||_____||___|___|                 \_/  |____||__|__||_____| \___/     |__|__|    |__|    \___/ |__|\_| \____||__|__|
                                                                                                                            """)
        input("Aperte ENTER para começar")
        contador_de_erro = 0
        palavra_escolhida = escolher_palavra()
        lista_tracos = gerar_tracos(palavra_escolhida)
        lista_tentativas = []
        while True:
            limpar_tela()
            desenhar_forca(contador_de_erro)   
            lista_tentativas.append(letra_chutada)
            print(f"você errou:{lista_tentativas}") 
            print(*lista_tracos)
            #Verificando se ele ganhou
            if "_" not in lista_tracos:
                print("Parabéns, você ganhou!!!")
                break
            letra_chutada = perguntar_letra()
            if letra_chutada  not in palavra_escolhida:
                contador_de_erro += 1
                if contador_de_erro == 9 :
                 print("VOCÊ PERDEU")
                 print(f"A palavra era {palavra_escolhida}")        
                 break    
            if letra_chutada in palavra_escolhida:
                contador = 0
                for  letra_palavra in palavra_escolhida:
                    if letra_palavra == letra_chutada:
                         lista_tracos[contador] = letra_chutada
                    contador += 1
                
            
            


if __name__ == "__main__": 
    jogar_forca()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        

    
      
    
     
            

    