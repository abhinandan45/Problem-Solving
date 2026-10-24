sen = "my name is Abhinandan"
vowels = "aeiou"

vowel = ""
count = 0


for i in sen.lower():
    if i in vowels:
        vowel += i
        count += 1

print(count)
print(vowel)


freq = {}

for j in vowel:
    if j in freq:
        freq[j] += 1

    else:
        freq[j] = 1

print(freq)
