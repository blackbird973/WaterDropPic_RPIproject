from flask import Flask, request, render_template

import time                           #ajout mat


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['valeur']
    processed_text = text.upper()   

    time.sleep(float(processed_text))   #le 'processed_text" et une chaine de caractere (string) et le sleep prend seulement les floats il faut donc convertir le 'text_processed' en float
    
    return render_template("bienvenue.html")

if __name__ == '__main__':
    app.run()    #remplacer par app.run(host='127.0.0.5')  et mettez l'ip voulue
