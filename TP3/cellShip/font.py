import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
def animTextPrint(text,endDelay):
    for i  in range(0 , len(text)):
        print (f"{text[i]}",end='')
        time.sleep(0.05)
    print("")
    time.sleep(endDelay) 
    

