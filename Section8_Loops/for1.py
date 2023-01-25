vowels = 0
consonants = 0

for letter in 'mississippi':
    if letter.lower() in 'aeiou':
        vowels += 1
    elif letter == ' ':
        pass
    else:
        consonants += 1

print('There are {} vowels'.format(vowels))
print('There are {} consonants'.format(consonants))
