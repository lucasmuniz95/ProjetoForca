import random
palavrasFrutas = ["uva", "maça", "pera", "melancia", "laranja"]
palavrasCores = ["branco", "azul", "preto", "amarelo", "vermelho", "roxo"]
palavrasAnimais = ["cachorro", "gato", "cavalo", "vaca", "galinha" ]
chances = 0
tentativas = 5
letrasDigitadas = []
letrasErradas = []
letrasAcertadas = []
categoria = ""
alfabeto = list("abcdefghijlmnopqrstuvxz")

def menuCategorias():
	print('''
	Digite [1] para Frutas 
	Digite [2] para Cores 
	Digite [3] para Animais
	
	Se quiser sair do jogo              
	
	Digite [S] para Sair 
				''')

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


while (categoria != "s"):
	categoria = input('\nPor favor, escolha sua categoria: ').lower() .strip()
	if (categoria == '1'):
		categoria = "Frutas"
	elif (categoria == '2'):
		categoria = "Cores"
	elif (categoria == "3"):
		categoria = "Animais"
	elif (categoria == "s"):
		print("\nJogo Finalizado!")
		break
	else:
		print("\nCategoria Invalida")
		menuCategorias()
		continue


	print('\nA categoria escolhida foi:',categoria)
	print('\nA palavra é: ',end="")

	palavra = "nao selecionada"
	if (categoria == "Frutas"):
		palavra = (random.choice(palavrasFrutas))
	elif (categoria == "Cores"):
		palavra = (random.choice(palavrasCores))
	elif (categoria == "Animais"):
		palavra = (random.choice(palavrasAnimais))

	for letra in palavra:
		print('_ ', end="")


	while True:
		letrasDigitadas = input("\n\nDigite a letra que você acha que tem na palavra: ")
		if (letrasDigitadas == alfabeto):
			print(palavra + letra)
			print("\nAs letras que você já digitou foram: ", letrasDigitadas, ",")
		else:
			print("\nVocê precisa digitar uma letra")
			continue




