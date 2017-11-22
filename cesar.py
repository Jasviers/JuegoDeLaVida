'''
Función Cesar
-Entrada:
	-Matriz de booleanos
	-Entero de posicion i
	-Entero de posicion j
-Funcionalidad:
	-Recibe una matriz de boleanos, y una posicion (i,j)
analiza las posiciones alrededor de la posicion dentro de la
matriz aplicando las reglas del juego devuelve true o false
-Salida:
	-Booleano

'''
alrededor = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
def cesar(i, j, matriz):
	 celVivas = 0; #Cuenta las celulas vivas alrededor de la que estamos estudiando
	 for x[0] + i and x[1] + j in alrededor:
		 if alrededor == True:
		 	celVivas += 1 #Necesito mierda de la buena coniio
	#Reglas Mágico-fantásticas________________________________________________________
	if celVivas < 2 or celVivas > 3:
		#Muere
	elif celVivas == 3:
		#Vive
	else:
		#Se queda como está
