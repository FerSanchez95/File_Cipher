import os
from typing import Any
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

class aes_encryptor:
    
    def __init__(self,file_name: str, byte_lenght: int) -> None:
        self.key_lenght = byte_lenght
        self.file = file_name

    def key_generator(self): 
        self.new_key = RSA.generate(self.key_lenght)
        self.public_key_file = open('public_key.pem', 'wb')
        self.new_public_key = self.new_key.publickey().export_key('DER')
        self.public_key_file.write(self.new_public_key)
        self.public_key_file.close()
        self.private_key_file = open('private_key.pem', 'wb')
        self.new_private_key = self.new_key.export_key('DER')
        self.private_key_file.write(self.new_private_key)
        self.private_key_file.close()
        print(f"\n== Llaves generadas ==\n")
        return self.new_key
    
    def encryption_process(self):
        #Lecture of te content in the file and encoding for encryption.
        self.content_of_file = open(self.file).read()
        self.data_to_encrypt = self.content_of_file.encode("utf-8")

        #Create the byte array for AES encryption
        self.bytes_for_aes_key = get_random_bytes(16)
       
        #Generate public key, private key and encryption for AES bytes array.
        self.public_key = self.key_generator()
        self.rsa_cipher = PKCS1_OAEP.new(self.public_key.publicKey())
        self.aes_key_encryption = self.rsa_cipher.encrypt(self.bytes_for_aes_key)

        #Encryption of the data with AES method
        self.aes_cipher = AES.new(self.bytes_for_aes_key, AES.MODE_EAX)
        self.encrypt_data, self.tag = self.aes_cipher.encrypt_and_digest(self.data_to_encrypt)

        #Uses 'with' to open the file and list comprenhension to write a file with the encrypted data.
        with open(self.file, "wb") as self.encripted_file:
            [ self.encripted_file.write(x) for x in (self.aes_key_encryption, self.aes_cipher.nonce, self.tag, self.encrypt_data) ]
            self.encripted_file.close()

        self.validation_message  = f"\n === Archivo cifrado ===\n"
        
        return self.validation_message
    
    def __call__(self):
        self.encryption_process()

#The next lines of code will be for testig the class only.
def main():
    name = input("Enter the name of the file you want to encrypt: ")
    length = input("Enter the length, in bytes, of the password (eg.: 2048, 4096, etc): ")
    new_encripted_file = aes_encryptor(name, length)
    new_encripted_file()

if __name__ == '__name__':
    app = main()

