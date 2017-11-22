'''
Función de actualizar
-Entrada:
	-Matriz de booleanos
-Funcionalidad:
	-Recibe una matriz de boleanos y devuelve otra
 con los estados actualizados.
-Salida:
	-Nueva matriz
'''
import cesar
import copy

def actualizar(matriz):
	mat_act = copy.deepcopy(matriz)
	for i in range(len(matriz)):
		j = 0
		while j < len(matriz[0]):
			 mat_act = cesar.cesar(i, j, matriz)
	return mat_act
