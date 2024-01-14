from flask import Flask, render_template, request, url_for
import oracledb
from datetime import datetime
import random

# vector_id_sueldo[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def asignarIDSueldo():
    for i in vector_id_sueldo.len():
        if vector_id_sueldo[i] == 0:
            vector_id_sueldo[i] = 1
            return i

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


"""@app.route('/procesar_pedido', methods=['POST'])
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
            return render_template('index.html', image_url=image_url)git
                
    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=image_url)"""

@app.route('/insertarPedido', methods=['POST'])
def procesar_pedido():
    try:
        image_url = url_for('static', filename='logo.jpeg')

        if request.method == 'POST':
            direccion = request.form['direccion']
            tipo = request.form['tipo']
            idCliente = request.form['idCliente']
            idPedido = request.form['idPedido']
            ingredientes = request.form['ingredientes']
            
            hora_recogida = request.form['hora_recogida']
            hora_recogida = hora_recogida.replace('T', ' ')
            hora_recogida += ':00'
            hora_recogida = str(hora_recogida)

            usuario = request.form['usuario']
            email = request.form['email']
            telefono = request.form['telefono']

            idMovimiento = request.form['idMovimiento']

            nombreCliente = request.form['nombreCliente']
            apellidosCliente = request.form['apellidosCliente']
            vip = request.form['vip']
            
            conexion = conectar_base_de_datos()

            if conexion:
                procesar_pedido_en_base_de_datos(conexion, idCliente, idPedido, usuario, email, telefono, idMovimiento, direccion, tipo, ingredientes, hora_recogida, nombreCliente, apellidosCliente, vip)

            cerrar_conexion(conexion)
            return render_template('index.html', image_url=image_url)
                
    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=image_url)

"""@app.route('/insertarSueldo', methods=['POST'])
def procesar_sueldo():
    try:
        image_url = url_for('static', filename='logo.jpeg')

        if request.method == 'POST':
            dni = request.form['dni']
            idSueldo = request.form['idSueldo']
            iban = request.form['iban']
            cantidad = request.form['cantidad']
            
            fecha = request.form['fecha']
            fecha = fecha.replace('T', ' ')
            fecha += ':00'
            fecha = str(fecha)

            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            sueldo = request.form['sueldo']
            edad = request.form['edad']
            puesto = request.form['puesto']

            conexion = conectar_base_de_datos()

        if conexion:
            procesar_sueldo(conexion, dni, idSueldo, iban, cantidad, fecha, nombre, apellidos, sueldo, edad, puesto)
            
        cerrar_conexion(conexion)
        return render_template('index.html', image_url=image_url)
                
    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=image_url)"""

@app.route('/es-un-Gasto', methods=['POST'])
def procesar_sueldo():
    try:
        image_url = url_for('static', filename='logo.jpeg')

        if request.method == 'POST':
            DineroGastado = request.form['Din_Gastado']
            CantidadProducto = request.form['Cantidad_Prod']
            Frecuencia = request.form['Frecuencia']
            idSueldo = asignarIDSueldo()
            conexion = conectar_base_de_datos()

        if conexion:
            procesar_gasto(conexion, idSueldo, DineroGastado, CantidadProducto, Frecuencia)
            
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
            
def procesar_pedido_en_base_de_datos(conexion, idCliente, id_pedido, usuario, email, telefono, idMovimiento, direccion, tipo_pedido, ingredientes, hora_recogida, nombre, apellidos, vip):
    try:
        
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()

        sentencia1 = """INSERT INTO ClienteRealizaPedido 
                 (idCliente, idPedido, usuario, email, telefono, direccion, tipoPedido, ingredientes, horaRecogida, nombre, apellidos, vip) 
                 VALUES (' """ + idCliente +""" ', ' """ + id_pedido +""" ', ' """ + usuario +""" ', ' """ + email +""" ', ' """ + telefono +""" ', ' """ + direccion +""" ', ' """+ tipo_pedido +""" ', ' """+ ingredientes +""" ',
                 TO_TIMESTAMP(' """ +hora_recogida + """ ', 'YYYY-MM-DD HH24:MI:SS'), ' """ + nombre + """ ' , ' """ + apellidos + """ ', ' """ + vip + """ ' )"""

        cursor.execute(sentencia1)

        senetncia2 = """INSERT INTO ProduceVenta 
                 (idPedido,idCliente, idMovimiento,direccion, tipoPizza, nombre, clienteVIP) 
                 VALUES (' """ + id_pedido +""" ', ' """ + idCliente +""" ', ' """ + idMovimiento + """ ', ' """+ direccion +""" ', ' """ + tipo_pedido + """ ', ' """ + nombre + """ ', ' """ + vip + """ ')"""

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


def procesar_gasto(conexion, DineroGastado, CantidadProducto, Frecuencia):
    try:

        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()

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


@app.route('/eliminarSueldo', methods=['POST'])
def eliminar_sueldo_route():
    try:
        if request.method == 'POST':
            idSueldo = request.form['idSueldo']

            conexion = conectar_base_de_datos()

            if conexion:
                eliminar_sueldo(conexion, idSueldo)

            cerrar_conexion(conexion)
            return render_template('index.html', image_url=url_for('static', filename='logo.jpeg'))

    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=url_for('static', filename='logo.jpeg'))

def eliminar_sueldo(conexion, idSueldo):
    try:
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()

        # Eliminar de la tabla RecibeSueldo
        sentencia1 = """DELETE FROM RecibeSueldo WHERE IDSUELDO = '""" + idSueldo + """'"""
        cursor.execute(sentencia1)

        # Eliminar de la tabla EmpleadoRecibe
        sentencia2 = """DELETE FROM EmpleadoRecibe WHERE idSueldo = '""" + idSueldo + """'"""
        cursor.execute(sentencia2)

        # Eliminar de la tabla EsUnGasto
        sentencia3 = """DELETE FROM EsUnGasto WHERE idSueldo = '""" + idSueldo + """'"""
        cursor.execute(sentencia3)

        conexion.commit()
        print(f"Sueldo con idSueldo {idSueldo} eliminado correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al eliminar el sueldo de la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()


def procesar_proveedor(conexion, idProveedor, dineroGastado, nombre, productos):
    try:
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()
        
        sentencia1 = """INSERT INTO CreaPromocion 
                 (idPromocion, Tipo, Productos, Nombre, F_ini, F_fin) 
                 VALUES (:idPromocion, :tipo, :productos, :nombre, TO_TIMESTAMP(:F_INI, 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP(:F_FIN, 'YYYY-MM-DD HH24:MI:SS'))"""

        cursor.execute(sentencia1, {'idPromocion': idPromocion, 'tipo': tipo, 'productos': productos, 'nombre': nombre, 'F_INI': F_INI, 'F_FIN': F_FIN})

        conexion.commit()
        print("Datos procesados correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al procesar los datos en la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

#MARKETING 
            
def procesar_promocion(conexion, idPromocion, tipo, productos, nombre, F_INI, F_FIN):
    try:
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()
        
        sentencia1 = """INSERT INTO CreaPromocion 
                 (idPromocion, Tipo, Productos, Nombre, F_ini, F_fin) 
                 VALUES (' """ + idPromocion +""" ', ' """ + tipo +""" ', ' """ + productos +""" ', ' """+nombre+""" ',
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

# Insertar promocion
@app.route('/insertarPromocion', methods=['POST'])
def insertar_promocion():
    try:
        image_url = url_for('static', filename='logo.jpeg')

        if request.method == 'POST':
            idPromocion = request.form['idPromocion']
            tipo = request.form['Tipo']
            productos = request.form['Productos']
            nombre = request.form['Nombre']
            F_INI = request.form['F_ini']
            F_FIN = request.form['F_fin']
            
            conexion = conectar_base_de_datos()

            if conexion:
                procesar_promocion(conexion, idPromocion, tipo, productos, nombre, F_INI, F_FIN)

            cerrar_conexion(conexion)
            return render_template('index.html', image_url=image_url)
                
    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=image_url)

# Eliminar promocion

@app.route('/EliminaC8', methods=['POST'])
def eliminar_promo_route():
    try:
        if request.method == 'POST':
            idPromocion = request.form['idPromocion']

            conexion = conectar_base_de_datos()

            if conexion:
                eliminar_promo(conexion, idPromocion)

            cerrar_conexion(conexion)
            return render_template('index.html', image_url=url_for('static', filename='logo.jpeg'))

    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=url_for('static', filename='logo.jpeg'))


def eliminar_promo(conexion, idPromocion):
    try:
        conexion = conectar_base_de_datos()
        cursor = conexion.cursor()

        sentencia1 = """DELETE FROM CreaPromocion WHERE idPromocion = '""" + idPromocion + """'"""
        cursor.execute(sentencia1)

        conexion.commit()
        print(f"Promoción con idPromocion {idPromocion} eliminada correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al eliminar la promoción de la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

# Eliminar cliente

@app.route('/EliminaC20', methods=['POST'])
def eliminar_cliente_route():
    try:
        if request.method == 'POST':
            idCliente = request.form['idCliente']
            print(f"ID Cliente recibido: {idCliente}")


            conexion = conectar_base_de_datos()

            if conexion:
                eliminar_cliente(conexion, idCliente)

            cerrar_conexion(conexion)
            return render_template('index.html', image_url=url_for('static', filename='logo.jpeg'))

    except Exception as e:
        print(f"Error no manejado: {str(e)}")
        return render_template('error.html', mensaje=f"Error no manejado: {str(e)}")

    return render_template('index.html', image_url=url_for('static', filename='logo.jpeg'))


def eliminar_cliente(conexion, idCliente):
    try:
        cursor = conexion.cursor()

        sentencia1 = """DELETE FROM GestionaPedido WHERE idCliente = '""" + idCliente + """'"""
        cursor.execute(sentencia1)

        sentencia2 = """DELETE FROM ProduceVenta WHERE idCliente = '""" + idCliente + """'"""
        cursor.execute(sentencia2)
        
        sentencia3 = """DELETE FROM ClienteRealizaPedido WHERE idCliente = '""" + idCliente + """'"""
        cursor.execute(sentencia3)



        conexion.commit()
        print(f"Cliente con idCliente {idCliente} eliminado/a correctamente")
        print("Consulta SQL:", cursor.statement)

    except Exception as error:
        print(f"Error al eliminar el cliente de la base de datos: {error}")
        conexion.rollback()

    finally:
        if cursor:
            cursor.close()

# FIN MARKETING


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

@app.route('/caso7.html')
def caso7():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso7.html', image_url=image_url)

@app.route('/caso8.html')
def caso8():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso8.html', image_url=image_url)

@app.route('/caso9.html')
def caso9():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso9.html', image_url=image_url)

@app.route('/caso10.html')
def caso10():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso10.html', image_url=image_url)

@app.route('/caso11.html')
def caso11():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso11.html', image_url=image_url)

@app.route('/caso12.html')
def caso12():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso12.html', image_url=image_url)

@app.route('/caso13.html')
def caso13():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso13.html', image_url=image_url)

@app.route('/caso14.html')
def caso14():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso14.html', image_url=image_url)

@app.route('/caso15.html')
def caso15():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso15.html', image_url=image_url)

@app.route('/caso19.html')
def caso19():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso19.html', image_url=image_url)

@app.route('/caso20.html')
def caso20():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso20.html', image_url=image_url)

@app.route('/caso21.html')
def caso21():
    image_url = url_for('static', filename = 'logo.jpeg')
    return render_template('caso21.html', image_url=image_url)

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