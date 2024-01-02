'''The module 'os' is used to get current work directory path.'''
import os
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from path_to_file_contruct import Constructor


class AesDecryptor:
    '''
    This class is used to decrypt the files encrypted with the public generated 
    by the encryption script.
    '''
    
    def __init__(self, file_to_decrypt: str, private_key_file: str):
        
        file_path = Constructor(file_to_decrypt, private_key_file)
        self.encrypted_data, self.private_key = file_path.ReadKeyPath()


    def files_load(self):
        '''
        This functions loads the encrypted file and decrypt it. Takes the path to the private
        key and the file as arguments.
        ''' 
        
        #Instances for private key lecture and division of encrypted data.
        data_file = open(self.encrypted_data, "rb")
        instace_for_key = open(self.private_key, "rb").read()
        key_lecture = RSA.import_key(instace_for_key)
        
        #Lecture of differents parts of the data.
        enc_key_in_file, nonce, tag, encrypted_text = \
              [data_file.read(x) for x in (key_lecture.size_in_bytes(), 16, 16, -1)]
        data_file.close()
        
        #Decrypt of  AES session key
        rsa_cipher = PKCS1_OAEP.new(key_lecture)
        session_key = rsa_cipher.decrypt(enc_key_in_file)
        
        #Data decrypt using AES session key.
        aes_cipher = AES.new(session_key, AES.MODE_EAX, nonce)
        decrypt_data = aes_cipher.decrypt_and_verify(encrypted_text, tag)
        decoded_data = decrypt_data
        
        #Write down the text in the same file.
        with open(self.encrypted_data, "wb") as write_file:
            write_file.write(decoded_data)
            write_file.close()
            
        #End message and retrun.
        print("\n -> Decrypted file\n")

    def __call__(self):
        self.files_load()

    def __str__(self) -> str:
        return "Archivo descifrado"
    
