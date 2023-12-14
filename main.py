import oracledb

try:
    conexion = oracledb.connect(user="x6861240", password="x6861240", dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP) (HOST=oracle0.ugr.es)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=practbd.oracle0.ugr.es)))")

    print('concexion existosa')
except:
    print("error")
    

cursor = conexion.cursor()

#Insertar Datos

cursorInsertar = conexion.cursor()

cursorInsertar.execute("Drop table EsUnGasto")
cursorInsertar.execute("Drop table GestionaPedido")
cursorInsertar.execute("Drop table EmpleadoRecibe")
cursorInsertar.execute("Drop table ProduceVenta")
cursorInsertar.execute("Drop table ClienteRealizaPedido")
cursorInsertar.execute("Drop table RecibeSueldo")
cursorInsertar.execute("Drop table ProveedorProvoca")
cursorInsertar.execute("Drop table CreaPromocion")

#Tabla RecibeSueldo
consulta = """CREATE TABLE RecibeSueldo(
    DNI VARCHAR2(9) UNIQUE,
    IDSUELDO VARCHAR2(15) UNIQUE,
    IBAN VARCHAR2(24),
    Cantidad NUMBER,
    Fecha TIMESTAMP,
    PRIMARY KEY(DNI,IDSUELDO)) """

cursorInsertar.execute(consulta)

#Tabla EmpleadoRecibe
consulta = """CREATE TABLE EmpleadoRecibe(
    DNI VARCHAR2(9) UNIQUE,
    idSueldo VARCHAR2(15),
    Nombre VARCHAR2(20),
    Apellidos VARCHAR2(50), 
    Sueldo NUMBER,
    Edad NUMBER,
    Puesto VARCHAR2(30),
    PRIMARY KEY (DNI,idSueldo),
    FOREIGN KEY (DNI,idSueldo) REFERENCES RecibeSueldo(DNI,IDSUELDO)) """

cursorInsertar.execute(consulta)

#CrearPromocion
consulta = """CREATE TABLE CreaPromocion (
    DNI VARCHAR2(9),
    idPromocion NUMBER,
    Tipo VARCHAR2(20),
    Productos VARCHAR2(500),
    Nombre VARCHAR2(20),
    F_ini TIMESTAMP,
    F_fin TIMESTAMP,
    PRIMARY KEY(DNI,idPromocion)) """

cursorInsertar.execute(consulta)

#Tabla ClienteRealizaPedido
consulta = """CREATE TABLE ClienteRealizaPedido(
    idCliente VARCHAR2(15),
    idPedido VARCHAR2(15) UNIQUE,
    usuario VARCHAR2(12) UNIQUE NOT NULL,
    email VARCHAR2(25) UNIQUE NOT NULL,
    telefono NUMBER(9) UNIQUE,
    nombre VARCHAR2(20),
    apellidos VARCHAR2(100),
    VIP NUMBER(1),
    direccion VARCHAR2(50),
    tipoPedido VARCHAR2(50),
    ingredientes VARCHAR2(20),
    horaRecogida TIMESTAMP,
    PRIMARY KEY(idCliente, idPedido)) """

cursorInsertar.execute(consulta)

#Tabla ProduceVenta
consulta = """CREATE TABLE ProduceVenta(
    idPedido VARCHAR2(15),
    idCliente VARCHAR2(15),
    idMovimiento VARCHAR2(15) UNIQUE,
    nombre VARCHAR2(50),
    clienteVIP NUMBER(1),
    direccion VARCHAR2(50),
    tipoPizza VARCHAR2(15),
    FOREIGN KEY(idPedido, idCliente)
    REFERENCES ClienteRealizaPedido(idPedido,idCliente),
    PRIMARY KEY(idPedido, idCliente, idMovimiento)) """

cursorInsertar.execute(consulta)

#Tabla EsUnGasto
consulta = """CREATE TABLE EsUnGasto(
    idSueldo VARCHAR2(15),
    DNI VARCHAR2(15),
    Gasto NUMBER,
    FOREIGN KEY (DNI, idSueldo) REFERENCES RECIBESUELDO (DNI, IDSUELDO),
    PRIMARY KEY(idSueldo, DNI))"""

cursorInsertar.execute(consulta)

#Tabla ProveedorProvoca
consulta = """CREATE TABLE ProveedorProvoca(
    idProveedor VARCHAR2(15),
    dineroGastado NUMBER,
    nombre VARCHAR2(20),
    productos VARCHAR2(200),
    PRIMARY KEY(dineroGastado, idProveedor)) """

cursorInsertar.execute(consulta)

#Tabla GestionaPedido
consulta = """CREATE TABLE GestionaPedido(
    idCliente VARCHAR2(9),
    idPedido VARCHAR2(15),
    tipoPedido VARCHAR2(50),
    ingredientes VARCHAR2(500),
    horaRecogida TIMESTAMP,
    FOREIGN KEY (idPedido, idCliente) REFERENCES ClienteRealizaPedido (idPedido, idCliente),
    PRIMARY KEY(idPedido)) """

cursorInsertar.execute(consulta)

conexion.commit()
cursorInsertar.close()

cursor.close()
conexion.close()
 