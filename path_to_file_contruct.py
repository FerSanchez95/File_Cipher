import os
import time
from typing import Any 

class Constructor:
    '''
        The constructor class will create the path to different files depending on what script 
        is performing. 
        
        Methods:
        -------
            * For Encryptor script it will be using "CreateKeyDir" method.
            
                This method will create a directory in the keys directory
                with the name of the file and then return the path to recently 
                create directory. The encryptor scrip then will store the keys 
                in that path.
                
            * For Decryptor script it will be using "ReadKeyPath method".
            
                This method took the given file name and private key name to create
                the path that will be used for the decipher script to locate and use 
                both file and key.
    '''
    def __init__(self, *args, **kwargs) -> None:
        self.name = args[0]
        self.key = args[1] 
        self.working_dir = os.getcwd()
        
    def FilePath(self):
        '''Creates the path to files directory.'''
        wornking_file = str(self.working_dir + "\\files\\" + self.name)
        return wornking_file
    
    def CreateKeyDir(self):
        '''
            CreateKeyDir - Create Key directory, is a method use to create the directories 
            for the keys from the name of the file that should be encrypted. With a given
            file name the method will create a directory within the keys directory and will pass
            this path to the encryption script that creates the public and private keys.
            The name of the file will appear in the file name of each key.
        '''
        working_cipher_file = self.FilePath()
        key_dir_name = "dir_" + self.name
        path_to_dir = self.working_dir + "\\keys\\" + key_dir_name
        os.mkdir(path_to_dir, mode = 555)
        path_public_key = path_to_dir + "\\" + "public_key_" + self.name + ".pem"
        path_private_key = path_to_dir + "\\"  + "private_key_" + self.name + ".pem"
        
        return working_cipher_file, path_to_dir, path_public_key, path_private_key
    
    def ReadKeyPath(self):
        '''
        PrivateKeyPath method creates the path used by the decipher script to locate the private
        key specific for the encripted file.
        '''
        working_cipher_file = self.FilePath()
        key_dir_name = "dir_" + self.name
        path_to_key_dir = self.working_dir + "\\keys\\" + key_dir_name        
        private_key_to_use = str(path_to_key_dir + "\\" + self.key)
        
        return working_cipher_file, private_key_to_use
