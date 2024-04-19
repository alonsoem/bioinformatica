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
        "GCG":["A","Alanina"],
        "GCA":["A","Alanina"],
        "GCC":["A","Alanina"],
        "GCT":["A","Alanina"],
        "GAG":["E","Ácido Glutámico"],
        "GAA":["E","Ácido Glutámico"],
        "GAC":["D","Ácido Aspártico"],
        "GAT":["D","Ácido Aspártico"],
        "ATG":["M","Metionina"], "ATA":["I","Isoleucina"], "ATC":["I","Isoleucina"], "ATT":["I","Isoleucina"],"TTG":["L","Leucina"],"TTA":["L","Leucina"],
        "CGA":["R","Arginina"], "CGT":["R","Arginina"], "CGC":["R","Arginina"], "CGG":["R","Arginina"],"AGG":["R","Arginina"],"AGA":["R","Arginina"],
        "CCC":["P","Prolina"], "CCG":["P","Prolina"], "CCT":["P","Prolina"], "CCA":["P","Prolina"],
        "CAG":["Q","Glutamina"], 
        "CAT":["Q","Glutamina"],
        "CAC":["H","Histidina"], 
        "CAT":["H","Histidina"],
        "ATG":["M","Metionina"],
        "ATA":["I","Isoleucina"],
        "ATC":["I","Isoleucina"],
        "ATT":["I","Isoleucina"],
        "AGT":["S","Serina"], 
        "AGC":["S","Serina"],
        "TCC":["S","Serina"],
        "TCG":["S","Serina"],
        "TCT":["S","Serina"],
        "TCA":["S","Serina"],
        "ACC":["T","Treonina"],
        "ACG":["T","Treonina"],
        "ACT":["T","Treonina"],
        "ACA":["T","Treonina"],
        "AAA":["K","Lisina"],
        "AAG":["K","Lisina"],
        "AAC":["N","Asparagina"],
        "AAT":["N","Asparagina"],
        "TTC":["F","Fenilalanina"], 
        "TTT":["F","Fenilalanina"],
        "TGG":["W","Triptofano"],
        "TGA":["START"],
        "TGC":["C","Cisteína"],
        "TGT":["C","Cisteína"],
        "TAG":["STOP"],
        "TAA":["STOP"],
        "TAC":["Y","Tirosina"], 
        "TAT":["Y","Tirosina"],
        "GTC":["V","Valina"],
        "GTG":["V","Valina"],
        "GTT":["V","Valina"], 
        "GTA":["V","Valina"],
        "GGC":["G","Glicina"],
        "GGG":["G","Glicina"], 
        "GGT":["G","Glicina"], 
        "GGA":["G","Glicina"],
        "CTA":["L","Leucina"],
        "CTG":["L","Leucina"],
        "CTT":["L","Leucina"],
        "CTC":["L","Leucina"],
        
  
    }
    try:
        return aminoDictionary[value]
    except Exception:
        return ""

def getComputer():
    
     
     out=False
     while out==False:
        os.system('cls')
        value = click.prompt('Indica el codón o triplete', type=str)
        print ("")
        value=value.upper()
        
        findOut=searchTripletValue(value)
        if findOut=="":
            print (f'El codón o triplete {value} no fué encontrado')
           
        else:
            print (f'El codón o triplete {value} es el aminoácido {findOut[1]} y identifica con {findOut[0]}')
        
        
        print ("")
        userContinue = click.prompt('¿Quiere buscar otro codón? (S/N)', type=str)
        
        if userContinue.upper()=="N":  
            out=True    #sale de la computadora
        
        
def testArnTriplet(arnM,amino):
    if searchTripletValue(arnM[0:3])[0]==amino:
        return True
    else:
        raise Exception("VIDA PERDIDA")
        
    
def etapaDos(aGame):
    aGame.setLevel(2)
    arnM=aGame.getArnM()
    os.system('cls')
    print(f'El ARN-m está listo para ser leído pero la función del Ribosoma también fué alcanzada por el virus.')
    print ("Deberás auxiliar la función del ARN TRANSFERENCIA y sustituir los aminoácidos que correspondan de leer el ARN MENSAJERO.")          
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
        print ("")
        value= int(input("Tu opción:"))
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
                    print(f'Ya sumamos {aGame.getAminos()} aminoácidos substituidos!')
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