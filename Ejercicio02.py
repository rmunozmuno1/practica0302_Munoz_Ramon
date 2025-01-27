"""Crear una Clase Producto con los siguientes atributos:
 - código
 - nombre
 - precio 
Crea su constructor, getter y setter y una función llamada calcular_total, 
donde le pasaremos unas unidades y nos debe calcular el precio final.
"""
class producto:
    def __init__ (self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,valor):
        self.__codigo = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @codigo.setter
    def codigo(self,valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    
    @codigo.setter
    def codigo(self,valor):
        self.__precio = valor
    
    def calcular_total(self, unidades):
        return self.precio * unidades

    def __str__ (self):
        return 'Codigo' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)
    
class pedido:
    def __init__(self,productos,cantidades):
        self.__productos = productos
        self.__cantidades = cantidades
    
    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)
        return total
    
    def mostrar_pedido(self):
        for (p,c) in zip(self.__productos, self.__cantidades):
            print("Producto ->", p.nombre, ", Cantidad: " + str(c))

       

p1 = producto(1,"producto 1", 5)
p2 = producto(2,"producto 1", 10)
p3 = producto(3,"producto 1", 20)
print (p1)
print (p2)
print (p3)

print (p1.calcular_total(5))
print (p2.calcular_total(5))
print (p3.calcular_total(5))

productos = [p1, p2, p3]
cantidades = [5, 10, 2]
pedido = pedido(productos, cantidades)

print ('Total pedido:' + str(pedido.total_pedido()))
pedido.mostrar_pedido()