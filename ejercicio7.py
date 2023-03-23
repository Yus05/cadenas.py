"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

"""

usuario = input("Introduzca su email: ")

usuario = usuario.split("@")
usuario = usuario[0]


correo = "@ceu.es"

print(usuario + correo)