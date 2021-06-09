import random
import math

class temple():
    def __init__(self, temperatura, listProductos,Eant):
        self.temperatura=temperatura
        self.listProductos=listProductos
        self.Eant=Eant
        self.it=0
        self.condicion=False
        self.listAnt=[]
        self.mejorList=[]
        #self.mejorE=10000

    def templado(self,Eactual):
        if (self.it)<1000:
            self.temperatura=self.temperatura*0.90

            if self.temperatura<0.01:
                self.condicion=True
            
            
            dE=Eactual-self.Eant
            
            if (dE<0):
                self.Eant=Eactual
                #self.mejorE=Eactual
                self.listAnt=self.listProductos.copy()
            else:
                if random.random()<math.exp(-dE/self.temperatura): #random random entre 0-1
                    self.Eant=Eactual
                    #self.mejorE=Eactual
                    self.listAnt=self.listProductos.copy()

            self.it+=1
            #if self.it<1000:
             #   random.shuffle(self.listProductos)
            
            random.shuffle(self.listProductos)
        else:
            self.condicion=True
            



        