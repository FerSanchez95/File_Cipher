import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP #Es un cifrador asimétrico basado en RSA y relleno (padding) OAEP.

#Funciona.

class encryptor():
    def __init__(self, bytes_lenght) -> None:
        self.key_lenght = int(bytes_lenght)

    def key_generator(self):
        self.new_key = RSA.generate(self.key_lenght)
        self.public_key_file = open('public_key.pem', 'wb')
        #¿Es necesario que el archivo tenga la extención '.PEM'?
        self.new_public_key = self.new_key.publickey().export_key('DER')
        self.public_key_file.write(self.new_public_key)
        self.public_key_file.close()
        self.private_key_file = open('private_key.pem', 'wb')
        self.new_private_key = self.new_key.export_key('DER')
        self.private_key_file.write(self.new_private_key)
        self.private_key_file.close()
        self.message = "== Llaves generadas =="
        return print(self.message) 

def main():
    first_arg = input('Ingrese el largo de la contraseña: ')
    new = encryptor(first_arg)
    new.key_generator()
    
if __name__ == '__main__':
    app = main()

