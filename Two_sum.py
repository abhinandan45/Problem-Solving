l = [2,4,6,8,3]

target = 11

dic = {}

for i in l:
    req = target - i
    if req in dic:
        print(i, req)

    else:
        dic[i] = True



