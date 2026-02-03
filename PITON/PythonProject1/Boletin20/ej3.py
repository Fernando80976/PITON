import mysql.connector

try:
    conexion = mysql.connector.connect(user="root",password="fere",
                                       host="localhost",database="pokemondb")
    cursor = conexion.cursor()
    query2 = "select nombre from pokemon where peso>200"
    cursor.execute(query2)
    nombres = [fila[0] for fila in cursor]  # lista de nombres
    for nombre in nombres:

        mayusculas = nombre.upper()
        query3="UPDATE pokemon SET nombre=UPPER(nombre) WHERE peso>200"
        cursor.execute(query3)
        print(mayusculas)

    conexion.commit()
    print(cursor.rowcount, "registros modificados")
    cursor.close()
    conexion.close()
except mysql.connector.Error as err:
    print(err)