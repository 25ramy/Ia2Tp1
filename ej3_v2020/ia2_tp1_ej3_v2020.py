

# Optimizacion Hibrida:  Temple Simulado + A*
#     "Orden de retiro de los productos" + "Camino para llegar a cada producto"

import random
import math

#CLASES Y FUNCIONES USADAS

from Espacio import Espacio
from Picking import Picking

class Busqueda_Aestrella(object):                              
    def __init__(self):  
        self.lista_abiertos = []
        self.lista_cerrados = []#set()     #lista de espacios visitados
        self.espacios= []
        
        self.almacen_x = None
        self.almacen_y = None   

        self.caminos_sumados=0


    # "funcion main" - Es el paso inicial basico de mi programa                                                                                 #5
    def definir_almacen(self, almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo):  
        self.almacen_y = prof   
        self.almacen_x = ancho
        for x in range(self.almacen_x):
            for y in range(self.almacen_y):
                if almacen[y][x] == 0:
                    alcanzable = True
                else:
                    alcanzable = False
                self.espacios.append(Espacio(x, y, alcanzable)) #creo todos los nodos "espacio" del almacen, todas las posiciones posibles
                
        self.comienzo = self.obtener_espacio(x_inic, y_inic)                                   
        self.final = self.obtener_espacio(x_objetivo, y_objetivo)                              
   

    def ordenar_segun_Fn(self,lista):     #   Usando BubbleSort                                   
        l= len(lista)
        for i in range(l):   # Recorremos todos los elementos
            # Pero los ultimos "i" elementos ya estan en el el lugar correcto, asi que...
            for j in range(0,l-i-1):
                if lista[j].Fn > lista[j+1].Fn:
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]


    def obtener_espacio(self, x, y):
        return self.espacios[x * self.almacen_y + y]
    # obtengo 1 espacio de la lista TOTAL de elementos del almacen


    def obtener_Hn(self, espacio):
            return abs(espacio.x - self.final.x) + abs(espacio.y - self.final.y)


    def obtener_adyacentes(self, espacio):                                                         
        espacios = []
    #Movimiento Axial:
        for i in range (espacio.x -1 , espacio.x +1 +1):
            for j in range (espacio.y -1 , espacio.y +1 +1):
                if (i != espacio.x) or (j != espacio.y):                                                   #si no es el espacio mismo...
                    if ((i == espacio.x) or (j == espacio.y)):                                             #si no es un espacio diagonal...
                        if not ( (i < 0) or (j < 0) or (i > self.almacen_x-1) or (j > self.almacen_y-1) ): #si no excede los limites del almacen...
                        
                            espacios.append(self.obtener_espacio(i , j))
                            #obtengo un espacio de la lista TOTAL de elementos del almacen y lo agrego a la lista "espacios"
        return espacios

    #Movimiento Diagonal:
    """
        for i in range (espacio.x -1 , espacio.x +1 +1):
            for j in range (espacio.y -1 , espacio.y +1 +1):
                if (i != espacio.x) or (j != espacio.y):
                    if not ( (i < 0) or (j < 0) or (i > self.almacen_x-1) or (j > self.almacen_y-1) ):
                        
                        espacios.append(self.obtener_espacio(i , j))
        return espacios"""  


    def espacio_actual(self, adyac, espacio):
            adyac.Gn = espacio.Gn + 1
            adyac.Hn = self.obtener_Hn(adyac)
            adyac.padre = espacio   #El espacio (nodo) con el que trabajabamos se convierte en el "padre" --> Lista enlazada
            adyac.Fn = adyac.Hn + adyac.Gn


    def presentar_camino(self):                                                                
            espacio = self.final
            camino = [(espacio.x, espacio.y)]
            print("\nSubCamino(posiciones x,y):")
            if espacio != self.comienzo:                   #Se agrega esta excepcion para el prevenir errores en aquellos casos en los cuales se inicia frente al lugar del producto.
                while espacio.padre is not self.comienzo:
                    espacio = espacio.padre
                    camino.append((espacio.x, espacio.y))
                camino.append((x_inic , y_inic))

            camino.reverse()
            print (camino)
            extension= len(camino)-1
            print ("La extensión de este camino es: ", extension)
            self.caminos_sumados= extension
           

    def sumando_caminos(self):
        return self.caminos_sumados
    

    def Resolver_Astar(self):                                                                                         
        self.lista_abiertos.append(self.comienzo)

        while len(self.lista_abiertos):
            
            self.ordenar_segun_Fn(self.lista_abiertos)                                                          

            espacio= self.lista_abiertos.pop(0) #saca el elemento de la lista "para verlo"      #Tomo 1 "nodo espacio" para trabajar con El
            
            if espacio not in (self.lista_cerrados):
                self.lista_cerrados.append(espacio) # Agregamos el espacio a la Lista Cerrada para no recorrerlo de nuevo
            
            if espacio is self.final:
                self.presentar_camino()                                                                         
                break
            
            espacios_adyac= self.obtener_adyacentes(espacio)    #obtengo una lista de nodos adyacentes                                                     
            for adyac in espacios_adyac:
                if adyac.alcanzable and adyac not in self.lista_cerrados:
                    if (adyac.Fn, adyac) in self.lista_abiertos:
                        if adyac.Gn > espacio.Gn + 1:
                            self.espacio_actual(adyac, espacio)
                    else:
                        self.espacio_actual(adyac, espacio)
                        self.lista_abiertos.append(adyac)





def estado_actual(estado_vecino, estado):
    estado_vecino.padre = estado   #El estado (nodo) con el que trabajabamos se convierte en el "padre" --> Lista enlazada
     
 
def picking_vecino(lista):
    #Se elige el vecino aleatoriamente. Para ser considerado un estado vecino, solo puede diferir del actual en 1 permutacion
    aux= random.randint(0,len(lista)-1)
    aux2= random.randint(0,len(lista)-1)
    while aux == aux2:
        aux2= random.randint(0,len(lista)-1)
    num=lista[aux]
    num2=lista[aux2]
    lista[aux]=num2
    lista[aux2]=num
    return lista


def Camino_Astar(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo, camino_total):
    camino_entre_productos= Busqueda_Aestrella()                                                                               
    camino_entre_productos.definir_almacen(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo)                      
    camino_entre_productos.Resolver_Astar()
    camino_total+= camino_entre_productos.sumando_caminos()
    return camino_total






#CREACION DEL ALMACEN  
cant_est_x= 2   #   int(input("Cuantos estantes de 2x8 tiene el deposito a lo ancho (Oeste a Este) del deposito?\n"))
ancho= 3*cant_est_x+1 #suponiendo que los corredores tienen el ancho de 1 cuadricula

pasillo_horizontal= []
for x in range(1,ancho+1):
    pasillo_horizontal.append(int(0)) #creamos corredores horizontales vacios para colocar entre estantes

cant_est_y= 3    #   int(input("Cuantos estantes de 2x8 tiene el deposito en profundidad (Norte a Sur) del deposito?\n"))
prof= 5*cant_est_y-1 #suponiendo que en que los estantes estan pegados a la paredes Norte y Sur


almacen=[] #lista vacia para la matriz del almacen: cada lista agregada como elemento en el siguiente paso será una de las filas de la matriz
for y in range(1,prof+1):
    if (y%5)==0:
        almacen.append(pasillo_horizontal)
    else:
        ancho_en_areas= []
        for x in range(1, ancho+1):
            if (x%3) == 1:
                ancho_en_areas.append(int(0))
            else:
                ancho_en_areas.append(int(1))
        almacen.append(ancho_en_areas)
        
print("Almacen:\n", almacen)
print("\nSe supone que el ancho de los corredores es el de 1 celda espacio")




#ESPACIOS DEL ALMACEN   
contad_vertical= 1
fila_vertical_de_estantes= 0

for x in range(0,ancho):
    if ((x+1)%3) == 0:
        fila_vertical_de_estantes+= 1
        for y in range(0,prof):
            if (almacen[y][x])>=1:
                almacen[y][x-1]= contad_vertical
                almacen[y][x]= contad_vertical+1
                contad_vertical+=2
                                                                                                   # print ("\n""\nA ver el almacen...",almacen)
        contad_vertical= (8*int(cant_est_y))*(fila_vertical_de_estantes) + 1
        
print ("\n""\nAlmacen con espacios numerados:",almacen)




#CONDICIONES Y OBJETIVOS    
#x_inic= int(input("\nIngrese las coord. de la pos. inicial, teniendo en cuenta que el area frente al Espacio 1 esta ubicada en x:0,y:0\n\nIngrese la coord x: "))
#y_inic= int(input("Ingrese la coord y: "))
x_inic= 0
y_inic= 0
x_origen= x_inic;
y_origen= y_inic;
print("Comienzo:", x_inic, ",", y_inic)

lista_prod= [];
xs_objetivos= [];
ys_objetivos= [];


if  x_inic>ancho-1 or x_inic<0 or y_inic>prof or y_inic<0:
    print("\nLa posicion inicial no puede estar fuera del almacen.\n")
else:
    if almacen[y_inic][x_inic] > 0:
        print("\nLa posicion inicial no puede estar dentro de un estante.\n")
    else:
        cant_prod= int(input("\nIngrese la cantidad de productos distintos que desea buscar: "))
        for k in range(0,cant_prod):
            print("\nIngrese el numero del espacio del producto", k, "que desea buscar: ");
            lista_prod.append(int(input()));
        print("\nLista de productos:",lista_prod);

        #Presentacion de los lugares objetivos:
        for k in range(0,cant_prod):
                for y in range(0,prof):
                    for x in range(0,ancho):
                        if almacen[y][x] == lista_prod[k]:
                            if (almacen[y][x]%2)==0:
                                xs_objetivos.append(x+1)
                                ys_objetivos.append(y)
                            else:
                                xs_objetivos.append(x-1)
                                ys_objetivos.append(y)
        
        for k in range(0,cant_prod):
            print("\nEn la matriz del Almacen, el espacio ubicado frente al producto", lista_prod[k], "esta en la fila", ys_objetivos[k],"y la columna", xs_objetivos[k])
        print("\nEstos espacios son los destinos finales y, para recorrer el almacen y llegar a ellos,");
        print("NO se permiten movimientos oblicuos");
        print("\nInicio del Temple:\n")


        

#RESOLUCION
        t= 0
        Tinic= 4000
        Temperatura= Tinic
        
        random.shuffle(lista_prod)

        estado= Picking(lista_prod)     #actual <-- HACER-NODO(ESTADO-INICIAL[problema])

    #Inicio del temple:
        while Temperatura > 0.1:
            t+= 1 
            print("iteracion t=",t)
            deltaE= 0
            Emejor= 0
            Temperatura= Temperatura/(pow(2, 0.5))  
            
        #inicio picking 1
            print("\n\n\nMejor camino hasta ahora:")
            print("Se recogeran en este orden:", estado.orden_productos)   #Muestra la lista de picking que se probara
            camino_total= 0          #Utilizado para sumar los caminos mas cortos entre cada producto (se usa para A*)
            x_inic= x_origen
            y_inic= y_origen
            xs_objetivos= [];       #Reinicio de los arrays que contienen las posiciones x y y de cada espacio
            ys_objetivos= [];       #correspondiente a cada producto ingresado
            for k in range(0,cant_prod):
                for y in range(0,prof):
                    for x in range(0,ancho):
                        if almacen[y][x] == estado.orden_productos[k]:
                            if (almacen[y][x]%2)==0:
                                xs_objetivos.append(x+1);
                                ys_objetivos.append(y);
                            else:
                                xs_objetivos.append(x-1);
                                ys_objetivos.append(y);        
          
            for k in range(0,cant_prod):
                x_objetivo= xs_objetivos[k];
                y_objetivo= ys_objetivos[k];
                
                camino_total= Camino_Astar(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo, camino_total)
              

                x_inic= xs_objetivos[k];
                y_inic= ys_objetivos[k];

            x_objetivo= x_origen;   #VUELTA A CASA
            y_objetivo= y_origen;
            
            #Se realiza un ultimo recorrido, para volver a la posicion de origen:
            camino_total= Camino_Astar(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo, camino_total)
            
            
            estado.E= camino_total            
            E1= camino_total
            print("\n El mejor camino total recorrido hasta ahora tiene una extension de:", camino_total, "\n")
            #fin del picking 1


        #Creacion del estado Vecino:
            listaaux= estado.orden_productos.copy()
            orden_vecino= picking_vecino(listaaux) #devuelve un "orden de picking" vecino aleatorio
            vecino= Picking(orden_vecino)
            estado_actual(vecino,estado)    #El estado actual se convierte en el padre del estado vecino 
            
            
        #inicio picking 2 (Vecino)
            print("\n\n\nVecino: Se recogeran en este orden:", vecino.orden_productos)   #Muestra la lista de picking que se probara
            camino_total= 0
            x_inic= x_origen
            y_inic= y_origen
            xs_objetivos= [];
            ys_objetivos= [];        
            for k in range(0, cant_prod):
                for y in range(0, prof):
                    for x in range(0,ancho):
                        if almacen[y][x] == vecino.orden_productos[k]:
                            if (almacen[y][x]%2) == 0:
                                xs_objetivos.append(x+1);
                                ys_objetivos.append(y);
                            else:
                                xs_objetivos.append(x-1);
                                ys_objetivos.append(y);
        
            for k in range(0,cant_prod):

                x_objetivo= xs_objetivos[k];
                y_objetivo= ys_objetivos[k];

                camino_total= Camino_Astar(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo, camino_total)
                

                x_inic= xs_objetivos[k];
                y_inic= ys_objetivos[k];

            x_objetivo= x_origen;   #VUELTA A CASA
            y_objetivo= y_origen;
            
            
            camino_total= Camino_Astar(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo, camino_total)


            vecino.E= camino_total
            E2=camino_total
            print("\n El camino total recorrido por su vecino aleatorio tiene una extension de:", camino_total, "\n")
            #fin del picking 2

            deltaE= E2-E1   #La "Energia" del Vecino menos la del Estado Actual
            #print("deltaE:",deltaE)
            #print("T:",Temperatura)
            Emejor=E1
            if deltaE <= 0:
                estado= vecino
                Emejor= E2
                #print("Se eligio el vecino")
            else:
                prob=(math.exp(-deltaE/Temperatura))
                #print("prob",prob)
                rand=(random.uniform(0, 1))
                if rand <= prob:
                    estado= vecino
                    Emejor= E2
                    #print("Se eligio el vecino")

        #Saliendo del bucle, se imprime el mejor resultado:
        print("\n\n\nEl mejor camino se obtiene con el picking", estado.orden_productos, ", y tiene una extension de:", Emejor)
        print("\nPara verlo en detalle, suba hasta el proximo -Mejor camino hasta ahora-")
        print("Se tardo", t, "iteraciones en llegar a El.\n")

#END