import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(num1,num2):
    multiplicar = num1*num2
    return multiplicar


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    iterador = 0
    suma  = 0

    while iterador < 1000:
        if (iterador%3 == 0) and (iterador%5 == 0):
            suma = suma + iterador
    
        iterador = iterador + 1

    return suma 


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
def definicionCono(radio,altura):
    
    result = {'generatriz': math.sqrt((altura*altura) + (radio*radio)), 'area' : math.pi *radio *(radio + (math.sqrt((altura*altura) + (radio*radio)))), 'volumen': (1/3)*(math.pi)*(radio*radio)*(altura)}

    return result


def obtenerGeneratriz(radio, altura):
    result = math.sqrt((altura*altura) + (radio*radio))
    return result


def obtenerArea(radio,altura):
    result = math.pi *radio *(radio + (math.sqrt((altura*altura) + (radio*radio))))
    return result


def obtenerVolumen(radio, altura):
    result = (1/3)*(math.pi)*(radio*radio)*(altura)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def __init__(self,radio,altura):
        self.radio = radio
        self.altura = altura 

    def definicionCono(self, radio, altura):
        
        
        return  {'generatriz': math.sqrt((self.altura*self.altura) + (self.radio*self.radio)), 'area' : math.pi *self.radio *(self.radio + (math.sqrt((self.altura*self.altura) + (self.radio*self.radio)))), 'volumen': (1/3)*(math.pi)*(self.radio*self.radio)*(self.altura)}
        
    def obtenerGeneratriz(self, radio, altura):
        return  math.sqrt((self.altura*self.altura) + (self.radio*self.radio))
    


    def obtenerArea(self, radio, altura):
         return  math.pi *self.radio *(self.radio + (math.sqrt((self.altura*self.altura) + (self.radio*self.radio))))
    


    def obtenerVolumen(self, radio, altura):
        return (1/3)*(math.pi)*(self.radio*self.radio)*(self.altura)
      


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:
    def registrar(self):
        return 0

    def totalCostoSanSalvador(self):
        return 0

    def totalCostoConDescuento(self):
        return 0


class Paciente:
    def __init__ (self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.nombre = nombre 
        self.lugar = lugar 
        self.descripcion = descripcion
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento

    def get_Nombre (self):
        return self.nombre
    
    def get_lugar (self):
        return self.lugar
    
    def get_descripcion(self):
        return self.descripcion
    
    def get_costo(self): 
        return self.costo
    
    def get_conDescuento (self) :
        return self.conDescuento
    
    def get_descuento (self): 
        return self.descuento

    def showPacient (self):
        print(f"{self.get_Nombre()}|{self.get_lugar()}|{self.get_descripcion()}|{self.get_costo()}|{self.get_conDescuento()}|{self.get_descuento()}")

    


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/sebasvr8/ExamenParcialQuiPython.git"
