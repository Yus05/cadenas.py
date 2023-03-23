"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

"""

nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
unidades = float(input("U/disponibles: "))

coste = precio * unidades
coste = str(coste)

precio = str(precio)
unidades = str(unidades)

print("El producto:",nombre ,"tiene un precio de:", precio,"y quedan:", unidades,"en inventario quedan:" ,coste)

