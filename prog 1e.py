#Q-1e write a python program to demonstrate various base conversion functions?
# Base Conversion Functions
def binary_to_decimal(binary):
return int(binary, 2)
def decimal_to_binary(decimal):
return bin(decimal)[2:]
def octal_to_decimal(octal):
return int(octal, 8)
def decimal_to_octal(decimal):
return oct(decimal)[2:]
def hexadecimal_to_decimal(hexadecimal):
return int(hexadecimal, 16)
def decimal_to_hexadecimal(decimal):
return hex(decimal)[2:]
# Test the functions
binary_num = "1010"
decimal_num = 10
octal_num = "12"
hexadecimal_num = "A"
print("Binary to Decimal:", binary_to_decimal(binary_num))
print("Decimal to Binary:", decimal_to_binary(decimal_num))
print("Octal to Decimal:", octal_to_decimal(octal_num))
print("Decimal to Octal:", decimal_to_octal(decimal_num))
print("Hexadecimal to Decimal:", hexadecimal_to_decimal(hexadecimal_num))
print("Decimal to Hexadecimal:", decimal_to_hexadecimal(decimal_num))
