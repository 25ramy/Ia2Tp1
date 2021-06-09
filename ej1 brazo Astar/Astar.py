import random
from node import node
    
grados = 180  # grados se refiere a la discretizacion, en este caso 180°, es decir de 2 en 2

xi=random.randint(0,grados)
yi=random.randint(0,grados)
zi=random.randint(0,grados)
ui=random.randint(0,grados)
vi=random.randint(0,grados)
wi=random.randint(0,grados)


xf=random.randint(0,grados)
yf=random.randint(0,grados)
zf=random.randint(0,grados)
uf=random.randint(0,grados)
vf=random.randint(0,grados)
wf=random.randint(0,grados)


ini = [xi,yi,zi,ui,vi,wi] # celda donde empezamos
fin = [xf,yf,zf,uf,vf,wf] #celda destino
print("EL robot comienza en el espacio reticular (inicio):")
print(ini)
print("EL robot debe llegar al espacio reticular (meta):")
print(fin)
print("")
density=round(grados*50) #densidad de obstaculos, muy grande para evaluar complejidad
obstcl = [i for i in range(density)]
print(density)
for i in range(density):
    a=random.randint(0,grados)
    b=random.randint(0,grados)
    c=random.randint(0,grados)
    d=random.randint(0,grados)
    e=random.randint(0,grados)
    f=random.randint(0,grados)
    for obs1 in obstcl:
        if([a,b,c,d,e,f]!=ini and [a,b,c,d,e,f]!=fin and [a,b,c,d,e,f]!=obs1): #un obstaculo no puede
            obstcl[i]= [a,b,c,d,e,f]                      #ser ni el inicio ni el final
            break
        else:                                       #ni tampoco otro obstaculo
            i=i-1

nodeAct=node(ini,0,0)
     

#while no este en la casilla final
while (nodeAct.get_pos()!=fin):
    act=nodeAct.get_pos()
    actx=act[0]
    acty=act[1]
    actz=act[2]
    actu=act[3]
    actv=act[4]
    actw=act[5]
    gn=nodeAct.get_gn()
    # proximos nodos a evaluar
    nodes=[]
    for i in range(actx-1, actx+2):
        for j in range(acty-1, acty+2):
            for k in range(actz-1, actz+2):
                for l in range(actu-1, actu+2):
                    for m in range(actv-1, actv+2):
                        for n in range(actw-1, actw+2):
                            if not [i,j,k,l,m,m] in obstcl: #si no es un obstaculo va a explorar
                                gn=nodeAct.get_gn()+1
                                hn=(((xf-i)**2)+((yf-j)**2)+((zf-k)**2)+((uf-l)**2)+((vf-m)**2)+((wf-n)**2))**(0.5) # dist linea recta-dist euclidiana
                                fn=gn+hn # valor representativo
                                nod1=node([i,j,k,l,m,n],gn,hn)
                                nodes.append(nod1) # Lista de proximos nodos posibles

    
    #ordenar nodo para ver fn mas chico
    min=grados*grados*grados*grados*grados #valor grande para comparar distancia
    for nod1 in nodes:
    # print(nod1.get_hn())
        if (nod1.get_hn()+nodeAct.get_gn()<min):
            min=nod1.get_hn()+nodeAct.get_gn()
            nodeAct=nod1
    
    print(nodeAct.get_pos())




                
