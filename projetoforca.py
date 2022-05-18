import random
import os

palavrasFrutas = ['abacate', 'abacaxi', 'banana', 'goiaba', 'laranja', 'manga', 'maça', 'melancia', 'pera', 'bergamota', 'uva', 'durian']
palavrasCores = ['azul', 'verde', 'vermelho', 'preto', 'amarelo', 'violeta', 'laranja', 'branco', 'rosa', 'marrom']
palavrasAnimais = ['cachorro', 'gato', 'cavalo', 'vaca', 'galinha', 'peixe', 'coelho', 'papagaio', 'jaguatirica', 'sucuri', 'beluga']
tentativas = 6
letrasDigitadas = []
letrasErradas = []
letrasAcertadas = []
categoria = ""
alfabeto = list("abcdefghijklmnopqrstuvwxyzáéíóúãõâêîôûç")
letrasChutadas = ""
palavra = ""

def bonecoforcaComemorando():
		print('''
	
	################################
	##                            ##
	##                            ##                             
	##                         ##########
	##
	##
	##
	##
	##
	##
	##
	##
	##                            *****
	##                         *         *             
	##                        *           *
	##                   *     *         *    *
	##                      *     *****     *
	##                        *     *     *
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

def bonecoforca5():
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
			##                         *    *    *
			##                       *      *      *
			##                     *        *        *
			##                              *
			##                            ******
			##                                   *  
			##                                     *  
			##                                       *         

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
		##                         *    *    *
		##                       *      *      *
		##                     *        *        *
		##                              *
		##                            ******
		##                                    
		##                                      
		##                                              

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
		##                              *   * 
		##                              *     * 
		##                              *       * 
		##                              *
		##                            ******
		##                                   
		##                                      
		##                                     
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
		##                                   
		##                                      
		##                                             
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
	#    Eduardo Gouveia                               #
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


	palavra = "nao selecionada"
	if (categoria == "Frutas"):
		palavra = (random.choice(palavrasFrutas))
	elif (categoria == "Cores"):
		palavra = (random.choice(palavrasCores))
	elif (categoria == "Animais"):
		palavra = (random.choice(palavrasAnimais))


	while (palavra != "s"):
		print('\n\n\nA palavra é: ', end="",)
		for letra in palavra:
			if letra in letrasAcertadas:
				print(" ",letra, " ", end="")
			else:
				print(' _ ', end="")
		print("\n\nLetras informadas: ", letrasDigitadas)
		print("         Corretas: ", letrasAcertadas)
		print("          Erradas: ", letrasErradas)
		print("\nCategoria: ", categoria)

		letrasChutadas = input("\n\n\n\nDigite a letra que você acha que tem na palavra: ") .lower()
		if letrasChutadas not in alfabeto:
			print("\nCaractere invalido, digite uma letra")
			continue
		if letrasChutadas in letrasDigitadas:
			print("\nEssa letra já foi digitada\n\n")
			continue
		else:
			letrasDigitadas.append(letrasChutadas)

		if (letrasChutadas in alfabeto) and (letrasChutadas in palavra):
			print("\n                   ACERTOOOOU!!!!!""\n")
			letrasAcertadas.append(letrasChutadas)
			acertou = True
			for letra in palavra:
				if letra not in letrasAcertadas:
					acertou = False
			if acertou:
				bonecoforcaComemorando()
				print("\nParabéns, você fugiu da forca e ganhou o jogo!!")
				print("\nA palavra é:", palavra)
				while True:
					jogarNovamente = input(
						"\nDeseja jogar novamente? (Digite [S] para SIM/Digite [N] para NÃO): ").lower().strip()
					if jogarNovamente == "s" or jogarNovamente == "n":
						if jogarNovamente == "s":
							os.system('cls')
							menu()
							letrasDigitadas = []
							letrasAcertadas = []
							letrasErradas = []
							tentativas = 6
							palavra = "s"
							break
						elif jogarNovamente == "n":
							print("\nJogo Finalizado!!")
							palavra = "s"
							categoria = "s"
							break
					else:
						print("Caractere Invalido, digite ou S ou N")
						continue
		elif (letrasChutadas in alfabeto) and (letrasChutadas not in palavra):
			letrasErradas.append(letrasChutadas)
			print("\n                   ERROU :( :(""\n")
			tentativas -= 1
			if (tentativas == 0):
				bonecoForcaCompleto()
				print("Fim de Jogo")
				print("A palavra era: ", palavra)
				while True:
					jogarNovamente = input("\nDeseja jogar novamente? (Digite [S] para SIM/Digite [N] para NÃO): ").lower().strip()
					if jogarNovamente == "s" or jogarNovamente == "n":
						if jogarNovamente == "s":
							os.system('cls')
							menu()
							letrasDigitadas = []
							letrasAcertadas = []
							letrasErradas = []
							tentativas = 6
							palavra = "s"
							break
						elif jogarNovamente == "n":
							print("\nJogo Finalizado!!")
							palavra = "s"
							categoria = "s"
							break
					else:
						print("Caractere Invalido, digite ou S ou N")
						continue
			if (tentativas == 1):
				bonecoforca5()
				print("\nVocê ainda tem ", tentativas, "tentativas")
			elif (tentativas == 2):
				bonecoforca4()
				print("\nVocê ainda tem ", tentativas, "tentativas")
			elif (tentativas == 3):
				bonecoforca3()
				print("\nVocê ainda tem ", tentativas, "tentativas")
			elif (tentativas == 4):
				bonecoforca2()
				print("\nVocê ainda tem ", tentativas, "tentativas")
			elif (tentativas == 5):
				bonecoforca1()
				print("\nVocê ainda tem ", tentativas, "tentativas")

