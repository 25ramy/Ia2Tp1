def backTrackingRecursive(X,D,C_P,C_M,historial,historialTiempo):

    for i in range(0,len(D)):
        var=variableMasRestringida(historial,C_P) #var se refiere a tarea asignada
        consistent=consistentValue(var,X,i,C_P,C_M,historial) #i se refiere a dominioActual
        if ((consistent==True)&(var!=-1)):
            historial.append(var)
            historialTiempo.append(i)
            backTrackingRecursive(X,D,C_P,C_M,historial,historialTiempo)
        elif((consistent==False)and(var==-1)):
            print(historial)
            print(historialTiempo)

            exit()


def most_frequent(List): 
    return max(set(List), key = List.count) 
  
def variableMasRestringida(historial,C_P):
    listNew=[]
    try:
        for i in range(0,len(C_P)):
            if(C_P[i][0] not in historial): #asigna ejemplo T3 ya q es la mas restringida
                listNew.append(C_P[i][0])
            elif(len(listNew)==0): #si no hay ningun valor x asignar empieza con las q restringen
                if(C_P[i][1] not in historial):
                    listNew.append(C_P[i][1])
                
        return most_frequent(listNew)
    except:
        print("Todos los elementos ya fueron completados en historial")

        return -1 


#Xact es el periodo actual
def consistentValue(var,X,tiempo,C_P,C_M,historial):
    estado=False
    for i in range(0,len(C_P)): #empezamos con las procedencias ya q son lo q mayor restricciones tiene
        if var == C_P[i][1]:
            if C_P[i][0] not in historial: #tiene q estar en historial, si no esta es inconsistente
                estado=False

    if ((var not in C_M[var].task) & (tiempo>=C_M[var].time)):
        C_M[var].state=True 
    
    if ((var not in C_M[var].task) & (C_M[var].state==True)): #tarea no esta terminada pero 
                                                            # maq sigue ocupada
        tiempoTask=0
        for tarea in C_M[var].task:
            tiempoTask+=X[tarea]                    
        if (tiempo-tiempoTask>=X[var]): #cuando se complete la tarea
            C_M[var].task.append(var) #variable local de tareas terminadas x maquina
            C_M[var].time=tiempo #ultimo tiempo de uso
            #C_M[var].time.append(tiempo)
            C_M[var].state=False #ya que se sumo el tiempo de dominio y se realizo la tarea
            #historial.append(var)
            estado=True
        elif(tiempo-tiempoTask<X[var]):
            C_M[var].state=False #esto se triggea a True false todo el tiempo mientras no este
                                    #completo el tiempo en Dominio

    else:
        estado=False
        
    return estado