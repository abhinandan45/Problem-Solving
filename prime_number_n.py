num = int(input("enter a number : "))

is_prime = False

if num <=1:
    is_prime = False
else:
    for i in range(2,num+1):
        is_prime = True

        for j in range(2,i):
            if i % j == 0:
                is_prime =  False
        if is_prime:
            print(i , end=" ")


