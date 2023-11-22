# DDSI
### Iniciar interfaz
Ejecutar el script de arranque: **arranque_interfaz.sh**.

###Distribución de archivos
**interfaz.py** es el archivo "guía" programado en python y tiene todo el mapeado de htmls a los que acceder y la conexión con las BD en la que le pasemos las variables para realizar las acciones
**main.py** crea la BD

Archivos dentro de templates; son los html:

**layout.html** es la plantilla de las páginas

**index.html** es la página principal desde la que se accede a todas las operaciones de la interfaz y a la que se vuelve al realizarlas (Cuando tengamos bien programado lo de mostrar tabla habrá que hacer que vaya a una página en la que esté la tabla, y sería interesante crear una paginilla de confirmacion antes de volver aquí para hacerlo todo menos violento xd).

**caso1.html** es el de inserción y borrado de tuplas (aun incompleto)

**caso2.html** es el de nuevos pedidos

**caso3.html** es el de mostrar la tabla
