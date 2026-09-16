n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

hcf = 1

for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        hcf = i

print("HCF is: ", hcf)

