def divisioresComunes(n1,n2):
    divn1=[]
    divn2=[]
    divAux=[]
    if n1<0 or n2 <0:
        return "metiste numeros negativos"
    if n1==0 or n2==0:
        return "divisiones comunes el 0"
    else:
        for i in range(1,n1):
            if n1%i==0:
                divn1.append(i)
        for i in range(1,n2):
            if n2%i==0:
                divn2.append(i)
        for i in divn2:
            if n1%i==0:
                divAux.append(i)
        for i in divn1:
            if n2%i==0:
                divAux.append(i)
        divCom=set(divAux)

    return "Los divisores comunes de",n1,n2,"Son: ",str(divCom).replace("{","").replace("}","")

print(divisioresComunes(-1,2))
print(divisioresComunes(22,16))
print(divisioresComunes(2,2))
print(divisioresComunes(1725,2500))