#binary of a number
def dec_to_bin(n):
    if n > 1:
        dec_to_bin(n // 2)
    print(n % 2, end = '')

dec = int(input("\nEnter decimal number:"))
print("The binary of the decimal number:")
dec_to_bin(dec)
