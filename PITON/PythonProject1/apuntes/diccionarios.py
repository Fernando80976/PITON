dict1={"nombre":"Jose Maria","edad":57,"activo":True}
dict2=dict(color="azul",modelo="Caddy",submodelo="Outdoor",motor=2.0)
print(dict1)
print(dict2)
dict3={24:"Charcuteria Manolo",26:"Medias Puri",28:"Bar el Torrezco"}
print(dict3)
#accdere conternido dentro
print(dict2["color"])
print(dict3[24])#si no la encuentra te da error
print(dict2.get("motor","Esa clave no existe"))#esto si no existe te devuelve que no existe un "none"
print(dict2.get("motore","Esa clave no existe"))#esto si no existe te devuelve que no existe un "none"
#Recorrer diccionario
for elememto in dict3:
    print(elememto)#esto te recorre las claves no los valores
for elememto in dict3:
    print(dict3.get(elememto))#esto te recorre los valores
for elememto in dict3:
        print(elememto,dict3[elememto])  # esto te recorre las claves no los valores

#lo convertimos a lista
print(list(dict2.keys()))#te devuleve claves
print(list(dict2.values()))#te devuelve valores
print(list(dict2.items()))#te devuelve valores y claves en forma de tuplas

dict3[26]="Peluqueria Canina el galgo"#si no existe esa clave se añade y si existe se cambia
print(list(dict3.items()))

dict4={"activo":False,"dni":"49304930X","telefono":744742837}
dict1.update(dict4)#añade las de dic 4 al 1 y las repetidas se sobreesciben
print(list(dict1.items()))
#dict1.clear()#borrar entero
print(dict1)
valor= dict1.pop("edad")#elimina el elemnto con clave edad lo elimina y devuelve
print(valor)
print(dict1)
valor=dict1.popitem()#te elimina el ultimo  y te devuelve la tupla con clave valor y elimna
print(valor)
print(dict1)