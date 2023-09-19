from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
import os


class aes_decryptor:

    def __init__(self, private_key_file: str, file_to_decrypt: str):
        self.private_key = private_key_file
        self.encrypted_data = file_to_decrypt

    def files_load(self):
        #In this test the directory for the key and the encrypted data is the same.
        self.path_cwd = os.getcwd()
        self.path_to_key = self.path_cwd + "/" + self.private_key
        self.path_to_file = self.path_cwd + "/" + self.encrypted_data
        
        #Instances for private key lecture and division of encrypted data.
        self.data_file = open(self.path_to_file, "rb")
        self.key_lecture = RSA.import_key(open(self.path_to_key).read())
        
        #Lecture of differents parts of the data.
        self.enc_key_in_file, self.nonce, self.tag, self.encrypted_text = [ self.data_file.read(self.x) for self.x in (self.key_lecture.size_in_bytes(), 16, 16, -1) ]
        self.data_file.close()

        #Decrypt of  AES session key
        self.rsa_cipher = PKCS1_OAEP.new(self.key_lecture)
        self.session_key = self.rsa_cipher.decrypt(self.enc_key_in_file)

        #Data decrypt using AES session key.
        self.aes_cipher = AES.new(self.session_key, AES.MODE_EAX, self.nonce)
        self.decrypt_data = self.aes_cipher.decrypt_and_verify(self.encrypted_text, self.tag)
        self.decoded_data = self.decrypt_data.decode("utf-8")
        
        #Write down the text in the same file.
        with open(self.path_to_file, "wb") as self.w_file:
            self.w_file.write(self.decoded_data)
            self.w_file.close()
        
        #End message.
        self.succesful_message = f"\n== Archivo descifrado ==\n"
        
        return self.succesful_message

    def __call__(self):
        self.files_load()


        