tex=input("mete un texto")
vocales=0
espacios=0
for caracter in tex :
    if caracter in "aeiou":
            vocales+=1
    if caracter == " ":
        espacios+=1
tex=tex.replace("a","")
tex=tex.replace("e","")
tex=tex.replace("i","")
tex=tex.replace("o","")
tex=tex.replace("u","")
tex=tex.replace(" ","")
print(tex)
print("HAY ",vocales,"vocales")
print("hay ",espacios,"espacios")