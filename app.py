from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('distancia-form.html')


@app.route('/calcularDistancia/', methods=['POST'])
def calcular_distancia():
    distancia = int(request.form['distancia'])
    return render_template('resultado-distancia.html', distancia=distancia)


if __name__ == '__main__':
    app.run(host="https://oibr.herokuapp.com", debug=False)
