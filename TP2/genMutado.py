def compararGenes(secuencia1 , secuencia2):
    #Retorna la cantidad de tomas necesarias para obtener el gen mutado
    #Devuelvo 9999 cuando llego a la cuarta toma porque puede ser mortal
    genMutado= 'GTTTGTGGTTG' 
    
    if genMutado in secuenciaADN:
            return 0
        
    for toma in range(1, 5):
        
        
        if toma==1:
            secuenciaADN=secuenciaADN.replace("C","T")	

        if toma==2:
            secuenciaADN=secuenciaADN.replace("A","G")	

        if toma==3:
            secuenciaADN=secuenciaADN.replace("C","A")	

        if toma>=4:
            return 9999 

        if genMutado in secuenciaADN:
            return toma
        


secuenciaEjemplo='ATGGAACTTGCAATCGAAGTTGGC'

print (tomasParaObtenerElGenMutado(secuenciaEjemplo))

