import time 
import os 
from font import bcolors
from font import animTextPrint


def clear_screen(): 
  os.system("cls" if os.name == "nt" else "clear") 
  
def display_frame(frame_content, delay): 
  clear_screen() 
  print(f"{bcolors.OKGREEN}{frame_content}{bcolors.ENDC}")
  time.sleep(delay) 
  


def showPresentation():
    frames = [ 
    "frame1.txt", 
    "frame2.txt", 
    "frame3.txt", 
    ] 
    frame_delay = 1
    
    with open("frame1.txt", "r") as file: 
            frame_content = file.read() 
            display_frame(frame_content, frame_delay)
    print()
    print(f"{bcolors.OKGREEN}Presioná una tecla para iniciar el viaje...{bcolors.ENDC}")
    input()            
    for frame_file in frames: 
        with open(frame_file, "r") as file: 
            frame_content = file.read() 
            display_frame(frame_content, frame_delay)
            
            
def prologo(aGame):
    os.system('cls')
    delay=0
    
    animTextPrint("Dentro de la micro nave CELLSHIP entrarás en un viaje celular adentrándote en una célula eucariota...",delay)
    
    animTextPrint('La célula fué atacada por un virus y no es capaz por si sola de realizar los procesos de TRANSCRIPCIÓN y TRADUCCIÓN.',delay)
    
    animTextPrint('Tu misión, será lograr subtituir la mayor cantidad de aminoácidos para formar cadenas polipeptídicas y luego proteínas.',delay)
    
    animTextPrint('Tranquil@, tendrás una computadora que te ayudara en el proceso!!',delay)
    print("")
    
    
    
    
    print('Presioná una tecla para continuar...')
    input()
    
    aGame.setLevel(1)            