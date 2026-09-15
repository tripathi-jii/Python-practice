# Program for Fabonacci series of first n terms

n = int(input("Enter a number of terms: "))

a = 0
b = 1

print("Fabonacci Series: ")

for i in range (n):
    print(a, end = " ")

    c = a + b
    a = b
    b = c