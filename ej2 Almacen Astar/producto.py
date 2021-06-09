from node import node

class producto:

    def __init__(self,node,name):
        self.__node = node
        self.__name = name

    def get_node(self):
        return self.__node

    def set_node(self, node):
        self.__node = node

        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name