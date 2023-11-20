from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    carta = ['Margharita', 'Prosciutto', 'Diavola', 'Marinera', 'Rucula', 'Patatina']
    data={
        'Titulo':'Pizzeria Ave Phoenix',
        'bienvenida':'Saludos!',
        'carta':carta,
        'numero_carta':len(carta)

    }
    if request.method == 'POST':
        direccion = request.form['direccion']
        tipo = request.form['tipo']
        hora = request.form['hora']
        tabla_mostrar = request.form['tabla_mostrar']
    return render_template('index.html', data = data)

@app.route('/caso1.html')
def caso1():
    return render_template('caso1.html')
@app.route('/caso2.html')
def caso2():
    return render_template('caso2.html')
@app.route('/caso3.html')
def caso3():
    return render_template('caso3.html')

if __name__ == '__main__':
    app.run(debug = True, port = 5000)