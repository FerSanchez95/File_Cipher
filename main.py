import os
from flask import Flask, request, flash
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI
from RSA_AES_file_dec import AesDecryptor as Decryption
from RSA_AES_file_Enc import AesEncryptor as Encryption 
from path_to_file_contruct import Constructor

app = Flask(__name__)
app.secret_key = b'=$%$)JrwerweTW)#"fdosejr=(3)'
ui = FlaskUI(app)

@app.route("/", methods = ["GET", "POST"])
def index():
    '''
    The index function just show two functions
    that con be used, cipher and decipher.
    '''
    return render_template('index.html')

@app.route("/cipher_page", methods=['GET', 'POST'])
def cipher():
    '''
    The cipher function calls the encription module 
    RSA_AES. Recives two arguments, the path to the file 
    that the user wants to cipher and the bytes used 
    for the encryption. 
    '''
    if request.method == 'GET':
      new_message = f'Ingrese el archivo que desea cifrar y el número de bytes para la llave de cifrado.'
      flash(new_message)
      
    if request.method == 'POST':
        try:
            file_name = request.form['file_path']
            bytes_for_key = int(request.form['bytes_long'])
            create_new = Constructor(file_name, None)
            path_to_cipher_file = create_new.FilePath()
            
            #if the file doesn't exist send error message.
            if not os.access(path_to_cipher_file, os.F_OK):
                raise FileNotFoundError
        
        except FileNotFoundError:
            not_found_error = "El archivo no fue encontrado."
            flash(not_found_error)
            
        except ValueError:
            no_integer_error = "El número ingresado debe ser un número entero."
            flash(no_integer_error)

        else:
            cipher_file = Encryption(file_name, bytes_for_key)
            cipher_file()
            flash(cipher_file)

    return render_template('cipher_page.html')

@app.route("/decipher_page", methods = ["GET", "POST"])
def decipher():
    '''
    The decipher function calls the decription module RSA_AES.
    The module recives tow arguments, the first is the path to 
    the cipher file and the second argument is the path to the 
    private key used for decipher the AES encryption in the file. 
    '''
    if request.method == 'GET':
      new_message = 'Recuerde cargar la llave privada correcta.'
      flash(new_message)
      
    if request.method == 'POST':
        try:
            encrypted_file = request.form['cipher_file_path']
            key_file = request.form['private_key_path']
            create_new = Constructor(encrypted_file, key_file)
            path_to_key, path_to_encrypted_file = create_new.ReadKeyPath()
            if not os.access(path_to_encrypted_file, os.F_OK):
                raise FileNotFoundError
            if not os.access(path_to_key, os.F_OK):
                raise FileNotFoundError
        
        except FileNotFoundError:
            files_not_found_error = "El archivo cifrado o la llave privada no fueron encontrados."
            flash(files_not_found_error)

        else:
            decipher_file = Decryption(encrypted_file, key_file)
            decipher_file()
            flash(decipher_file)

    return render_template('decipher_page.html')



if __name__ == "__main__":
  # If you are debugging you can do that in the browser:
    #app.run(debug=True)
   #If you want to view the flaskwebgui window:
    FlaskUI(
      app = app,
      server = "flask",
      #browser_path = "/usr/bin/chromium"
      browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome",
      width = 410,
      height = 360,
      port=5000
    ).run()