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

#lancer
if __name__ == '__main__':
    app.run(debug=True)
