'''The module 'os' is used to get current work directory path.'''
import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from path_to_file_contruct import Constructor
from time_stamp import timeStamp 

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
    def __init__(self, file_name: str, byte_lenght: int) -> None:
        
        self.key_lenght = byte_lenght
        path_creation_instance = Constructor(file_name, None)        
        self.file, self.key_dir, self.public_key_name, self.private_key_name = path_creation_instance.CreateKeyDir() 
        

    def key_generator(self):
        '''
        'key_generator' function  generates the public and private keys. For now it store the
        keys in the directory where the script is executed. This will change whe the the program
        is completed.
        '''
        new_key = RSA.generate(self.key_lenght)
        
        #Public key generation.
        public_key_file = open(self.public_key_name, 'wb')
        new_public_key = new_key.publickey().export_key('DER')
        public_key_file.write(new_public_key)
        public_key_file.close()
        
        #Private key generation.
        private_key_file = open(self.private_key_name, 'wb')
        new_private_key = new_key.export_key('DER')
        private_key_file.write(new_private_key)
        private_key_file.close()
        
        #Timestamp at the time of creatios of the keys
        instance_for_timestamp = timeStamp(self.key_dir)
        instance_for_timestamp()
        
        #End message and key generated instance returned.
        print("\n -> Llaves generadas.")
        return new_key

    def encryption_process(self) -> None:
        '''
        The function takes the variables, call the 'key_generator' function and generates an AES
        key that is encripted within the file. The AES key have a byte longitude of 16 bytes,
        this wil change later in the complete version. 
        '''
        #Lecture of te content in the file and encoding for encryption.
        content_of_file = open(self.file, 'rb').read()
        data_to_encrypt = content_of_file
        
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
        print("\n -> Archivo cifrado.")

    def __call__(self):
        self.encryption_process()
        
    def __str__(self) -> str:
        return "Archivo cifrado"


