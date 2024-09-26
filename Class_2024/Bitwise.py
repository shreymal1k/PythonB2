

def convert_number(number):

    binary = ''
    for i in range(31, -1, -1):  
        bit = (number >> i) & 1  
        binary += str(bit)
    binary = binary.lstrip('0') or '0'  

    # Octal conversion
    octal = ''
    for i in range(30, -1, -3): 
        oct_digit = (number >> i) & 0b111  
        octal += str(oct_digit)
    octal = octal.lstrip('0') or '0'

    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    for i in range(28, -1, -4): 
        hex_digit = (number >> i) & 0b1111  
        hexadecimal += hex_chars[hex_digit]
    hexadecimal = hexadecimal.lstrip('0') or '0' 

    return binary, octal, hexadecimal


# Taking an integer as input from the user

num=int(input("Enter A Number : "))

# Convert the integer and print results
binary, octal, hexadecimal = convert_number(num)
print(f"Binary equivalent: {binary}")
print(f"Octal equivalent: {octal}")
print(f"Hexadecimal equivalent: {hexadecimal}")
