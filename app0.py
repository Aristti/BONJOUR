from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon app Flask !"

if __name__ == '__main__':
    app.run(debug=True)
