igual =False
intentos=0
while igual==False:
    contra =input("mete contra\n")
    contra2=input("mete repite contra")
    intentos+=1
    if(contra.__eq__(contra2)):
        print()
        igual=True
print("metiste la misma contra")
print("intentos ",intentos)