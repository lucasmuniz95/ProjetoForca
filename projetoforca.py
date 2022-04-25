import random
palavrasFrutas = ["uva", "maça", "pera", "melancia", "laranja"]
palavrasCores = ["branco", "azul", "preto", "amarelo", "vermelho", "roxo"]
palavrasAnimais = ["cachorro", "gato", "cavalo", "vaca", "galinha" ]
chances = 0
tentativas = 5
letrasDigitadas = []
letrasErradas = []
letrasAcertadas = []
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
<<<<<<< HEAD

=======
>>>>>>> cd8e27729b5338dcd57e662043e6cf540f66a258
def menu():
	print('''
	 >>>>>>>>>>>>         Uniesp         >>>>>>>>>>>>>>
	#               Centro Universitario               #
	#                                                  #
	#                   Categorias                     #
	#                                                  #
	#         [1] - Frutas                             #
	#         [2] - Cores                              #
	#         [3] - Animais                            #
	#                                                  #            
	#             Se quiser sair do jogo               #
	#                                                  #                    
	#         [S] - Sair                               # 
	#                                                  #
	#    Grupo:                                        #
	#    Daniela Lima                                  #
	#    Eduargo Gouveia                               #
	#    Fernanda Mota                                 #
	#    Jullyana Maciel                               # 
	#    Larissa Maia                                  #
	#    Lucas Muniz                                   #
	#    Maira Nathalya                                #
	#                                                  # 
	####################################################       
			''')
menu()
categoria = input('Por favor, escolha sua categoria: ')

palavrasFrutas = (random.choice(palavrasFrutas))
palavrasCores = (random.choice(palavrasCores))
palavrasAnimais = (random.choice(palavrasAnimais))
<<<<<<< HEAD
=======



print("A palavra contem essas letras abaixo:")
>>>>>>> cd8e27729b5338dcd57e662043e6cf540f66a258

print("\nA palavra é:")

for letra in palavrasFrutas:
	if (categoria == "1"):
		palavra = palavrasFrutas
		print('-', end="")
	elif (categoria == "2"):
		palavra = palavrasCores
		print('-', end="")
	elif (categoria == "3"):
		palavra = palavrasAnimais
		print('-', end="")
	elif (categoria == "s"):
		print("Jogo Finalizado")
		break;
	else:
		print("Você não escolheu nenhuma categoria")
		break;


<<<<<<< HEAD
print(f"\n{palavra}")
=======



print("A palavra é:", palavra)
>>>>>>> cd8e27729b5338dcd57e662043e6cf540f66a258


