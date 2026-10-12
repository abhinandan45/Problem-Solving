num = 11

is_prime = True

if num < 2:
    is_prime = False
    print("please enter a number that greater than 2")

else:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False

if is_prime:
    print(f"{num} number is a prime number.")

else:
    print(f"{num} number is not a prime number")

