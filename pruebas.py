import actualizar
import cesar
import os
import time
import itertools
import numpy as np
import genMat

def visualizacion(elem):
    if elem:
        return "*"
    else:
        return "_"

dim = int(input("¿Que tamaño tendra el juego?\n"))
mat = genMat.genMat(dim)


while True:
    mat = actualizar.actualizar(mat)
    os.system("clear")
    flatten = lambda x : itertools.chain(*x)
    #Fuck bucles eso es de noobs
    print(np.array(list(map(visualizacion,flatten(mat)))).reshape(dim,dim))
    time.sleep(1)
