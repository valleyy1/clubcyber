def decimalnumtobinary(decimal, bits):
    binary= bin(decimal) 
    binary = binary[2:] 
    binary = binary.zfill(bits) 
    return binary


def shitatmashlim2(binary, bitamount):
    reverse_binary = ''.join(('1' if bit == '0' else '0' for bit in binary)) 
    reverse_dec = int(reverse_binary, 2) + 1
    return(decimalnumtobinary(reverse_dec, bitamount))
    

try:
    decimal_input = int(input("enter a decimal num: "))
    bitamount = int(input("enter a bit amount: "))
    binary = decimalnumtobinary(decimal_input, bitamount)
    negative_binary = shitatmashlim2(binary, bitamount)
    print(negative_binary)

except:
    print("ONLY NUMBERS ARE ALLOWED AS INPUT!")