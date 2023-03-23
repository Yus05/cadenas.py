"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

"""

fecha = input("Introduce fecha de cumpleanos dd/mm/aaaa: ")

fecha = fecha.split("/")

dia = fecha[0]
mes = fecha[1]
ano = fecha[2]

print("El dia de tu cumpleanos es:", dia)
print("Tu mes de cumpleanos es:", mes)
print("Tu ano de nacimiento es:", ano)

