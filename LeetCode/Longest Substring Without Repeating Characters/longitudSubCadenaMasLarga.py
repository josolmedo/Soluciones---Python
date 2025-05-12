def longitudCadenaMasLarga(s):
    contador1 = 0
    contador2 = 0
    constructor = ""
    if(s == " "):
        return 1    
    for letra in s:
        constructor = constructor + letra       
        if(verificador(constructor, letra) == True):
            contador1+=1
        else:            
            if contador1 > contador2:
                contador2 = contador1                
            #constructor = letra
            contador1=1
    if(contador1>contador2):
        contador2 = contador1
    
    return contador2        


def verificador(cadena, letraNueva):
    contador = 0
    for letra in cadena:
        if letraNueva == letra:
            contador+=1
        if contador > 1:
            return False
    return True

print("\n")
s = str(input("Ingresa una cadena: "))
print("\n\n"+str(longitudCadenaMasLarga(s))+"\n\n")
    
    
