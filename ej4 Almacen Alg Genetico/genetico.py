import random
from producto import producto
from node import node
from temple import temple
from gen import gen
from templeAstar import templeAstar
from operator import itemgetter
import copy

ini = [0,0,0] # celda donde empezamos
print("La persona comienza en el espacio (inicio):")
print(ini)

x= int(input("Ingrese Tamaño del almacen a lo ancho\n"))

y=int(input("Ingrese Tamaño del almacen a lo largo\n"))

poblacion=5
genomas=[]

for pob in range(0, poblacion+1):
    cont=0
    productos=[]
    ordenProducto=random.sample(range(42), 42)
    Matrix = [[0 for i in range(x)] for j in range(y)] 
    for j in range(0, y): #de 0 a y-1
        for i in range(0, x):
            if (((j%5)==0) or (j==(y-1))):
                Matrix[j][i]=0
            else:
                if((i%3)==0):
                    Matrix[j][i]=0        
                else:
                    Matrix[j][i]=1
                    nod1=node([j,i],0,100000000)
                    prod1=producto(nod1,ordenProducto[cont]) # se le asocia el nodo y el nombre
                    productos.append(prod1)
                    cont=cont+1

    genoma=templeAstar(Matrix,productos)
    genomas.append(genoma)

k=0.35


for x in range(0, len(genomas)):
    for y in range(0, len(genomas)):
        if(genomas[y].get_fitness()>genomas[x].get_fitness()):
            aux=genomas[y]
            genomas[y]=genomas[x]
            genomas[x]=aux

for gen1 in genomas:
    print("productos: ")
    for prod1 in gen1.get_individuo():
        print(prod1.get_name())
    print("fitness es: "+str(gen1.get_fitness()))

input()
#poblacion=round(poblacion*k)

while(poblacion>1):    
    puntosCorte=random.sample(range(42), 2) #cruce de orden
    sorted(puntosCorte)
    pos1=puntosCorte[0]
    pos2=puntosCorte[1]
    #individuo1=list(genomas[0].get_individuo()) #.copy()
    #individuo2=list(genomas[1].get_individuo()) #.copy()
    individuo1=[]
    individuo2=[]
    norep1=[]
    norep2=[]
    genomas2=[]
    individuos=[]
    for x in range(0,round(poblacion-1)):
        #try:
            prod1=copy.deepcopy(genomas[x].get_individuo()) #.copy()
            prod2=copy.deepcopy(genomas[x+1].get_individuo()) #.copy()
            individuo1=copy.deepcopy(prod1) #.copy()
            individuo2=copy.deepcopy(prod2) #.copy()

            print("prod1 antes de cruzamiento")     
            for i in range(0, len(prod1)):
                print(prod1[i].get_name())

            for i in range(pos1,pos2):
                norep1.append(prod1[i].get_name()) # elementos q no se deben repetir
                norep2.append(prod2[i].get_name())
                individuo1[i].set_name(prod2[i].get_name())
                individuo2[i].set_name(prod1[i].get_name())


            #cruce de orden
            cont=0
            for i in range(1, len(prod1)+1):
                if(not prod1[i-1].get_name() in norep2):
                    if((pos2+i)<len(prod1)):
                        individuo1[pos2+i].set_name(prod1[i-1].get_name())
                    else:
                        if (not (cont==pos1)):
                            individuo1[cont].set_name(prod1[i-1].get_name())
                            cont+=1
            cont=0    
            for i in range(1, len(prod2)+1):
                if(not prod2[i-1].get_name() in norep1):
                    if((pos2+i)<len(prod2)):
                        individuo2[pos2+i].set_name(prod2[i-1].get_name())
                    else:
                        if (not (cont==pos1)):
                            individuo2[cont].set_name(prod2[i-1].get_name())
                            cont+=1
                

            #Mutacion x intercambio
            puntosMutar=random.sample(range(42), 2) 
            aux=individuo1[puntosMutar[0]].get_name()
            individuo1[puntosMutar[0]].set_name(individuo1[puntosMutar[1]].get_name())
            individuo1[puntosMutar[1]].set_name(aux)
            
            aux=individuo2[puntosMutar[0]].get_name()
            individuo2[puntosMutar[0]].set_name(individuo2[puntosMutar[1]].get_name())
            individuo2[puntosMutar[1]].set_name(aux)


            print("individuo post cruzamiento y mutacion")     
            for i in range(0, len(individuo1)):
                print(individuo1[i].get_name())
            input()
            print("individuo2 post cruzamiento y mutacion")     
            for i in range(0, len(individuo2)):
                print(individuo2[i].get_name())
            
            individuos.append(individuo1)
            individuos.append(individuo2)
            
        #except IndexError as error:
        #    print()

    
    for ind in individuos:
        #genoma=templeAstar(Matrix,ind)
        genomas2.append(templeAstar(Matrix,ind))
    genomas.clear()
    genomas=copy.deepcopy(genomas2)
    for x in range(0, len(genomas)):
        for y in range(0, len(genomas)):
            if(genomas[y].get_fitness()>genomas[x].get_fitness()):
                aux=genomas[y]
                genomas[y]=genomas[x]
                genomas[x]=aux

    poblacion=round(poblacion*k)

individuo1=genomas[0].get_individuo().copy()
for i in range(0, len(individuo1)):
    print(individuo1[i].get_name())
print("el mejor valor de fitness es: "+str(genomas[0].get_fitness()))