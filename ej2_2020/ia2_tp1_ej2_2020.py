
#CLASES USADAS

from Nodo import Nodo

class Busqueda_Aestrella(object):                                                                 #4
    def __init__(self):  
        self.lista_abiertos = []
        self.lista_cerrados = []     #lista de nodos visitados
        self.nodos= []
        self.almacen_x = None   
        self.almacen_y = None   


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
                self.nodos.append(Nodo(x, y, alcanzable, False))                                            #6
        self.comienzo = self.obtener_nodo(x_inic, y_inic)                                            #7
         
        self.final = self.obtener_nodo(x_objetivo, y_objetivo)                                       #8
        
   

    def ordenar_segun_Fn(self,lista):     #   Usando BubbleSort                                      #10
        l= len(lista)

        # Recorremos todos los elementos
        for i in range(l):
            #print("i es: ",i)
 
            # Pero los ultimos "i" elementos ya estan en el el lugar correcto, asi que...
            for j in range(0,l-i-1):
                if lista[j].Fn > lista[j+1].Fn:
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]


    def obtener_nodo(self, x, y):
        return self.nodos[x * self.almacen_y + y]
    # obtengo un nodo de la lista TOTAL de elementos del almacen


    def obtener_Hn(self, nodo):
            return abs(nodo.x - self.final.x) + abs(nodo.y - self.final.y)


    def obtener_adyacentes(self, nodo):                                                         #12
        nodos = []
        #
        for i in range (nodo.x -1 , nodo.x +1 +1):
            for j in range (nodo.y -1 , nodo.y +1 +1):
                if (i != nodo.x) or (j != nodo.y):
                    if not ( (i < 0) or (j < 0) or (i > self.almacen_x-1) or (j > self.almacen_y-1) ):
                        
                        nodos.append(self.obtener_nodo(i , j))
        return nodos
        
        #Manera poco eficiente:
        """
        if nodo.x < self.almacen_x-1:
            nodos.append(self.obtener_nodo(nodo.x +1 , nodo.y))
        if nodo.y > 0:
            nodos.append(self.obtener_nodo(nodo.x , nodo.y -1))
        if nodo.x > 0:
            nodos.append(self.obtener_nodo(nodo.x -1 , nodo.y))
        if nodo.y < self.almacen_y-1:
            nodos.append(self.obtener_nodo(nodo.x , nodo.y +1))
        #
        if (nodo.x > 0) and (nodo.y > 0):
            nodos.append(self.obtener_nodo(nodo.x -1 , nodo.y -1))
        if (nodo.x > 0) and (nodo.y < self.almacen_y-1 ):
            nodos.append(self.obtener_nodo(nodo.x -1 , nodo.y +1))
        if (nodo.x < self.almacen_x-1) and (nodo.y > 0 ):
            nodos.append(self.obtener_nodo(nodo.x+1 , nodo.y-1))
        if (nodo.x < self.almacen_x-1 ) and (nodo.y < self.almacen_y-1): 
            nodos.append(self.obtener_nodo(nodo.x +1 , nodo.y +1))
        #
        return nodos
        """


    def presentar_camino(self):                                                                 #11
            nodo= self.final
            camino= [(nodo.x, nodo.y)]
            print("\n\nCamino (posiciones x,y de cada paso):")
            if nodo != self.comienzo:   #Se agrega esta excepcion para el prevenir errores en aquellos casos
                                        #en los cuales se inicia frente al lugar del producto.
                while nodo.padre is not self.comienzo:
                    nodo= nodo.padre
                    camino.append((nodo.x, nodo.y))
                camino.append((x_inic , y_inic))

            camino.reverse()
            print (camino)
           

    def nodo_actual(self, adyac, nodo):
            adyac.Gn= nodo.Gn + 1
            adyac.Hn= self.obtener_Hn(adyac)
            adyac.padre= nodo
            adyac.Fn= adyac.Hn + adyac.Gn
    

    def Resolver(self):                                                                                         #9
        self.lista_abiertos.append(self.comienzo)

        while len(self.lista_abiertos):
            
            self.ordenar_segun_Fn(self.lista_abiertos)                                                          #10

            nodo= self.lista_abiertos.pop(0)
            
            if nodo not in (self.lista_cerrados):
                self.lista_cerrados.append(nodo)
            # Agregamos el nodo a la Lista Cerrada para no recorrerlo de nuevo
            
            if nodo is self.final:
                self.presentar_camino()                                                                         #11
                break
            
            nodos_adyac= self.obtener_adyacentes(nodo)                                                          #12
            for adyac in nodos_adyac:
                if adyac.alcanzable and adyac not in self.lista_cerrados:
                    if (adyac.Fn, adyac) in self.lista_abiertos:
                        if adyac.Gn > nodo.Gn + 1:
                            self.nodo_actual(adyac, nodo)
                    else:
                        self.nodo_actual(adyac, nodo)
                        self.lista_abiertos.append(adyac)


#Respecto al metodo "__init__":
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=43&codigo=43&inicio=30
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=44&codigo=44&inicio=30




#CREACION DEL ALMACEN   #1
cant_est_x= int(input("Cuantos estantes de 2x8 tiene el deposito a lo ancho (Oeste a Este) del deposito?\n"))
ancho= 3*cant_est_x+1 #suponiendo que los corredores tienen el ancho de 1 cuadricula

pasillo_horizontal=[]
for x in range(1,ancho+1):
    pasillo_horizontal.append(int(0)) #creamos corredores horizontales vacios para colocar entre estantes

cant_est_y=int(input("Cuantos estantes de 2x8 tiene el deposito en profundidad (Norte a Sur) del deposito?\n"))
prof= 5*cant_est_y-1 #suponiendo que en que los estantes estan pegados a la paredes Norte y Sur


almacen=[] #lista vacia para la matriz del almacen: cada lista agregada como elemento en el siguiente paso será una de las filas de la matriz
for y in range(1,prof+1):
    if (y%5)==0:
        almacen.append(pasillo_horizontal)
    else:
        ancho_en_areas=[]
        for x in range(1,ancho+1):
            if (x%3)==1:
                ancho_en_areas.append(int(0))
            else:
                ancho_en_areas.append(int(1))
        almacen.append(ancho_en_areas)
        
print("\n""Matriz que representa los estantes del Almacen:\n",almacen)
"""Con las entradas "3" y "2", se obtiene la lista de listas:
[[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0]]"""
#ej:
#almacen[3][1]=8 #posicion x=1,y=3...    Con 2x2 estantes, x llega hasta 7 (ancho) y y llega hasta 9 (prof)... Se cambia en todas las "ancho_en_x"

print("\nSe supone en este modelado que el ancho de los corredores es el de 1 celda espacio")


#ESPACIOS DEL ALMACEN   #2
contad_vertical=1
fila_vertical_de_estantes=0

for x in range(0,ancho):
    if ((x+1)%3) == 0:
        fila_vertical_de_estantes+= 1
        for y in range(0,prof):
            if (almacen[y][x]) >= 1:
                almacen[y][x-1]= contad_vertical
                almacen[y][x]= contad_vertical+1
                contad_vertical+= 2
                                                                                                   # print ("\n""\nA ver el almacen...",almacen)
        contad_vertical= (8*int(cant_est_y))*(fila_vertical_de_estantes) + 1
        
print ("\n""Matriz que representa el Almacen con los espacios numerados:\n",almacen)




#CONDICIONES Y OBJETIVOS    #3
x_inic= int(input("\n\nIngrese las coord. de la pos. inicial, teniendo en cuenta que el area frente al Espacio 1 esta ubicada en x:0,y:0\n\nIngrese la coord x: "))
y_inic= int(input("Ingrese la coord y: "))
print("Comienzo:", x_inic,",",y_inic)

if  x_inic>ancho-1 or x_inic<0 or y_inic>prof or y_inic<0:
    print("\nLa posicion inicial no puede estar fuera del almacen.\n")
else:
    if almacen[y_inic][x_inic] > 0:
        print("\nLa posicion inicial no puede estar dentro de un estante.\n")
    else:

        producto= int(input("\nIngrese el numero del espacio del producto que desea buscar: "))
        for y in range(0,prof):
            for x in range(0,ancho):
                if almacen[y][x]==producto:
                    if (almacen[y][x]%2) == 0:
                        x_objetivo= x+1
                        y_objetivo= y
                    else:
                        x_objetivo= x-1
                        y_objetivo= y
        print("\nEn la matriz del Almacen, el espacio ubicado frente al producto buscado esta en la columna", x_objetivo,"y la fila", y_objetivo)
        print("Ese espacio es el destino final y, para llegar a el,");
        print("Sí se permite el movimiento oblicuo.");




#RESOLUCION

        busqueda1= Busqueda_Aestrella()                                                                               #4

        busqueda1.definir_almacen(almacen, ancho, prof, x_inic, y_inic, x_objetivo, y_objetivo)                       #5

        busqueda1.Resolver()                                                                                          #9    
#aca tiraba error:definir_almacen() missing 1 required positional argument: 'y_objetivo'. Respuesta:
#a)Para invocar el método nuevo_articulo(), debes hacerlo sobre un objeto, y no sobre la clase. Eso es lo que te está fallando ya que cuando
# haces objeto.metodo(parametros), Python lo traduce a Clase.metodo(objeto, parametros), haciendo que el objeto en cuestión pase a ser self
# dentro del método. Al llamarlo como Clase.metodo(parametros), que es lo que has hecho, faltaría un parámetro en la llamada (python no puede
# saber cuál y supone que es el último, precio, pero en realidad era el primero, self).
#b)Cuando "invocas" una clase, así Clase(), se ejecuta su constructor y se retorna un objeto de esa clase. En tu caso, ya que la clase se llama
# Manejo_stock, el objeto creado podría llamarse manejador, en lugar de articulo1, pues no es un artículo. Esto hace más comprensible el código.


#END