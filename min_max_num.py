lis = [1,2,3,4,5,6,7,9]

min = float("inf")
max = float("-inf")

for i in lis:
    if i > max:
        max = i

    if min > i:
        min = i

print(max,min)

