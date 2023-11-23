import oracledb

try:
    conexion = oracledb.connect(user="x6861240", password="x6861240", dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP) (HOST=oracle0.ugr.es)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=practbd.oracle0.ugr.es)))")

    print('conexion existosa')
except:
    print("error")
    

cursor = conexion.cursor()

#Insertar Datos

cursorInsertar = conexion.cursor()

#Tabla GestionaPedido
consulta = """CREATE TABLE GestionaPedido(
    DNI VARCHAR2(9),
    idPedido VARCHAR2(15),
    tipoPedido VARCHAR2(50),
    ingredientes VARCHAR2(500),
    horaRecogida TIMESTAMP,
    FOREIGN KEY (DNI) REFERENCES EmpleadoRecibe(DNI),
    FOREIGN KEY (idPedido) REFERENCES ClienteRealizaPedido (idPedido),
    PRIMARY KEY(idPedido, DNI)) """

cursorInsertar.execute(consulta)
# Inserción en RecibeSueldo
cursorInsertar.execute("INSERT INTO RecibeSueldo VALUES ('123456789', 'IDSUELDO001', 'ES0123456789012345678901', 3000, TO_DATE('2023-11-23', 'YYYY-MM-DD'))")

# Inserción en EmpleadoRecibe
cursorInsertar.execute("INSERT INTO EmpleadoRecibe VALUES ('123456789', 'IDSUELDO001', 'Juan', 'Perez', 3000, 25, 'Cocinero')")

# Inserción en CreaPromocion
cursorInsertar.execute("INSERT INTO CreaPromocion VALUES ('987654321', 1, 'Descuento', 'Pizza Margarita', 'Promo1', TO_DATE('2023-11-23', 'YYYY-MM-DD'), TO_DATE('2023-12-23', 'YYYY-MM-DD'))")

# Inserción en ClienteRealizaPedido
cursorInsertar.execute("INSERT INTO ClienteRealizaPedido VALUES ('CLIENTE001', 'PEDIDO001', 'user1', 'user1@example.com', '123456789', 'NombreCliente', 'ApellidosCliente', 1, 'DireccionCliente', 'Delivery', 'Jamón, Queso', TO_TIMESTAMP('2023-11-23 18:00:00', 'YYYY-MM-DD HH24:MI:SS'))")

# Inserción en ProduceVenta
cursorInsertar.execute("INSERT INTO ProduceVenta (idPedido, idCliente, idMovimiento, nombre, clienteVIP, direccion, tipoPizza) VALUES ('PEDIDO001', 'CLIENTE001', 'MOVIMIENTO001', 'Pizza Pepperoni', 0, 'DireccionCliente', 'Pepperoni')")

# Inserción en EsUnGasto
cursorInsertar.execute("INSERT INTO EsUnGasto VALUES ('IDSUELDO001', 'MOVIMIENTO001', 20.0, 1, 1)")

# Inserción en ProveedorProvoca
cursorInsertar.execute("INSERT INTO ProveedorProvoca VALUES ('PROVEEDOR001', 500.0, 'Proveedor1', 'ProductosProveedor1')")

# Inserción en GestionaPedido
cursorInsertar.execute("INSERT INTO GestionaPedido VALUES ('123456789', 'PEDIDO001', 'Delivery', 'Jamón, Queso', TO_TIMESTAMP('2023-11-23 18:00:00', 'YYYY-MM-DD HH24:MI:SS'))")

# Guardar cambios
conexion.commit()

# Cerrar cursores y conexión
cursorInsertar.close()
cursor.close()
conexion.close()