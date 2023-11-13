from flask import Flask, request, flash
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI
from tests import RSA_AES_file_dec as Decryption #import decrytpion module.
from tests import RSA_AES_file_Enc as Encryption #import encryption module.

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
    witch the user wants to cipher and the bytes used 
    for the encryption. 
    '''
    new_message = 'Página abierta.'
    flash(new_message, 'welcome')
    if request.method == 'POST':
        file = request.form['file_path']
        bytes_for_key = request.form['bytes_long']
        new_new_message_for_test_only = 'hola!'
        flash(new_new_message_for_test_only)
        #return render_template('cipher_page.html')
    return render_template('cipher_page.html')

@app.route("/decipher_page", methods = ["GET", "POST"])
def decipher():
    '''
    The decipher function calls the decription module RSA_AES.
    The module recives tow arguments, the first is the path to 
    the cipher file and the second argument is the path to the 
    private key used for decipher the AES encryption in the file. 
    '''

    return render_template('decipher_page.html')



if __name__ == "__main__":
  # If you are debugging you can do that in the browser:
    #app.run(debug=True)
   #If you want to view the flaskwebgui window:
    FlaskUI(
      app = app,
      server = "flask",
      browser_path = "/usr/bin/chromium",
      width = 400,
      height = 320,
      port=5000
    ).run()