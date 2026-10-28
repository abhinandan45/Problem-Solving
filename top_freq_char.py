sen = "my name is abhinandan sendhav"

freq = {}

for i in sen:
    if i not in freq:
        freq[i] = 1

    else:
        freq[i] += 1

