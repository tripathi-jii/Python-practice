# Program to convert numbers from binary to decimal.

binary = input("Enter a binary number: ")

decimal = 0
power = 0

for digit in binary[::-1]:
    decimal = decimal + int(digit) * (2 ** power)
    power += 1

    print("Decimal number = ", decimal)