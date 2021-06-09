class Machine():
    def __init__(self,name):
        self.name=name
        self.state=False #True=Ocupada
        self.time=0
        self.task=[] #Historial maquina

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
    
    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def get_task(self):
        return self.__task

    def set_task(self, task):
        self.__task = task