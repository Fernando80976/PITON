import mysql.connector

try:
    conexion = mysql.connector.connect(user="daw2",password="LaElipa",
                                       host="localhost",database="dwes2")
    cursor = conexion.cursor()
    # query1=cursor.execute("select * from pokemon")

    #   METODO 1 metodo para recorrer
    # for fila in cursor:
    #     print(fila)
    #     print(fila[1])

    #   METODO 2 si quieres los datos de una
    # lista = cursor.fetchall()#devuelve l
    # print(lista)

    #   METODO 3
    query2 = "select nombre,altura from pokemon where altura>1.5"
    cursor.execute(query2)
    # for (pokemon,id) in cursor:
    #     print(id,"-",pokemon)

    # query1="UPDATE pokemon SET nombre='Pokemon Cachas' where nombre='Mewtwo'"
    # cursor.execute(query1)
    # print(cursor.rowcount,"Filas afectadas por el query")
    # query2="select * from pokemon"
    # cursor.execute(query2)
    for fila in  cursor:
        print(fila)
    cursor.close()#hay qu cerrarlo antes de la bbdd
    conexion.close()
except mysql.connector.Error as err:
    print(err)