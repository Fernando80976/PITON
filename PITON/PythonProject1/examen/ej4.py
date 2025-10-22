seg=int(input("mete numero de segundos"))
dias=0
horas=0
min=0
while seg>60:
    if(seg//86400!=0):
        dias+=1

        seg=seg-86400
    else:
        if(seg//3600!=0):
            horas+=1
            seg=seg-3600
        else:
            if(seg//60!=0):
                min+=1
                seg=seg-60

print("SON :")
if dias!=0:
    print("son",dias,"dias")
if horas!=0:
    print(horas,"horas")
if min!=0:
    print(min,"minutos")
if seg!=0:
    print(seg,"segundos")