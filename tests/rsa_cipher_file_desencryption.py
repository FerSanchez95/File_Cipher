import sys, os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class encryptor:

    def __init__(self, bytes_lenght, file_to_encrypt) -> None:
        self.key_lenght = int(bytes_lenght)
        self.file = file_to_encrypt

    def key_generator(self): 
        self.new_key = RSA.generate(self.key_lenght) #Generador de llaves pública y privada.
        #¿Es necesario que el archivo tenga la extención '.PEM'?
        #Llave pública.
        self.public_key_file = open('public_key.pem', 'wb')
        self.new_public_key = self.new_key.publickey().export_key('DER')
        self.public_key_file.write(self.new_public_key)
        self.public_key_file.close()
        #Llave privada.
        self.private_key_file = open('private_key.pem', 'wb')
        self.new_private_key = self.new_key.export_key('DER')
        self.private_key_file.write(self.new_private_key)
        self.private_key_file.close()
        print(f"\n== Llaves generadas ==\n")
        return self.new_key
     
    def file_cipher(self):
        self.folder_path = os.getcwd()
        self.file_path = self.folder_path + "/" + self.file #Completar la ruta del archivo.
        with open(self.file_path, "wb") as self.f:   #Abrir el archivo y encriptarlo con las llaves generadas.
            self.key_to_encrypt = self.key_generator()
            self.cipher = PKCS1_OAEP.new(self.key_to_encrypt.publickey())
            self.text_to_cipher = self.cipher.encrypt(self.file.encode())
            self.f.write(self.text_to_cipher)
            self.f.close()
        return print(f"\n=== Archivo cifrado en {self.folder_path} ===\n")

    def __call__(self):
        self.file_cipher()

#Seguir con la clase de desifrado.

class de_encryptor:
    def __init__(self, key_file, file_to_decrypt):
        self.private_key = key_file
        self.cipher_text = file_to_decrypt

    def decipher(self):
        #Construyo la ruta.
        self.path_to_key = os.getcwd()
        self.private_key_path = self.path_to_key + "/" + self.private_key
        with open(self.cipher_text, "wb") as self.cf:
            #Cargo la llave privada 
            self.private_key = RSA.import_key(open(self.private_key_path, "rb").read(), passphrase=None)
            self.key = PKCS1_OAEP.new(self.private_key)
            self.decipher_text = self.key.decrypt(self.cf)
            self.cf.write(self.decipher_text)
        
        #with open(self.private_key_path, "rb") as self.pk:
            #self.private_key = StopIteration.load_pem_private_key(self.file_to_decipher.read(), password=None)
            


def main():
    password_bytes = input('Ingrese el largo de la contraseña: ')
    plain_text_file = input("Escriba el nombre del archivo que desea cifrar: ")
    new_encripted_file = encryptor(password_bytes, plain_text_file)
    new_encripted_file()

if __name__ == '__main__':
    app = main()