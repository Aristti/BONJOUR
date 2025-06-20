#pip install flask
#importation 
from flask import Flask, render_template, request

app = Flask(__name__)

#première route
@app.route('/')
def index():
    return render_template('index.html')

#2 eme route
@app.route('/hello', methods=['POST'])
def hello():
    prenom = request.form['prenom']
    return render_template('hello.html', prenom=prenom)

@app.route('/compte', methods=['GET', 'POST'])
def compte():
    if request.method == 'POST':  # Si formulaire envoyé
        prenom = request.form['prenom']
    else:
        prenom = request.args.get('prenom', '')
    if prenom:    
        longueur = len(prenom.strip())
        return render_template('compte.html', prenom=prenom, longueur=longueur)
    # Sinon, c'est une visite normale (GET), on affiche juste le formulaire
    return render_template('index.html')

#lancer
if __name__ == '__main__':
    app.run(debug=True)
