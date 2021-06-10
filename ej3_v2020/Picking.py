class Picking(object):                  #Objetos que el Temple Simulado analizará. Cada uno es un posible camino para buscar los k productos
    def __init__(self, orden):
        self.orden_productos = orden    #debe recibir una lista
        #
        self.padre = None
        #
        self.E = 10000 
