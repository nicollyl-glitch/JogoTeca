import os 
import time
import random

def jogo_acertar_cores():
    dicionario_de_cores = {"verde":"20",
                        "azul":"90",
                        "amarelo":"60",
                        "vermelho":"40",
                            "roxo" : "50",
                            "branco":"70"}
    lista_sequencia = []

    def limpar_tela():
        os.system("color 07")
        os.system("cls")

    limpar_tela()
    def mudar_cor(cor):
        codigo_cor = dicionario_de_cores[cor]
        os.system(f"color {codigo_cor}")
        time.sleep(1)
        limpar_tela()

    print("""                                                          
        //   ) )                                        
    //         ___       __     ( )           ___    
    //  ____  //___) ) //   ) ) / / //   / / ((   ) ) 
    //    / / //       //   / / / / //   / /   \ \     
    ((____/ / ((____   //   / / / / ((___( ( //   ) )   
            
            Repita as cores se errar
    """)
    input("Pressione ENTER para continuar")
    limpar_tela()

    lista_cores = ["verde","azul","amarelo","vermelho","roxo", "branco"]

    while 1 == 1:
        cor_aleatoria = random.choice(lista_cores)
        contado = 0
        #inserindo a cor aleaoria dentro da lista_sequencia.
        lista_sequencia.append(cor_aleatoria)

        #percorrendo a lista
        for cor_lista in lista_sequencia:
            mudar_cor(cor_lista)
    #pergunta para o usuario que cor apareceu
        print(""" 
        ########################################    
                V = VERDE
                A = AZUL
                M = AMARELO
                E = VERMELHO
                R = ROXO 
                B = BRANCO
        ########################################   
            """)
        Resposta = input("Digite a sequencia: ").upper()

        dicionario_abreviacoes ={"v" : "verde",
                                "A" : "azul",
                                "M" : "amarelo",
                                "E" : "vermelho",
                                "R" : "roxo",
                                "B" : "branco"}
        lista_resposta = []

        for letra in Resposta:
            cor = dicionario_abreviacoes.get(letra)
            lista_resposta.append(cor)
        contador = contador + 1
        #verificar se ele errou
        if lista_sequencia != lista_sequencia:
            print("você ERROU")
            print("a sequencia era:")
            print(*lista_sequencia)
            print(f"você errou na fase {contador}")
            break
        else:
            print("você acertou, vamos para a próxima fase")
            input("Aperte ENTER qundo estiver pronto")
            limpar_tela()

if __name__ == "__main__":
    jogo_acertar_cores()


