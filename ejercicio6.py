"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

frase = input("Introduce frase y una vocal: ")

vocal = frase[-1]
vocal = vocal.upper()

frase = frase[:-1]

print(frase + vocal)

