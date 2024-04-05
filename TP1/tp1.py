import sys




def getAminoPreference (aminoAcid):
    #esta funcion toma la tabla y retorna la preferencia de plegado de un aminoacido
    preferences = dict(
        glu='H',
        alu='H',
        leu='H',
        met='H',
        gln='H',
        lys='H',
        arg='H',
        his='H',
        val='B',
        lle='B',
        tyr='B',
        cys='B',
        trp='B',
        phe='B',
        thr='B',
        gly='L',
        asn='L',
        pro='L',
        ser='L',
        asp='L',
    )
    
    return preferences.get(aminoAcid)



def getSecondaryStructure(proteicChain):
    #Dada una lista de aminoacidos retorna una lista de preferencias de plegado
    result = map(getAminoPreference, proteicChain)
    return result
    


def main():
    #toma como parametro una lista empresada entre comillas y separando los elementos con una coma.
    #Ejemplo "glu,alu,pro"
    
    inboundList = sys.argv[1]
    proteicChain = inboundList.split(",")

    print (list(getSecondaryStructure(proteicChain)))
	


if __name__ == '__main__':
    main()

