import sys, os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class de_encryptor:

    def __init__(self, key_file, file_to_decrypt):
        self.private_key = key_file
        self.cipher_text = file_to_decrypt

    def file_decipher(self):
        #Construyo la ruta.
        self.path_to_key = os.getcwd()
        self.private_key_path = str(self.path_to_key + "/" + self.private_key)
        self.path_to_cipher_file = str(self.path_to_key + "/" + self.cipher_text)

        #Ninguno de los 3 bloques escritos funciona.

        #Bloque para el descifrado sin sentencia "with".
        self.instance_for_private_key = open(self.private_key_path, "rb").read() #Creo una instancia de apertura para la llave con la que voy a descifrar
        self.load_private_key = RSA.import_key(self.instance_for_private_key)
        self.loaded_private_key = PKCS1_OAEP.new(self.load_private_key)
        self.instance_for_encrypted_data = open(self.path_to_cipher_file, "rb").read() #Creo una instancia de apertura para el archivo que voy a descifrar
        self.decipher_text = self.loaded_private_key.decrypt(self.instance_for_encrypted_data)
        print(self.decipher_text) #.decode("utf-8")

        with open(self.path_to_cipher_file, "wb") as self.f:
            self.f.write(self.decipher_text)
            self.f.close()

        #Bloque con apertura del archivo de la llave privada.
        #with open(self.private_key_path, "rb") as self.pk:
        #    self.load_private_key = RSA.import_key(self.pk.read())
        #    self.loaded_private_key = PKCS1_OAEP.new(self.load_private_key)
        #    self.decipher_text = self.loaded_private_key.decrypt(self.cipher_text)
        #    print(self.decipher_text.decode("utf-8"))
        #    self.pk.close()

        #Bloque con apertura del archivo de texto cifrado.    
        #with open(self.cipher_text, "rb") as self.cf: # wb = write, binary mode; rb = read, binary mode; wrb = write, read, binary mode. 
        #     #Cargo la llave privada 
        #    self.private_key = RSA.import_key(open(self.private_key_path).read())
        #    self.key = PKCS1_OAEP.new(self.private_key)
        #    self.decipher_text = self.key.decrypt(self.cf)
        #    self.cf.write(self.decipher_text)
        #    self.cf.close()
        return print(f"\nArchivo descifrado en: {self.path_to_cipher_file}")
        #PROBAR SI DESCIFRA Y GUARDA EL CONTENIDO DEL ARCHIVO!
    
    def __call__(self):
        self.file_decipher()

def main():

    password_bytes = input('Ingrese el nombre del archivo que contiene la contraseña: ')
    plain_text_file = input("Escriba el nombre del archivo que desea descifrar: ")
    new_deencripted_file = de_encryptor(password_bytes, plain_text_file)
    new_deencripted_file()

if __name__ == '__main__':
    app = main()