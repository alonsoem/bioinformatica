def porcentageCyG(cadenaADN):
    nucleotidos =list(cadenaADN)
    totalNucleotidos=len(nucleotidos)
    totalCG=0
    
    for cadaNucleotido in nucleotidos:
        if cadaNucleotido in ["C", "G"]:
            totalCG=totalCG+1
    
    return totalCG/ totalNucleotidos*100
    

cadenaADNEjemplo="AUGAAAAAAAAACUACUAAUG"
print ("El porcentaje de CyG es : ",porcentageCyG(cadenaADNEjemplo) )
