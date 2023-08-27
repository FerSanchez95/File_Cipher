import sys
from Crypto.PublicKey import RSA 

#Ingreso los valores que necesitan las variables para la genereación de contraseñas.

bit_size = int(sys.argv[1])
key_format = sys.argv[2]

keys = RSA.generate(bit_size)

print("Clave pública: ")

print(keys.publickey().export_key(key_format), end = "\n")

print("Clave Privada: ")

print(keys.export_key(key_format))


