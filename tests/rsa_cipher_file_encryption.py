import sys, os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class encryptor:

    def __init__(self, bytes_lenght, file_to_encrypt) -> None:
        self.key_lenght = int(bytes_lenght)
        self.file = file_to_encrypt

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
        print(f"\n== Llaves generadas ==\n")
        return self.new_key

    def file_cipher(self):
        self.folder_path = os.getcwd()
        self.file_path = self.folder_path + "/" + self.file #Completar la ruta del archivo.
        self.f = open(self.file_path).read() 
        self.data_to_encrypt = self.f.encode("utf-8")  #Codificación UTF-8 del los datos del archivo.         
        self.key_to_encrypt = self.key_generator() 
        self.cipher = PKCS1_OAEP.new(self.key_to_encrypt.publickey())
        self.encrypted_data = self.cipher.encrypt(self.data_to_encrypt)
        with open(self.file_path, "wb") as self.f:
            self.f.write(self.encrypted_data)
            self.f.close()
            
        return print(f"\n=== Archivo cifrado en {self.folder_path} ===\n")

    # def file_cipher(self):
    #     self.folder_path = os.getcwd()
    #     self.file_path = self.folder_path + "/" + self.file #Completar la ruta del archivo.
    #     with open(self.file_path, "rb") as self.f:   #Abrir el archivo y encriptarlo con las llaves generadas.
    #         self.read_data = self.f.read() #Lecturad del archivo
    #         self.encoded_data = self.read_data.encode("utf-8")  #Codificación UTF-8 del los datos del archivo.         
    #         self.key_to_encrypt = self.key_generator() #Llamo al generador de llaves
    #         self.cipher = PKCS1_OAEP.new(self.key_to_encrypt.publickey())
    #         #Los datos a cifrar deben estar codificados en formato UTF-8 antes de encriptarlos. 
    #         self.text_to_cipher = self.cipher.encrypt(self.encoded_data)
    #         self.f.close()
    #     with open(self.file_path, "wb") as self.f:
    #         self.f.write(self.text_to_cipher)
    #         self.f.close()
            
    #     return print(f"\n=== Archivo cifrado en {self.folder_path} ===\n")

    # def file_cipher(self):
    #     self.folder_path = os.getcwd()
    #     self.file_path = self.folder_path + "/" + self.file #Completar la ruta del archivo.
    #     with open(self.file_path, "wb") as self.f:   #Abrir el archivo y encriptarlo con las llaves generadas.
    #         self.key_to_encrypt = self.key_generator()
    #         self.cipher = PKCS1_OAEP.new(self.key_to_encrypt.publickey())
    #         # Los datos a cifrar deben estar codificados en formato UTF-8 antes de encriptarlos.
    #         self.encoded_data = self.f.read().encode("utf-8")
    #         self.text_to_cipher = self.cipher.encrypt(self.encoded_data.encode("utf-8"))
    #         self.f.write(self.text_to_cipher)
    #         self.f.close()
    #     return print(f"\n=== Archivo cifrado en {self.folder_path} ===\n")

    def __call__(self):
        self.file_cipher()

def main():
    password_bytes = input('Ingrese el largo de la contraseña: ')
    plain_text_file = input("Escriba el nombre del archivo que desea cifrar: ")
    new_encripted_file = encryptor(password_bytes, plain_text_file)
    new_encripted_file()

if __name__ == '__main__':
    app = main()