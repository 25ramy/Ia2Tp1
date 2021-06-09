from machine import Machine
from cspStuart import backTrackingRecursive

X=[5,15,10,30] #T0=5m T1=15m T2=10m T3=30, en esta caso seria X, nuestro conjunto de variables fin.
limit=0
D=[]
for i in range(0,len(X)):
    limit=limit+X[i] #limit max tiempo de tarea, no podria durar mas q la ssuma por separado
    #incluso si tenemos en cuenta q cada tarea usan todas las misma maquina

for i in range(0,limit):
    D.append(i) #Dominio de nuestro CSP

C_P=[[1,2],[3,0],[3,2]] #C restricciones precedencias T1 antes q T2,
                                        # T3 antes q T0 y T3 antes q T2

M1=Machine("M1")
M2=Machine("M2")
                  #restricciones maquinas
C_M=[M1,M1,M2,M2] #T0 y T1 usa M1 T3 y T4 usa M2
historial=[]
historialTiempo=[]
backTrackingRecursive(X,D,C_P,C_M,historial,historialTiempo)


