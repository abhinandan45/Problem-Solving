sen = "my name is abhinandan"

freq = {}

w = ""

for i in sen.replace(" ",""):
    if i not in freq:
        freq[i] = 1

    else:
        freq[i] += 1

for j,k in freq.items():
    if k == 1:
        print(f"{j}")