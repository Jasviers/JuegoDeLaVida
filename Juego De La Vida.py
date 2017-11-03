matriz=[["F", "F", "F", "F", "F"],
	["F", "F", "T", "F", "F"],
	["F", "F", "T", "F", "F"],
	["F", "F", "F", "F", "F"],
	["F", "F", "F", "F", "F"]]


def caesar(i, t):
        matriz[i][t]
        if((i==0) & (t==0)):
                for i in range(2):
                        for t in range(2):
                                print(matriz[i][t])
        elif((i==0) & (t==4)):
                t=3
                for i in range(2):
                        for t in range(2):
                                print(matriz[i][t])
        elif((i==4) & (t==4)):
                i=3
                t=3
                for i in range(2):
                        for t in range(2):
                                print(matriz[i][t])
        elif((i==4) & (t==0)):
                i=3
                for i in range(2):
                        for t in range(2):
                                print(matriz[i][t])
        elif(i==0):
                if(t==1):
                        for i in range(2):
                                for t in range(3):
                                        print(matriz[i][t])
                elif(t==2):
                        t=1
                        for i in range(2):
                                for t in range(3):
                                        print(matriz[i][t])
                else:
                        t=2
                        for i in range(2):
                                for t in range(3):
                                        print(matriz[i][t])
        elif(i==4):
                if(t==1):
                        for i in range(2):
                                for t in range(3):
                                        print(matriz[i][t])
                elif(t==2):
                        t=1
                        for i in range(2):
                                for t in range(3):
                                        print(matriz[i][t])
                else:
                        t=2
                        for i in range(2):
                                for t in range(3):
                                        print(matriz[i][t])
        elif(t==0):
                if(i==1):
                        for i in range(3):
                                for t in range(2):
                                        print(matriz[i][t])
                elif(i==2):
                        for i in range(3):
                                for t in range(2):
                                        print(matriz[i][t])
                else:
                        for i in range(3):
                                for t in range(2):
                                        print(matriz[i][t])
        elif(t==4):
                if(i==1):
                        t=3
                        for i in range(3):
                                for t in range(2):
                                        print(matriz[i][t])
                elif(i==2):
                        t=3
                        for i in range(3):
                                for t in range(2):
                                        print(matriz[i][t])
                else:
                        t=3
                        for i in range(3):
                                for t in range(2):
                                        print(matriz[i][t])
        else:
                i=1
                t=1
                for i in range(3):
                        for t in range(3):
                                print(matriz[i][t])

                
def recorrido(matriz):
	for i in range(5):
		for t in range(5):
			caesar(i, t)
