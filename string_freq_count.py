sen = "my name ia abhinandan sendhav"

freq = {}

for i in sen.lower().replace(" ",""):
    if i not in freq:
        freq[i] = 1

    else:
        freq[i] += 1

unique = {}

for j , k in freq.items():
    if k == 1:
        unique[j] = k


print(unique)

print(freq)