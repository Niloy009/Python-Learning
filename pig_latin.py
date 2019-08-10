#get the sentence from the user

orginal = input("Please give a sentence: ").lower().strip()

#split the sentence into the words

words =  orginal.split()

#loop through the words and convert pig latin

new_words = []

for word in words:
    #if words start with vowel then just add 'yay' at last
    if word[0] in 'aeiou':
        new_word = word + 'yay'
        new_words.append(new_word)
    else:
        #otherwise, move the frst consonant cluser to end and and 'ay' 
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons+ 'ay'
        new_words.append(new_word)

#stck words back together

output = ' '.join(new_words)

#output the final sentence
print(output)
