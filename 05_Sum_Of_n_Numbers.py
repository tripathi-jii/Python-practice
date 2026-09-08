# Program for sum of n numbers

n = int(input("Enter the value of n: "))

sum = 0

for i in range(1, n+1):
    sum = sum+i

    print("Sum of first", n, "numbers is: ", sum)
    