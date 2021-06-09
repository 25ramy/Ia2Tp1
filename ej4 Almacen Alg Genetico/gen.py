class gen:

    def __init__(self,individuo,fitness):
        self.__individuo = individuo
        self.__fitness = fitness
        
    def get_fitness(self):
        return self.__fitness

    def set_fitness(self, fitness):
        self.__fitness = fitness

        
    def get_individuo(self):
        return self.__individuo

    def set_individuo(self, individuo):
        self.__individuo = individuo
