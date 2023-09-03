import sys, os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class de_encryptor:

    def __init__(self, key_file, file_to_decrypt):
        self.private_key = key_file
        self.cipher_text = file_to_decrypt

    def file_decipher(self):

        self.path_to_key = os.getcwd()
        self.private_key_path = str(self.path_to_key + "/" + self.private_key)
        self.path_to_cipher_file = str(self.path_to_key + "/" + self.cipher_text)

        self.instance_for_private_key = open(self.private_key_path, "rb").read() 
        self.instance_for_encrypted_data = open(self.path_to_cipher_file, "rb").read()
        self.load_private_key = RSA.import_key(self.instance_for_private_key)
        self.loaded_private_key = PKCS1_OAEP.new(self.load_private_key)
        self.decipher_text = self.loaded_private_key.decrypt(self.instance_for_encrypted_data)
        print(self.decipher_text)

        with open(self.path_to_cipher_file, "wb") as self.f:
            self.f.write(self.decipher_text)
            self.f.close()

        return print(f"\n === Archivo descifrado en: {self.path_to_cipher_file} ===\n")
    
    def __call__(self):
        self.file_decipher()

def main():

    password_bytes = input(f"\n >> Ingrese el nombre del archivo que contiene la contraseña: ")
    plain_text_file = input(" >> Escriba el nombre del archivo que desea descifrar: ")
    new_deencripted_file = de_encryptor(password_bytes, plain_text_file)
    new_deencripted_file()

if __name__ == '__main__':
    app = main()