from jogo01_mad_libs.JogoTeca import jogar_madlibs
from jogo02_adivinha_o_número. adivinha_número import jogar_adivinha_número
from jogo3_tabuada.jogo_tabuada import jogar_tabuada
from jogo05_cara_ou_coroa.cara_ou_coroa import jogar_cara_ou_coroa
from jogo06_if.jogo_com_if import jogar_com_if
from jogo07_par_ou_impar.jogo_parou_impar import jogar_par_ou_impar
from genius import jogo_acertar_cores
while True:
  print("""
        ✴.·´¯`·.·★  🎀𝓳𝓸𝓰𝓸 𝓽𝓮𝓬𝓪🎀  ★·.·`¯´·.✴

  # ######################################################## #
  #            01- Mad Libs                                  #
  #            02- adivinha o número                         #
  #            03- tabuada                                   #                                 
  #            04- cara ou coroa                             #
  #            05- jogo com if                               #
  #            06- par ou impar
  #            07- 0 para sair                              #
  # ######################################################## #
    ************Desenvolvido por Nicolly************** """)

  escolha= int(input("Com qual jogo iremos nós divertir hoje?"))
  if escolha == 1:
    jogar_madlibs()
  elif escolha == 2:
    jogar_adivinha_número
  elif escolha == 3:
    jogar_tabuada()
  elif escolha == 4:
    jogar_cara_ou_coroa
  elif escolha == 5:
    jogar_com_if
  elif escolha == 6: 
    jogar_par_ou_impar
  elif escolha == 0:
    print("foi ótimo johar com você!!!")
    break