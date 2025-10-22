num1=int(input("mete num1"))
num2=int(input("mete num2"))
cap=[]
if(num1>num2):
    num3=num2
    num1=num2
    num2=num3
for i in range (num1,num2):

    if(i<10 and i>0):
        cap.append(i)
    else:
         if(i%11==0 and i<=100):
             cap.append(i)

    for pos in range(0, len(str(i))):  # rrecorremos cadena
        if(str(i).count(str(pos))==len(str(i))):
            cap.append(i)
        # for posicion in range(0, len(texto2)):  # rrecorremos cadena
        #     print(posicion, "-", texto2[posicion])
        #     11 22 33 99 110
    con=str(i)
    if(con.count(con[0])==len(con)):
        cap.append(con)


print(cap)