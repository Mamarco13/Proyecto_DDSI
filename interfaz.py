from flask import Flask, render_template, request, url_for
import oracledb

app = Flask(__name__)
def conectar_base_de_datos():
    try:
        conexion = oracledb.connect(user="x0607565", password="x0607565", dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP) (HOST=oracle0.ugr.es)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=practbd.oracle0.ugr.es)))")
        print('conexion existosa')
        return conexion
    except:
        print("error")
        return None

def cerrar_conexion(conexion):
    if conexion:
        conexion.close()

@app.route('/')
def index():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('index.html', image_url=image_url)


@app.route('/procesar_pedido', methods=['POST'])
def procesar_pedido():
    if request.method == 'POST':
        direccion = request.form['direccion']
        tipo = request.form['tipo']
        hora = request.form['hora']
        DNI = request.form['DNI']
        ID = request.form['ID']
    conexion = conectar_base_de_datos()
    #Aqui codigo para procesar el pedido
    cerrar_conexion(conexion)
    return render_template('index.html')

    
@app.route('/mostrar_tabla', methods=['POST'])
def mostrar_tabla():
    if request.method == 'POST':
        tabla_mostrar = request.form['tabla_mostrar']

    conexion = conectar_base_de_datos()
    #Aqui codigo para mostrar la tabla en pantalla.
    cerrar_conexion(conexion)
    return render_template('index.html')

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