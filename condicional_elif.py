#Pedir numeros al usaurio
anos = int(input("Ingresar la edad del usuario: "))

if  anos <= 16:
    print("No puedes conducir")
elif anos <= 18:
    print("Permiso para conducir")
elif anos <= 70:
    print("Licencia estandar")
else:
    print("Licencia especial")