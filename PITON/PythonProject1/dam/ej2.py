def bin_a_dec(binario):
    for bit in binario:
        if bit != "0" and bit != "1":
            return -1

    decimal = 0
    for bit in binario:
        decimal = decimal * 2 + int(bit)

    return decimal
print(bin_a_dec("1010"))  # 10
print(bin_a_dec("1101"))  # 13
print(bin_a_dec("1234"))  # -1
print(bin_a_dec("10A01")) # -1
