# Program to print Armstrong number in given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers are: ")

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print(num)