from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Esto es una descripción breve: retorno de información

if __name__ == '__main__':
    app.run(debug=True)

# Esto es un archivo del documento en código Python