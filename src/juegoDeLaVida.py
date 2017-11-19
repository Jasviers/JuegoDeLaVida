from copy import deepcopy
import numpy as np
from random import randint
from os import system
from itertools import chain
from time import sleep

class JuegoDeLaVida:

    def __init__(self):
        self.dim = int(input("¿Que tamaño tendra el juego?\n"))
        self.mat = self.__genMat()
        self.posSubMat = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        self.celVisvas = 0

    def actualizar(self):
        mat_act = deepcopy(self.mat)
        for i in range(self.dim):
            for j in range(self.dim):
                self.celVisvas=0
                mat_act[i][j]=self.cesar(i,j)
        self.mat = mat_act

    def cesar(self,i, j):
    	#Comprobamos si existen y si estan vivas las celulas adyacentes
        for x,y in self.posSubMat:
            if self.__enRango(i+x,j+y) and self.mat[i+x][j+y]: #Cortocircuito Explicar porque esto esta bien
                self.celVisvas += 1 #Si estan vivas añadimos 1 al contador
    	#Sabiendo las celulas vivas aplicamos las reglas
        if self.celVisvas==3:
            return True
        elif self.celVisvas<2 or self.celVisvas>3:
            return False
        else:
            return self.mat[i][j]

    def representar_term(self):
        flatten = lambda x : chain(*x)
        visualizacion = lambda x : '*' if x else '_'
        while True:
            self.actualizar()
            system("clear")
            print(np.array(list(map(visualizacion,flatten(self.mat)))).reshape(self.dim,self.dim))
            sleep(1)

    # Funcion auxiliar que me dice si esta en rango
    def __enRango(self,i,j):
    	return (i in range(self.dim) and j in range(self.dim))

    def __genMat(self):
        array = np.ones((self.dim*self.dim), dtype = bool)
        rand = lambda x : randint(0,1) > 0
        return list(np.array(list(map(rand, array))).reshape(self.dim, self.dim))



if __name__=='__main__':
    juego = JuegoDeLaVida()
    juego.representar_term()
