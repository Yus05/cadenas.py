"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

"""
productos = input("Lista de productos: ")
productos = productos.split(",")

productos = "\n".join(productos)


print(productos)

