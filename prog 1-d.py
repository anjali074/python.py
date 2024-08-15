#Q1-d write a python program  to demonstrat variuos base convesion functions?

#Decimal to Binary
def decimal_to_binary(n):
return bin(n).replace("0b", "")
#Decimal to Octal
def decimal_to_octal(n):
return oct(n).replace("0o", "")
#Decimal to Hexadecimal
def decimal_to_hexadecimal(n):
return hex(n).replace("0x", "")
#Binary to Decimal
def binary_to_decimal(b):
return int(b, 2)
#Octal to Decimal
def octal_to_decimal(o):
return int(o, 8)
#Hexadecimal to Decimal
def hexadecimal_to_decimal(h):
return int(h, 16)
#Demonstration
number = 42
print(f"Decimal {number} to Binary: {decimal_to_binary(number)}")
print(f"Decimal {number} to Octal: {decimal_to_octal(number)}")
print(f"Decimal {number} to Hexadecimal: {decimal_to_hexadecimal(number)}")
binary_num = '101010'
octal_num = '52'
hexadecimal_num = '2a'
print(f"Binary {binary_num} to Decimal: {binary_to_decimal(binary_num)}")
print(f"Octal {octal_num} to Decimal: {octal_to_decimal(octal_num)}")
print(f"Hexadecimal {hexadecimal_num} to Decimal: {hexadecimal_to_decimal(hexadecimal_num)}")
