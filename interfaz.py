from flask import Flask, render_template, request, url_for
import oracledb
from datetime import datetime
import random

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
    try:
        image_url = url_for('static', filename='logo.jpeg')

        if request.method == 'POST':

            direccion = request.form['direccion']
            tipo = request.form['tipo']
            idCliente = request.form['idCliente']
            ID = request.form['id']
            ingredientes = request.form['ingredientes']
            
            hora_recogida = request.form['hora_recogida']
            hora_recogida = hora_recogida.replace('T', ' ')
            hora_recogida += ':00'
            hora_recogida = str(hora_recogida)




            #fecha_y_hora = datetime.strptime(fecha_hora_texto, '%Y-%m-%dT%H:%M')

            usuario = request.form['usuario']
            email = request.form['email']
            telefono = request.form['telefono']

            idMovimiento = random.randint(0, 1000000)
            
            conexion = conectar_base_de_datos()

            if conexion:
                procesar_pedido_en_base_de_datos(conexion, idCliente, ID, usuario, email, telefono, idMovimiento, direccion, tipo, ingredientes, hora_recogida)

            cerrar_conexion(conexion)
            return render_template('index.html', image_url=image_url)
                
    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

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

        sql = f"SELECT * FROM {nombre_tabla}"
        cursor.execute(sql)

        datos_tabla = cursor.fetchall()

        return datos_tabla

    except :
        print(f"Error al obtener datos de la tabla")
        return None

    finally:
        if cursor:
            cursor.close()
            
def procesar_pedido_en_base_de_datos(conexion, idCliente, id_pedido, usuario, email, telefono, idMovimiento, direccion, tipo_pedido, ingredientes, hora_recogida):
    try:
        
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()

        sentencia1 = """INSERT INTO ClienteRealizaPedido 
                 (idCliente, idPedido, usuario, email, telefono, direccion, tipoPedido, ingredientes, horaRecogida) 
                 VALUES (' """ + idCliente +""" ', ' """ + id_pedido +""" ', ' """ + usuario +""" ', ' """ + email +""" ', ' """ + telefono +""" ', ' """ + direccion +""" ', ' """+ tipo_pedido +""" ', ' """+ ingredientes +""" ',
                 TO_TIMESTAMP(' """ +hora_recogida + """ ', 'YYYY-MM-DD HH24:MI:SS'))"""

        cursor.execute(sentencia1)

        senetncia2 = """INSERT INTO ProduceVenta 
                 (idPedido,idCliente, idMovimiento,direccion, tipoPizza) 
                 VALUES (' """ + id_pedido +""" ', ' """ + idCliente +""" ', ' """ + str(idMovimiento) + """ ', ' """+ direccion +""" ', ' """ + tipo_pedido +""" ')"""

        cursor.execute(senetncia2)

        sentencia3 = """INSERT INTO GestionaPedido 
                 (idCliente, idPedido, tipoPedido, ingredientes, horaRecogida) 
                 VALUES (' """ + idCliente +""" ', ' """ + id_pedido +""" ', ' """ + tipo_pedido + """ ', ' """ +ingredientes +""" ',
                 TO_TIMESTAMP(' """ +hora_recogida + """ ', 'YYYY-MM-DD HH24:MI:SS'))"""
            
        cursor.execute(sentencia3)


        conexion.commit()
        print("Pedido procesado correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al procesar el pedido en la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

def procesar_sueldo(conexion, dni, idSueldo, iban, cantidad, fecha, nombre, apellidos, sueldo, edad, puesto):
    try:

        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()

        sentencia1 = """INSERT INTO RecibeSueldo 
                 (DNI, IDSUELDO, IBAN, Cantidad, Fecha) 
                 VALUES (' """ + dni +""" ', ' """ + idSueldo +""" ', ' """ + iban +""" ', ' """ + cantidad +""" ',
                 TO_TIMESTAMP(' """ +fecha + """ ', 'YYYY-MM-DD HH24:MI:SS'))"""

        cursor.execute(sentencia1)

        sentencia2 = """INSERT INTO EmpleadoRecibe 
                 (DNI, idSueldo, Nombre, Apellidos, Sueldo, Edad, Puesto) 
                 VALUES (' """ + dni +""" ', ' """ + idSueldo +""" ', ' """ + nombre +""" ', ' """ + apellidos +""" ', ' """+ sueldo+""" ', ' """+edad+""" ', ' """+puesto+""" ')"""

        cursor.execute(sentencia2)

        sentencia3 = """INSERT INTO EsUnGasto 
                 (idSueldo, DNI, Gasto) 
                 VALUES (' """ + idSueldo +""" ', ' """ + dni +""" ', ' """ + cantidad + """ ')"""
            
        cursor.execute(sentencia3)

        conexion.commit()
        print("Datos procesados correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al procesar los datos en la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

def procesar_proveedor(conexion, idProveedor, dineroGastado, nombre, productos):
    try:
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()
        
        sentencia1 = """INSERT INTO ProveedorProvoca 
                 (idProveedor, dineroGastado, nombre, productos) 
                 VALUES (' """ + idProveedor +""" ', ' """ + dineroGastado +""" ', ' """ + nombre +""" ', ' """ + productos +""" ')"""

        cursor.execute(sentencia1)

        conexion.commit()
        print("Datos procesados correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al procesar los datos en la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

def procesar_promocion(conexion, DNI, idPromocion, tipo, productos, nombre, F_INI, F_FIN):
    try:
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()
        
        sentencia1 = """INSERT INTO CreaPromocion 
                 (DNI, idPromocion, Tipo, Productos, Nombre, F_ini, F_fin) 
                 VALUES (' """ + DNI +""" ', ' """ + idPromocion +""" ', ' """ + tipo +""" ', ' """ + productos +""" ', ' """+nombre+""" ',
                 TO_TIMESTAMP(' """ +F_INI + """ ', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP(' """ +F_FIN + """ ', 'YYYY-MM-DD HH24:MI:SS'))"""

        cursor.execute(sentencia1)

        conexion.commit()
        print("Datos procesados correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al procesar los datos en la base de datos: {error}")
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

@app.route('/caso4.html')
def caso4():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso4.html', image_url=image_url)

@app.route('/caso5.html')
def caso5():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso5.html', image_url=image_url)

@app.route('/caso6.html')
def caso6():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso6.html', image_url=image_url)

@app.route('/produccion.html')
def Prod():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('produccion.html', image_url=image_url)

@app.route('/contabilidad.html')
def Cont():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('contabilidad.html', image_url=image_url)

@app.route('/RRHH.html')
def RRHH():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('RRHH.html', image_url=image_url)

@app.route('/marketing.html')
def Mark():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('marketing.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)