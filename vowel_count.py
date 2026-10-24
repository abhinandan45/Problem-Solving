sen = "my name is Abhinandan"
vowels = "aeiou"
count = 0


for i in sen.lower():
    if i in vowels:
        count += 1

print(count)

