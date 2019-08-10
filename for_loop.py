vowels = 0
consonants = 0

for letter in "Niloy":
    if letter.lower() in 'aeiou':
        vowels = vowels + 1

    else:
        consonants = consonants +1

print("vowels: {}".format(vowels))
print("consonants: {}".format(consonants))
