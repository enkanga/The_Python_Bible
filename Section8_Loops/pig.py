# get sentence from user
original = input('Please enter a sentence: ').strip().lower()

# split sentence into words
words = original.split()

# loop through words and convert to pig latin
new_words = []

# if starts with a vowel, just add 'yay'
# otherwise, move the first consonant cluster to end, add 'ay'
for word in words:
    if word[0] in 'aeiou':
        new_words.append(word + 'ay')
    else:
        # Video solution
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos += 1
            else:
                break
        
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + 'ay'
        new_words.append(new_word)
        
""" My solution (doesn't account for non-vowel words)
        for i in range(len(word)):
            if word[i] in 'aeiou':
                cons_cluster = word[:i]
                rem_cluster = word[i:]
                break
        
        new_words.append(rem_cluster + cons_cluster + 'ay')
"""


# stick words back together
output = ' '.join(new_words)

# output the final string
print(output)