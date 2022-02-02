#hexadcimal to binary
hex_dec_num = input("Enter the hexadecimal number:")
binary_num = " "
hexlen = len(hex_dec_num)
i = 0
while i<hexlen:
    if hex_dec_num[i] == '0':
        binary_num = binary_num + "0000"
    elif hex_dec_num[i] == '1':
        binary_num = binary_num + "0001"
    elif hex_dec_num[i] == '2':
        binary_num = binary_num + "0010"
    elif hex_dec_num[i] == '3':
        binary_num = binary_num + "0011"
    elif hex_dec_num[i] == '4':
        binary_num = binary_num + "0100"
    elif hex_dec_num[i] == '5':
        binary_num = binary_num + "0101"
    elif hex_dec_num[i] == '6':
        binary_num = binary_num + "0110"
    elif hex_dec_num[i] == '7':
        binary_num = binary_num + "0111"
    elif hex_dec_num[i] == '8':
        binary_num = binary_num + "1000"
    elif hex_dec_num[i] == '9':
        binary_num = binary_num + "1001"
    elif hex_dec_num[i] == 'a' or hex_dec_num[i] == 'A':
        binary_num = binary_num + "1010"
    elif hex_dec_num[i] == 'b' or hex_dec_num[i] == 'B':
        binary_num = binary_num + "1011"
    elif hex_dec_num[i] == 'c' or hex_dec_num[i] == 'C':
        binary_num = binary_num + "1100"
    elif hex_dec_num[i] == 'd' or hex_dec_num[i] == 'D':
        binary_num = binary_num + "1101"
    elif hex_dec_num[i] == 'e' or hex_dec_num[i] == 'E':
        binary_num = binary_num + "1110"
    elif hex_dec_num[i] == 'f' or hex_dec_num[i] == 'F':
        binary_num = binary_num + "1111"

    i = i + 1

print("Equivalent binary value is ",binary_num)





