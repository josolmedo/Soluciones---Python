def esPrimo(numero):
    if numero==1:
        return False
    for x in range(2,numero):
        cociente = numero // x
        if cociente*x == numero:
            return False        
    return True

numero=int(input("\n¿Hasta que número quieres imprimir los números primos?: "))
print("\n")
for x in range(1,numero+1):
    if(esPrimo(x)):
        print(x)

print("\n")