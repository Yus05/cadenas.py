"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

"""

precio =input("Introduzca el precio: ")

precio = precio.split(".")

euros = precio[0]
centimos = precio[1]

print("El numero de euros es: " + euros)
print("La cantidad de centimos es: " + centimos)