import mysql.connector

try:
    conexion = mysql.connector.connect(user="daw2",password="LaElipa",
                                       host="localhost",database="dwes2")
    cursor = conexion.cursor()

    query2 = "select nombre,altura from pokemon where altura>1.5"
    cursor.execute(query2)

    for fila in  cursor:
        print(fila)
    cursor.close()
    conexion.close()
except mysql.connector.Error as err:
    print(err)