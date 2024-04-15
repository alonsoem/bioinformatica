import time 
import os 
from font import bcolors


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