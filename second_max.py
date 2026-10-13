lis = [1,2,3,4,5,6,7,8,9]

max = float("-inf")

sec_max = float("inf")

for i in lis:
    if i > max:
        sec_max = max
        max = i

    elif i > sec_max and i != max:
        sec_max = i

print(sec_max)