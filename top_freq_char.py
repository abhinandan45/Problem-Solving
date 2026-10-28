sen = "my name is abhinandan sendhav"

freq = {}

for i in sen:
    if i not in freq:
        freq[i] = 1

    else:
        freq[i] += 1

l = float("-inf")
m = ""


for k,j in freq.items():
    if j > l:
        l = j
        m = k

print(l,m)
        
