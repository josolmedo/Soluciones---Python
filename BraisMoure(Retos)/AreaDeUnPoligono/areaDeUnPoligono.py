class Poligono(): #Clase sumamente chafa, porque solo se soportan cuadrados, triangulos y rectángulos
    def __init__(self, base, altura, figura): #Método constructor
        self.__base = base
        self.__altura = altura
        self.__figura = figura
    
    def getBase(self):
        return self.__base
    
    def getAltura(self):
        return self.__altura
    
    def getFigura(self):
        return self.__figura
    
def saltoDeLinea():
    print("\n")

def calcularArea(poligono):
    figura = poligono.getFigura()
    if (figura == "triangulo"):
        base = poligono.getBase()
        altura = poligono.getAltura()
        return (base*altura)/2
    elif (figura == "cuadrado"):
        lado = poligono.getBase()
        return lado*lado
    elif (figura == "rectangulo"):
        base = poligono.getBase()
        altura = poligono.getAltura()
        return (base*altura)
    else:
        return "Ingresaste una figura no válida"
    
saltoDeLinea()
base = int(input("Ingrese la base de su poligono: "))
saltoDeLinea()
altura = int(input("Ingrese la altura de su poligono: "))
saltoDeLinea()
figura = str(input("Ingrese que figura es: "))
saltoDeLinea()
poligono = Poligono(base, altura, figura)

area = int(calcularArea(poligono))
print(f'El área del {figura} es de {area}')    
saltoDeLinea()