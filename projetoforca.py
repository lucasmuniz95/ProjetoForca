import random
palavrasFrutas = ["uva", "maça", "pera", "melancia", "laranja"]
palavrasCores = ["branco", "azul", "preto", "amarelo", "vermelho", "roxo"]
palavrasAnimais = ["cachorro", "gato", "cavalo", "vaca", "galinha"]
tentativas = 5
letrasDigitadas = []
letrasErradas = []
letrasAcertadas = []
categoria = ""
alfabeto = list("abcdefghijlmnopqrstuvxz")


def bonecoForcaCompleto():
	print('''
	
	################################
	##                            ##
	##                            ##                             
	##                         ##########
	##                            *****
	##                         *         *             
	##                        *           *
	##                         *         *
	##                            *****
	##                              *
	##                            *****
	##                          *   *    *
	##                        *     *      *
	##                      *       *        *
	##                              *
	##                            ******
	##                          *         *
	##                        *             * 
	##                      *                 *      
	
	''')

def bonecoforca4():
	print('''

		################################
		##                            ##
		##                            ##                             
		##                         ##########
		##                            *****
		##                         *         *             
		##                        *           *
		##                         *         *
		##                            *****
		##                              *
		##                            *****
		##                              *    *
		##                              *      *
		##                              *        *
		##                              *
		##                            ******
		##                          *         *
		##                        *             * 
		##                      *                 *      

		''')

def bonecoforca3():
	print('''

		################################
		##                            ##
		##                            ##                             
		##                         ##########
		##                            *****
		##                         *         *             
		##                        *           *
		##                         *         *
		##                            *****
		##                              *
		##                            *****
		##                              *    
		##                              *      
		##                              *        
		##                              *
		##                            ******
		##                          *         *
		##                        *             * 
		##                      *                 *      
		''')

def bonecoforca2():
	print('''

		################################
		##                            ##
		##                            ##                             
		##                         ##########
		##                            *****
		##                         *         *             
		##                        *           *
		##                         *         *
		##                            *****
		##                              *
		##                            *****
		##                              *    
		##                              *      
		##                              *        
		##                              *
		##                            ******
		##                                    *
		##                                      * 
		##                                        *      
		''')

def bonecoforca1():
	print('''

		################################
		##                            ##
		##                            ##                             
		##                         ##########
		##                            *****
		##                         *         *             
		##                        *           *
		##                         *         *
		##                            *****
		##                              
		##                           
		##                                  
		##                                    
		##                                     
		##                              
		##                            
		##                          
		##                        
		##                            
		''')


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

	while (categoria != "s"):
		letrasTentadas = str(input("\n\nDigite a letra que você acha que tem na palavra: "))
		letrasDigitadas.append(letrasTentadas)
		palavraSecreta = list(palavra)
		if letrasTentadas in palavra:
			print("_ ", end="")
			print("\nParabéns, você acertou uma letra")
			print("\nAs letras que você já digitou foram: ", letrasDigitadas)
			print(palavra)
		else:
			print("\nNão tem essa letra na palavra :/")
			print("\nAs letras que você já digitou foram: ", letrasDigitadas)
			tentativas -= 1
			print("\nVocê ainda tem ", tentativas, "tentativas")

		if (letrasTentadas != str):
			print("Digite uma letra")

		if (tentativas == 0):
			bonecoForcaCompleto()
			print("Fim de Jogo")
			print("A palavra era: ", palavra)
			categoria = "s"
		elif (tentativas == 1):
			bonecoforca4()
		elif (tentativas == 2):
			bonecoforca3()
		elif (tentativas == 3):
			bonecoforca2()
		elif (tentativas == 4):
			bonecoforca1()




