# File cipher
File cipher program is a simple RSA-AES cipher and decipher. It uses Flask with FlaskWebGui for the user interface to work like a normal program in a desktop environment.
The interface is simple with a main page and two options, cipher and decipher. 

In the cipher page you just need to select the file an enter the bytes long for the encryption key. In the decipher page you have to select the encrypted file and the corresponding private key. **The file will be modificated itself, so for extra caution just make a copy and save it**.

When the program search for the file and the key, both files should be in the corresponding directory. It is:
* "files": This directory should be inside the main directory were the main script is allocated. If doesn't exist should be created. Then you should store your files to cipher there before the encryption.
* "keys": This directory is were the public an private key will be stored. To know wich key is for any file the program will save the keys inside a directory were the name is "dir_" plus the file name.
There you sholud be able to find both keys. 

#### For the main directory the folder tree will be:

    -> files
        -> file1
        -> file2
        ...

    -> keys
        -> dir_file1
            -> private_key_file1.pem
            -> public_key_file1.pem
            -> timestamp.txt

        -> dir_file2
            -> private_key_file2.pem
            -> public_key_file2.pem
            -> timestamp.txt
        ...

### Cipher

Within the cipher page will be two elements, one is to select the file the user want to encrypt. This file should be inside the "files" directory creted by the user in the directory were the python main script is executed. In the development of the program it was tested with plain text files only. The other element is the logitude of the key expressed in bytes. Today the recommneded longitude is 2048 or higher, for this the program will not allow the user enter a value less than 2048. 

When all the elements are complete, press the cipher button and then the program will create both keys (public and private), the timestamp corresponding to the key creation event, encrypt  the file and tell the user if the file was encrypted succesfully.

For now if the encription fails in any part of the program it will show a "Internal server error" message. In this case the user should check if the file was encryted in wich case both keys should be created too.

### Decipher

In the decipher page, like the cipher page the user will fild two elemnts. The first one works exactly like the first element encountered in the cipher page. The user should select the file that want to decrypt in the "files" directory. The second element in the page is the selection of the private key that was genereted in the encryption proccess. The private key is located whitin a directory with the name of the file encrypted before. This directory is in the "keys" directory.

In case neither, file or key, is found the program will inform that one of the file is missing. In wich case the file cannot be decrypted.

If the process is succesfull then the file will be decrypted an saved in the same path. Both keys will still exist, it depends of the user erase them or not. If the user don't erase the keys then cannot use the same file name because it will produce an error in the directory created for the keys.