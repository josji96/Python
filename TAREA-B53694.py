import random



#Clases, metodos y variables
opcion_anterior =0
N=0
M=0
matrices=[]
matrices_2=[]



opcion=0

class ficha():
    valor=0
    nom=''

def crear_arreglo(M):
    arreglo = []
    for i in range(0,M):
        pieza=ficha()
        pieza.valor=random.randint(0,10)
        
        if pieza.valor<=3:
            pieza.nom = 'P'
        elif pieza.valor>3 and pieza.valor<=6:
            pieza.nom = 'L'
        else:
            pieza.nom = 'T'
        arreglo.append(pieza)
    return arreglo


def crear_matriz(N,M):
    matriz=[]
    for i in range(0,N):
        matriz.append(crear_arreglo(M))
    return matriz



def menu():
    intento=True
    print("Presione 1 para inicializar una partida")
    print("Presione 2 para imprimir la primera matriz")
    print("Presione 3 para imprimir la segunda matriz")
    print("Presione 4 para jugar y determinar ganador")
    print("Presione 5 para carga la ultima partida jugada")
    print("Presione 6 para salir del juego")
    while intento==True:
        try:
            opcion=int(input("Ingrese la opcion que desea\n"))
            if opcion>0 and opcion<=6:
                intento=False
            else:
                print("La opcion digitada no esta dentro de las opciones")
        except ValueError:
            print("La entrada detectada no es correcta, por favor intentelo de nuevo")
    return opcion


def opcion_1(N,M):
    resultado=[]
    matriz_1=crear_matriz(N,M)
    matriz_2=crear_matriz(N,M)
    print("AMBAS MATRICES INICIALIZADAS")
    print("")
    resultado.append(matriz_1)
    resultado.append(matriz_2)
    return resultado

def opcion_2(matriz_1):
    print("La matriz 1 contiene:")
    for i in range(0,len(matriz_1)):
        for j in range(0,len(matriz_1[i])):
            if j<len(matriz_1[i])-1:
                print(str(matriz_1[i][j].valor)+str(matriz_1[i][j].nom), end="-")
            else:
                print(str(matriz_1[i][j].valor)+str(matriz_1[i][j].nom))
    return 0

def opcion_3(matriz_2):
    print("La matriz 2 contiene:")
    for i in range(0,len(matriz_2)):
        for j in range(0,len(matriz_2[i])):
            if j<len(matriz_2[i])-1:
                print(str(matriz_2[i][j].valor)+str(matriz_2[i][j].nom), end="-")
            else:
                print(str(matriz_2[i][j].valor)+str(matriz_2[i][j].nom))
    return 0

def opcion_4(matriz_1,matriz_2,opcion_anterior,N,M):
    resultado=[]
    if opcion_anterior!=1:
        matriz_1=crear_matriz(N,M)
        matriz_2=crear_matriz(N,M)
        matriz_resultado=crear_matriz(N,M)
        opcion_anterior=1
        opcion_4(matriz_1,matriz_2,opcion_anterior,N,M)
    else:
        matriz_resultado=crear_matriz(N,M)
        contador_matriz1=0
        contador_matriz2=0
        contador_emp=0
        nombreArchivo = "savep.csv"
        archivo=open(nombreArchivo, "w")
        try:
            for i in range(0,len(matriz_1)):
                for j in range(0,len(matriz_1[i])):
                    if matriz_1[i][j].nom == 'P' and matriz_2[i][j].nom == 'T':
                        matriz_resultado[i][j]=1
                    elif matriz_1[i][j].nom == 'P' and matriz_2[i][j].nom == 'L':
                        matriz_resultado[i][j]=2
                    elif matriz_1[i][j].nom == 'L' and matriz_2[i][j].nom == 'P':
                        matriz_resultado[i][j]=1
                    elif matriz_1[i][j].nom == 'L' and matriz_2[i][j].nom == 'T':
                        matriz_resultado[i][j]=2
                    elif matriz_1[i][j].nom == 'T' and matriz_2[i][j].nom == 'L':
                        matriz_resultado[i][j]=1
                    elif matriz_1[i][j].nom == 'T' and matriz_2[i][j].nom == 'P':
                        matriz_resultado[i][j]=2
                    else:
                        if matriz_1[i][j].valor > matriz_2[i][j].valor:
                            matriz_resultado[i][j]=1
                        elif matriz_1[i][j].valor < matriz_2[i][j].valor:
                            matriz_resultado[i][j]=2
                        else:
                            matriz_resultado[i][j]=0


            for i in range(0, len(matriz_resultado)):
                for j in range(0,len(matriz_resultado[i])):
                    if matriz_resultado[i][j] == 1:
                        contador_matriz1+=1
                    elif matriz_resultado[i][j] == 2:
                        contador_matriz2+=1
                    elif matriz_resultado[i][j] == 0:
                        contador_emp+=1
            if contador_matriz1!=0:
                print("Para esta partida los resultados son:")
                print("")
                print("Matriz1 tiene un total de " + str(contador_matriz1) + "victorias.")
                print("Matriz2 tiene un total de " + str(contador_matriz2) + "victorias.")
                print("Se presentaron " + str(contador_emp) + "empates")
                print("")
            else:
                print("Se necesitan inicializar matrices")
                print("")

            for i in range(0,len(matriz_resultado)):
                linea=matriz_resultado[i]
                archivo.write(str(linea)+"\n")
        except UnboundLocalError:
            print("Las matrices no se inicializaron correctamente")

        archivo.close()
    resultado.append(matriz_1)
    resultado.append(matriz_2)
    return resultado
  

def opcion_5():
    nombreArchivo="savep.csv"
    archivo=open(nombreArchivo,"r")
    for linea in archivo:
        print(linea)
    archivo.close()



    return 0

def opcion_6():
    print("Finalizando partida")
    print("Gracias por jugar")

    return 0




#Bloque principal


while opcion!= 6:
    opcion=menu()
    print("")

    if opcion==1:
        ingreso=False
        while ingreso==False:
            try:
                N=int(input("Ingrese el numero de filas que desea"))
                if N>5 and N<=10:
                    ingreso=True
                else:
                    print("El numero de filas digitado no es correcto")
            except ValueError:
                print("El valor digitado no es correcto")

        ingreso=False
        while ingreso==False:
            try:
                M=int(input("Ingrese el numero de columnas que desea"))
                if M>5 and M<=10:
                    ingreso=True
                else:
                    print("El numero de columnas digitado no es correcto")
            except ValueError:
                print("El valor digitado no es correcto")
        ingreso=False
        matrices=opcion_1(N,M)
        matriz_1=matrices[0]
        matriz_2=matrices[1]
        opcion_anterior=1

    elif opcion==2:
        if opcion_anterior!=1:
            print("Necesita inicializar matrices")
        else:
            opcion_2(matriz_1)
        print("")

    elif opcion==3:
        if opcion_anterior!=1:
            print("Necesita inicializar matrices")
        else:
            opcion_3(matriz_2)
        print("")
    
    elif opcion==4:
        try:
            matrices_2=opcion_4(matriz_1,matriz_2,opcion_anterior,N,M)
            matriz_1=matrices_2[0]
            matriz_2=matrices_2[1]
        except NameError:
            print("Se necesita inicializar matrices para la primera partida jugada")
        

    elif opcion==5:
        try:
            print("Los resultados de la ultima partida guardada son:")
            opcion_5()
            opcion_anterior=5
        except FileNotFoundError:
            print("Archivo no encontrado")
        print("")
    elif opcion==6:
        opcion_6()