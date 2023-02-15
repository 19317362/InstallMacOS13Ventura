#!/usr/bin/python3
import os

print ("1. Instalar programas necesarios")
print ("2. Descargar fichero BaseSystem.dmg")
print ("3. Crear fichero BaseSystem.img")
print ("4. Crear disco")
print ("5. Instalar/Iniciar MacOS 13 Ventura")
print ("6. Salir")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
	os.system("bash InstalarSW.sh")
elif opcion == 2:
	os.system("python3 macrecovery.py -b Mac-B4831CEBD52A0C4C -m 00000000000000000 download")
elif opcion == 3:
	os.system("bash CrearBaseSystemImg.sh")
elif opcion == 4:
	os.system("bash CrearDisco.sh")
elif opcion == 5:
	os.system("bash InstalarMacOS.sh")

