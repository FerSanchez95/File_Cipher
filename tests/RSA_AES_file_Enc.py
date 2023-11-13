'''The module 'os' is used to get current work directory path.'''
#import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

class AesEncryptor:
    '''
    This class takes the file name and the bytes for the key longitude as arguments.
    Generates private and public keys and the encripted file that is passed.

    Functions:
    ----------
        key_generator:
            'key_generator' function  generates the public and private keys. For now it estore the
            keys in the directory where the script is executed. This will change whe the the program
            is completed. 

        encription_process:
            The function takes the variables, call the 'key_generator' function and generates an AES
            key that is encripted within the file. The AES key have a byte longitude of 16 bytes,
            this wil change later in the complete version. 
    '''
    def __init__(self,file_name: str, byte_lenght: int) -> None:
        self.key_lenght = int(byte_lenght)
        self.file = file_name

    def key_generator(self):
        '''
        'key_generator' function  generates the public and private keys. For now it estore the
        keys in the directory where the script is executed. This will change whe the the program
        is completed.
        '''
        new_key = RSA.generate(self.key_lenght)
        #Public key generation.
        public_key_file = open('public_key.pem', 'wb')
        new_public_key = new_key.publickey().export_key('DER')
        public_key_file.write(new_public_key)
        public_key_file.close()
        #Private key generation.
        private_key_file = open('private_key.pem', 'wb')
        new_private_key = new_key.export_key('DER')
        private_key_file.write(new_private_key)
        private_key_file.close()
        #End message and key generated instance returned.
        print("\n== Llaves generadas ==\n")
        return new_key

    def encryption_process(self):
        '''
        The function takes the variables, call the 'key_generator' function and generates an AES
        key that is encripted within the file. The AES key have a byte longitude of 16 bytes,
        this wil change later in the complete version. 
        '''
        #Lecture of te content in the file and encoding for encryption.
        content_of_file = open(self.file, 'rb').read()
        data_to_encrypt = content_of_file.encode("utf-8")
        #Create the byte array for AES encryption
        bytes_for_aes_key = get_random_bytes(16)
        #Generate public key, private key and encryption for AES bytes array.
        public_key = self.key_generator()
        rsa_cipher = PKCS1_OAEP.new(public_key.publickey())
        aes_key_encryption = rsa_cipher.encrypt(bytes_for_aes_key)
        #Encryption of the data with AES method
        aes_cipher = AES.new(bytes_for_aes_key, AES.MODE_EAX)
        encrypt_data, tag = aes_cipher.encrypt_and_digest(data_to_encrypt)

        #Uses 'with' to open the file and a list to write a file with
        #the encrypted data.
        variables_to_write_in_file = [aes_key_encryption, aes_cipher.nonce, tag, encrypt_data]
        with open(self.file, "wb") as encripted_file:
            for variable in variables_to_write_in_file:
                encripted_file.write(variable)
            encripted_file.close()
        #End message.
        succeful_message = "\n === Archivo cifrado === \n"
        return succeful_message

    def __call__(self):
        self.encryption_process()

#The next lines of code will be for testig the class only.
def main():
    '''
    This function will take the name and the bytes for the key, then passed 
    to the encryption class.
    In the future there will be a good idea to add an input variable that
    refers to the aes random bytes generator. In this case is a fix value
    of 16 (see line 37).
    THIS FUNCTION IS ONLY USED TO TEST THE SCRIPT.
    EVEN THE if __name__ == '__main__'.
    '''
    name = input("Enter the name of the file you want to encrypt: ")
    length = input("Enter the length, in bytes, of the password (eg.: 2048, 4096, etc): ")
    new_encripted_file = AesEncryptor(name, length)
    new_encripted_file()

if __name__ == '__main__':
    main()
