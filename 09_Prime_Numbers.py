start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range (start, end + 1):

    if num < 2:
        continue

    is_prime = True

    for i in range (2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)