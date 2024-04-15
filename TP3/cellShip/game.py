import time
from font import bcolors

class GenicExpressionGame:
    def __init__(self):
        self.vidas=2
        self.arnM=""
        self.level=0
        self.name=""
        self.aminos=0
    
    def reset(self):
        self.vidas=2
        self.arnM=""
        self.level=0
        self.name=""
        self.aminos=0
        

    def setUserName(self,name):
        self.name=name
        
    def remove1Life(self):
        self.vidas-=1   
        if self.remainingLifes()<0:
            print (f"{bcolors.FAIL}Perdiste el juego! Volvé a intentarlo{bcolors.ENDC}")     
        else:
            print (f"{bcolors.FAIL}Perdiste una vida. Ahora te queda {self.remainingLifes()} vidas{bcolors.ENDC}") 
        time.sleep(5)
        
    def checkLifeStatus(self):
        
        if self.vidas<=0:
            self.reset()
        
    def remainingLifes(self):
        return self.vidas    
    
    def setArnM(self,value):
        self.arnM+=value 
        
    def getArnM(self):
        return self.arnM
    
    def getLevel(self):
        return self.level
    
    def setLevel(self,level):
        self.level=level
        
    def addOneAmino(self):
        self.aminos+=1
        
    def getAminos(self):
        return self.aminos
