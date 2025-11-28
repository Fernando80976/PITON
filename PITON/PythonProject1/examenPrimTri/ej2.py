# def dec_a_bin(valor):
#     val=128
#     fin=False
#     cad=""
#     if valor<0 and valor>255 :
#         while fin !=True and val<1:
#
#
#             if valor%val==0:
#                 cad+="1"
#             else:
#                 cad+="0"
#             val=val/2
#
#         return cad
#     else:
#         return -1

def dec_a_bin(num):
    if str(num).isdigit() and (0<= num <=255):
        return str(bin(num)[2:].zfill(8))
    return -1

print(dec_a_bin(22))
print(dec_a_bin(127))
print(dec_a_bin(333))
print(dec_a_bin("hola"))