'''The module 'os' is used to get current work directory path.'''
import os
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA


class AesDecryptor:
    '''
    This class is used to decrypt the files encrypted with the public generated 
    by the encryption script.
    '''

    def __init__(self, private_key_file: str, file_to_decrypt: str):
        self.private_key = private_key_file
        self.encrypted_data = file_to_decrypt

    def files_load(self):
        '''
        This functions loads the encrypted file and decrypt it. Takes the path to the private
        key and the file as arguments.
        '''
        #In this test the directory for the key and the encrypted data is the same.
        path_cwd = os.getcwd()
        path_to_key = str(path_cwd + "/" + self.private_key)
        path_to_file = str(path_cwd + "/" + self.encrypted_data)
        print(f"\n--> {path_to_file}\n--> {type(path_to_file)}\n")
        #Instances for private key lecture and division of encrypted data.
        data_file = open(path_to_file, "rb")
        instace_for_key = open(path_to_key, "rb").read()
        key_lecture = RSA.import_key(instace_for_key)
        #Lecture of differents parts of the data.
        enc_key_in_file, nonce, tag, encrypted_text = \
              [data_file.read(x) for x in (key_lecture.size_in_bytes(), 16, 16, -1)]
        print(f"\n{enc_key_in_file}\n\n{nonce}\n\n{tag}\n\n{encrypted_text}\n") #For debug
        data_file.close()
        #Decrypt of  AES session key
        rsa_cipher = PKCS1_OAEP.new(key_lecture)
        session_key = rsa_cipher.decrypt(enc_key_in_file)
        #Data decrypt using AES session key.
        aes_cipher = AES.new(session_key, AES.MODE_EAX, nonce)
        decrypt_data = aes_cipher.decrypt_and_verify(encrypted_text, tag)
        decoded_data = decrypt_data#.decode("utf-8")
        #Write down the text in the same file.
        with open(path_to_file, "wb") as write_file:
            write_file.write(decoded_data)
            write_file.close()
        #End message and retrun.
        succesful_message = "\n== Archivo descifrado ==\n"
        return succesful_message

    def __call__(self):
        self.files_load()

#The next lines of code will be for testig the class only.
#def main():
#    '''
#    main function is used to take the names of the file that will be pased
#    as arguments to the decryption class.
#    THIS FUNCTION IS ONLY USED TO TEST THE SCRIPT.
#    EVEN THE if __name__ == '__main__'.
#
#    '''
#    key_file = input("\nEnter the name of the private key: ")
#    data_file = input("Enter the name of the file to decrypt: ")
#    new_class_instance = AesDecryptor(key_file, data_file)
#    new_class_instance()
#
#if __name__ == '__main__':
#    main()
