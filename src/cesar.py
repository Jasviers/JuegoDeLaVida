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
posSubMat = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] #Bonitas tuplas a que si

def cesar(i, j, matriz):
	rangei= len(matriz) #Explicar porque mejor esto aqui y no en el bucle
	rangej= len(matriz[0])
	celVisvas=0 #Contador de celulas vivas
	#Comprobamos si existen y si estan vivas las celulas adyacentes
	for x,y in posSubMat:
		if enRango(i+x,j+y,rangei, rangej) and matriz[i+x][j+y]: #Cortocircuito Explicar porque esto esta bien
			celVisvas += 1 #Si estan vivas añadimos 1 al contador
	#Sabiendo las celulas vivas aplicamos las reglas
	if celVisvas==3:
		return True
	elif celVisvas<2 or celVisvas>3:
		return False
	else:
		return matriz[i][j]

# Funcion auxiliar que me dice si esta en rango
def enRango(i,j,rangei, rangej):
	return (i in range(rangei) and j in range(rangej))
