from flask import Flask, render_template, request, url_for
import oracledb

app = Flask(__name__)
def conectar_base_de_datos():
    try:
        conexion = oracledb.connect(user="x6861240", password="x6861240", dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP) (HOST=oracle0.ugr.es)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=practbd.oracle0.ugr.es)))")
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
    image_url = url_for('static', filename = 'logo.jpeg')
    if request.method == 'POST':
        direccion = request.form['direccion']
        tipo = request.form['tipo']
        hora = request.form['hora']
        DNI = request.form['DNI']
        ID = request.form['ID']
    conexion = conectar_base_de_datos()
    if conexion:
        procesar_pedido_en_base_de_datos(conexion, direccion, tipo, hora)
    cerrar_conexion(conexion)
    return render_template('index.html', image_url=image_url)

    
@app.route('/mostrar_tabla', methods=['POST'])
def mostrar_tabla():
    image_url = url_for('static', filename = 'logo.jpeg')
    if request.method == 'POST':
        tabla_mostrar = request.form['tabla_mostrar']

    conexion = conectar_base_de_datos()
    if conexion:
        try:
            datos_tabla = obtener_datos_tabla(conexion, tabla_mostrar)
            return render_template('mostrar_tabla.html', datos_tabla=datos_tabla, image_url=image_url)
             
        except Exception as e:
            print(f"Error al ejecutar la consulta: {str(e)}")
            return render_template('error.html', mensaje=f"Error al obtener datos de la tabla")

        finally:
            cerrar_conexion(conexion)
    return render_template('index.html', image_url=image_url)

def obtener_datos_tabla(conexion, nombre_tabla):
    try:
        cursor = conexion.cursor()

        # Supongamos que deseas mostrar todos los datos de la tabla 'pedidos'
        sql = f"SELECT * FROM {nombre_tabla}"
        cursor.execute(sql)

        # Recupera todos los resultados
        datos_tabla = cursor.fetchall()

        return datos_tabla

    except :
        print(f"Error al obtener datos de la tabla")
        return None

    finally:
        if cursor:
            cursor.close()

def procesar_pedido_en_base_de_datos(conexion, dni, id_pedido, tipo_pedido):
    try:
        cursor = conexion.cursor()

        sql = "INSERT INTO GestionaPedido (DNI, idPedido, tipoPedido) VALUES (:1, :2, :3)"
        cursor.execute(sql, (dni, id_pedido, tipo_pedido))
        
        conexion.commit()
        print("Pedido procesado correctamente")

    except Exception as error:
        print(f"Error al procesar el pedido en la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

@app.route('/caso1.html')
def caso1():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso1.html', image_url=image_url)
@app.route('/caso2.html')
def caso2():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso2.html', image_url=image_url)
@app.route('/caso3.html')
def caso3():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso3.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)