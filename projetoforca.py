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
#print('Olá, seja bem vindo!\n')
#print('Esse é o nosso jogo da forca')
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
	#              Se quiser sair do jogo              #
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
#catFrutas = "1"
#catCores = "2"
# catAnimais = "3"
# sair = 's'



print("A palavra contem essas letras abaixo:")


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





print("A palavra é:", palavra)


