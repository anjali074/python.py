#Q-write a python program  to demonstrat varipos base convesion functions?
def binary_to_decimal(binary):
    """Convert binary to decimal"""
    return int(binary, 2)

def octal_to_decimal(octal):
    """Convert octal to decimal"""
    return int(octal, 8)

def hexadecimal_to_decimal(hexadecimal):
    """Convert hexadecimal to decimal"""
    return int(hexadecimal, 16)

def decimal_to_binary(decimal):
    """Convert decimal to binary"""
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    """Convert decimal to octal"""
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    """Convert decimal to hexadecimal"""
    return hex(decimal)[2:]

def main():
    print("Base Conversion Functions")
    print("---------------------------")

    # Binary to Decimal
    binary = "1010"
    decimal = binary_to_decimal(binary)
    print(f"Binary {binary} to Decimal: {decimal}")

    # Octal to Decimal
    octal = "12"
    decimal = octal_to_decimal(octal)
    print(f"Octal {octal} to Decimal: {decimal}")

    # Hexadecimal to Decimal
    hexadecimal = "A"
    decimal = hexadecimal_to_decimal(hexadecimal)
    print(f"Hexadecimal {hexadecimal} to Decimal: {decimal}")

    # Decimal to Binary
    decimal = 10
    binary = decimal_to_binary(decimal)
    print(f"Decimal {decimal} to Binary: {binary}")

    # Decimal to Octal
    decimal = 10
    octal = decimal_to_octal(decimal)
    print(f"Decimal {decimal} to Octal: {octal}")

    # Decimal to Hexadecimal
    decimal = 10
    hexadecimal = decimal_to_hexadecimal(decimal)
    print(f"Decimal {decimal} to Hexadecimal: {hexadecimal}")

if __name__ == "__main__":
    main()
