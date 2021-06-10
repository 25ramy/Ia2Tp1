class Espacio(object):
    def __init__(self, x, y, alcanzable):
        self.alcanzable = alcanzable
        #
        self.x = x
        self.y = y
        #
        self.padre = None
        #
        self.Gn = 0  #Gn es el costo de moverse al siguiente espacio
        self.Hn = 0  #Hn es la Heuristica... En este caso, la Distancia de Manhattan es apropiada
        self.Fn = 0

