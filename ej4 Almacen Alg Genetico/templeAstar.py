import random
from producto import producto
from node import node
from temple import temple
from gen import gen

def templeAstar(Matrix, productos):
    ini = [0,0,0]
    buscar=[33, 1 ,3,25]
    genomas=[]

    tem=temple(100,buscar,0)

    buscar1=[37,33, 1 ,3,25,22,21,4,10,4,2,11,40]
    buscar2=[25,10,35,8]
    buscar3=[11,18,40,31,5]
    buscarList=[]
    buscarList.append(buscar1)
    buscarList.append(buscar2)
    buscarList.append(buscar3)

    fitness=0
    for buscar in buscarList:
            
        tem=temple(100,buscar,0)
        listHistorial=[]
        while(tem.condicion==False):
            nodeAct=node(ini,0,0)
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
                                        if ((Matrix[j][i]!=1)&(not [j,i] in listHistorial)): 
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
                        listHistorial=[]        
                            
            print("la cantidad de energia fue "+str(pasos))
            tem.templado(pasos)
            buscar=tem.listProductos
            
        print("el mejor orden de los productos es ")
        for ordprod in tem.listAnt:
            print(str(ordprod))

        print("La energia para estos fue: "+ str(tem.Eant))
        #input()
        fitness+=tem.Eant

    fitness=fitness/len(buscarList)
    print("el promedio de energia, o fitness total de ordenes es "+str(fitness))
    genoma=gen(productos,fitness)
    return genoma