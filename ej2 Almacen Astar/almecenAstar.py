from producto import producto
from node import node

ini = [0,0,0] # celda donde empezamos
print("La persona comienza en el espacio (inicio):")
print(ini)

x= int(input("Ingrese Tamaño del almacen a lo ancho\n"))

y=int(input("Ingrese Tamaño del almacen a lo largo\n"))
cont=1
productos=[]
#ordenProducto=random.sample(range(42), 42)
Matrix = [[0 for i in range(x)] for j in range(y)] 
for j in range(0, y): #de 0 a y-1
    for i in range(0, x):
        if (((j%5)==0) or (j==(y-1))):
            Matrix[j][i]=0
        else:
            if((i%3)==0):
                Matrix[j][i]=0        
            else:
                Matrix[j][i]=cont
                nod1=node([j,i],0,100000000)
                prod1=producto(nod1,cont) # se le asocia el nodo y el nombre
                #print(cont)
                productos.append(prod1)
                cont=cont+1

print(Matrix)
buscar=[]
p1=int(input("Ingrese el primer producto a buscar (casilla de inicio)\n"))
p2=int(input("Ingrese el segundo producto a buscar (casilla de fin)\n"))
buscar.append(p1)
buscar.append(p2)
for prod in productos:
    if (prod.get_name()==buscar[0]):
        nodeAct=prod.get_node()

listHistorial=[]
condEncontrado=False
while(condEncontrado==False):
    #nodeAct=node(ini,0,0)
    pasos=0
    for prodAbuscar in buscar:#empiaza A* producto x producto
        for prods in productos:
            if(prodAbuscar==prods.get_name()): #si el producto existe lo va a buscar
                #busqueda A*
                fin=prods.get_node().get_pos()
                finy=fin[0]
                finx=fin[1]
                finLista=[]
                
                for i in range(finx-1, finx+2):
                        for j in range(finy-1, finy+2):
                            finLista.append([j,i])
                            

                act=nodeAct.get_pos()
                acty=act[0]
                actx=act[1]
                #print(acty)
                #print(actx)
                #while no este en la casilla final
                while not ([acty,actx] in finLista):
                    act=nodeAct.get_pos()
                    acty=act[0]
                    actx=act[1]

                    yf=fin[0]
                    xf=fin[1]
                    gn=0
                    # proximos nodos a evaluar
                    nodes=[]
                    for i in range(actx-1, actx+2):
                        for j in range(acty-1, acty+2):
                            try:        
                                if ((Matrix[j][i]==0)&(not [j,i] in listHistorial)): 
                                    #si no es un obstaculo va a explorar

                                    gn=gn+1
                                    hn=((xf-i)**2+(yf-j)**2)**(0.5) # dist linea recta
                                    #hn=abs(i-xf)+abs(j-yf)
                                    fn=gn+hn # valor representativo
                                    nod1=node([j,i],gn,hn)
                                    nodes.append(nod1) # Lista de proximos nodos posibles
                            except IndexError as error:
                                print()
                    #ordenar nodo para ver fn mas chico
                    min=1000000000000
                    for nod1 in nodes:
                        if (nod1.get_hn()<min):
                            min=nod1.get_hn()
                            nodeAct=nod1
                    print(nodeAct.get_pos())
                    listHistorial.append(nodeAct.get_pos())
                    pasos+=1
                    
                print("producto "+str(prods.get_name())+" pickeado")
                print("cantidad de pasos recorridos en almacen entre productos: "+ str(pasos))
                condEncontrado=True
                listHistorial=[]        
    
