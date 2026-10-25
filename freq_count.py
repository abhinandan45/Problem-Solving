sen = "abhinandan sendhav"

freq = {}

for i in sen.replace(" ",""):
    if i not  in freq:
        freq[i] = 1

    else:
        freq[i] += 1



# print(freq)

for j,k in freq.items():
    if k > 1:
        print(f"{j} : {k}")
