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
	mat_act=copy.deepcopy(matriz)
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			mat_act[i][j]=cesar.cesar(i,j, matriz)
	return mat_act
