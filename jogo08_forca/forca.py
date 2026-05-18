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
    resposta = input("Digite UMA letra: ").upper()
    if resposta != 1:
        print("Eu disse UMA letra")
        resposta2 = input("Digite UMA letra: ")
pergunta = perguntar_letra()    

def jogar_forca():
#Tela inicial do jogo
  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        

    
      
    
     
            

    