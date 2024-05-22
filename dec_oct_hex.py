def convert(n):
    binary = bin(n).replace("0b", "")
    octal = oct(n).replace("0o", "")
    hexadecimal = hex(n).replace("0x", "").upper()
    return binary, octal, hexadecimal
decimal = int(input("Enter a deciaml number: "))
binary , octal, hexadecimal = convert(decimal)
print(f"Decimal: {decimal}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

