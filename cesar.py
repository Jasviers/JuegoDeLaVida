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
def esRango(i,j,rangoi,rangoj):
	return i in range(rangoi) and range(rangoj)

def cesar(i, j, matriz):

	elementosCercanos = [[-1, -1][-1, 0][0, -1][1, 1][1, 0][0, 1]]
	rangoi = len(matriz)
	rangoj = len(matriz)
	celulasVivas = 0

	for x,y in elementosCercanos:
		if esRango(i, j, )
