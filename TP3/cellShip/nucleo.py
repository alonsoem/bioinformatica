
import click
import time 
import random
import os
from cli_tables.cli_tables import *
from game import GenicExpressionGame
from font import bcolors

class CodigoGenetico:
    
    def __init__(self):
        # Creating instance variables
        self.adnLetters = ['A','U','C','G']
        self.baseArnLetters = ['C','G','T','A']
        self.geneticCode=""
        self.genAdn=""
    
    def generarCodigoGenetico(self):
        #arnLetters = ['C','G','T','A']
        arnList=[]
        while self.baseArnLetters!=[]:
            oneItem= self.baseArnLetters.pop(random.randrange(len(self.baseArnLetters))) 
            arnList.append(oneItem)
        
        self.geneticCode= arnList
        
        #return arnList
    
    def getAdnLetters(self):
        return self.adnLetters
    
    def arnOk(self,n):
        replacedValue = self.geneticCode[self.adnLetters.index(n)]
        return replacedValue

    
    def arnIsValid(self,arnValue):
        
        
        adnToArn = list(map(self.arnOk, self.genAdn))
        
        return arnValue==''.join(adnToArn)
        
    def generarGenADN(self):
        arnM=""
        
        for i in range(1, 10):
            letter = random.choice(self.adnLetters)
            arnM += letter
        self.genAdn=arnM
    
    def getGen(self):
        return " ".join(self.genAdn)
    
    def getArnGeneticCode(self):
        return self.geneticCode
    
    

def presentacion2():
    os.system('cls')
    print (f'Estamos entrando al núcleo')
    time.sleep(1)
    print("")
    print(f'Se ha activado un gen...')
    
    print("")
   
    
    
def gotoNucleus(aGame):
    aGame.setLevel(1)
    presentacion2() 
    
    codigo=CodigoGenetico()
    
    codigo.generarCodigoGenetico() ##Equivalencia de ARN
    
    codigo.generarGenADN() #cadena adn
    
    print (codigo.getGen()) #muestro el gen en pantalla
    
    
    print("")
    time.sleep(2)
    print(f'Ayuda al ARN polimerasa en la TRANSCRIPCIÓN para generar el ARN Mensajero.')        
    
    time.sleep(2)
    print(f'Este parece ser el código genético:')        
    
    print("")        
    print_table([['ADN']+codigo.getAdnLetters(),['ARN']+codigo.getArnGeneticCode()])
    print("")        
    
    value = click.prompt('Indicá como debería ser el ARN Mensajero', type=str)
    value=value.upper()
    
    if codigo.arnIsValid(value):
        aGame.setArnM(value)
        aGame.setLevel(2)
        os.system('cls')
        print ("")
        
        print (f"{bcolors.OKGREEN}¡BUEN TRABAJO!{bcolors.ENDC}")     
        print(f'El ARN-m generado ya salió del núcleo y se dirige al Ribosoma')        
        print ("")
        time.sleep(4)
    else :
        os.system('cls')
        print ("")
        print (f"{bcolors.FAIL}SE HA DEGENERADO EL ARN MENSAJERO{bcolors.ENDC}")     
        print ("")
        time.sleep(4)
        raise Exception("VIDA PERDIDA")
        
    