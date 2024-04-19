import click
import time 
import random
import os

from font import bcolors

from cli_tables.cli_tables import *
from nucleo import gotoNucleus
from game import GenicExpressionGame
from presentation import showPresentation
from presentation import prologo

      
    
    
def getSplited(arnM):
    return arnM[0:3]
    
def loopSliced(arnM):
    #get first if ok got to second if not throw exception
    print (getSplited(arnM))

def searchTripletValue(value):
    aminoDictionary = {
        "GCG":["A"],
        "GCA":["A"],
        "GCC":["A"],
        "GCT":["A"],
        "GAG":["E"],
        "GAA":["E"],
        "GAC":["D"],
        "GAT":["D"],
        "ATG":["M"], "ATA":["I"], "ATC":["I"], "ATT":["I"],"TTG":["L"],"TTA":["L"],
        "CGA":["R"], "CGT":["R"], "CGC":["R"], "CGG":["R"],"AGG":["R"],"AGA":["R"],
        "CCC":["P"], "CCG":["P"], "CCT":["P"], "CCA":["P"],
        "CAG":["Q"], 
        "CAT":["Q"],
        "CAC":["H"], 
        "CAT":["H"],
        "ATG":["M"],
        "ATA":["I"],
        "ATC":["I"],
        "ATT":["I"],
        "AGT":["S"], 
        "AGC":["S"],
        "TCC":["S"],
        "TCG":["S"],
        "TCT":["S"],
        "TCA":["S"],
        "ACC":["T"],
        "ACG":["T"],
        "ACT":["T"],
        "ACA":["T"],
        "AAA":["K"],
        "AAG":["K"],
        "AAC":["N"],
        "AAT":["N"],
        "TTC":["F"], 
        "TTT":["F"],
        "TGG":["W"],
        "TGA":["START"],
        "TGC":["C"],
        "TGT":["C"],
        "TAG":["STOP"],
        "TAA":["STOP"],
        "TAC":["Y"], 
        "TAT":["Y"],
        "GTC":["V"],
        "GTG":["V"],
        "GTT":["V"], 
        "GTA":["V"],
        "GGC":["G"],
        "GGG":["G"], 
        "GGT":["G"], 
        "GGA":["G"],
        "CTA":["L"],
        "CTG":["L"],
        "CTT":["L"],
        "CTC":["L"],
        
  
    }
    try:
        return aminoDictionary[value][0]
    except Exception:
        return ""

def getComputer():
    
     
     out=False
     while out==False:
        os.system('cls')
        value = click.prompt('Indica el codón o triplete', type=str)
        value=value.upper()
        
        findOut=searchTripletValue(value)
        if findOut=="":
            print (f'El codón o triplete {value} no fué encontrado')
           
        else:
            print (f'El codón o triplete{value} puede ser {findOut}')

        userContinue = click.prompt('¿Quiere buscar otro codón? (S/N)', type=str)
        
        if userContinue.upper()=="N":  
            out=True    #sale de la computadora
        
def testArnTriplet(arnM,amino):
    if searchTripletValue(arnM[0:3])==amino:
        return True
    else:
        raise Exception("VIDA PERDIDA")
        
    
def etapaDos(aGame):
    aGame.setLevel(2)
    arnM=aGame.getArnM()
    os.system('cls')
    print(f'El ARN-m está listo para ser leído pero la función del Ribosoma también fué alcanzada por el virus.')
    print ("Deberás sustituir la función del ARN TRANSFERENCIA y substituir los aminoácidos que correspondan de leer el ARN MENSAJERO.")          
    print("")
    print(f'Recordá que la hebra de ARN-m es : {arnM}')        
    print ("")
    out=False
    while (out==False):
        print ("1) Leer un codón / triplete")
        print ("2) Volver al núcleo")
        print ("3) Usar Computadora (ayuda)")
        print ("4) Sustituir aminoácido por codón")
        print ("5) Ver hebra de ARN-m pendiente")
        print ("6) Ver cantidad de aminoácidos substituidos")
        value= int(input())
        print ("")
        
        if value==1:
            loopSliced(arnM)
            print ("")
        elif value==2:
            aGame.setLevel(1)
            out=True
        elif value==3:
            getComputer()
            
        elif value==4:
            if arnM=="":
                print ("")
                print (f'No hay hebra de ARN-m aquí! Deberás volver al núcleo.')
                print ("") 
            else:
                aminoValue = click.prompt('Indica el aminoácido que corresponde al codón o triplete', type=str)
                if testArnTriplet(arnM,aminoValue.upper()):
                    arnM=arnM[3:]
                    aGame.setArnM(arnM)
                    aGame.addOneAmino()
                    
                    
                    print (f"{bcolors.OKGREEN}EXCELENTE! Obtuvimos un aminoácido!{bcolors.ENDC}")     
                    print(f'Ya sumamos {aGame.getAminos()} aminoácidos sintetizados!')
                    print ("")
                
                
                
        elif value==5:
            if arnM=="":
                print ("")
                print (f'No hay hebra de ARN-m aquí! Deberás volver al núcleo.')
                print ("")   
            else: 
                print ("")
                print (f'La hebra de ARN-m es: {arnM}')
                print ("")
        elif value==6:
            print ("")
            print (f'Ya substituiste {aGame.getAminos()} aminoácidos en total!')
            print ("")
            
        
    
    
    
@click.command()
def main():
    
    game=GenicExpressionGame()
    
    while True:
        
        showPresentation()
        game.checkLifeStatus()
        
        
        while game.remainingLifes()>=0:
            try:
                if game.getLevel()==0:
                    prologo(game)
                elif game.getLevel()==1:
                    gotoNucleus(game)
                else:
                    etapaDos(game)
            except Exception:
                
                game.remove1Life()
                
            


if __name__ == '__main__':
    main()