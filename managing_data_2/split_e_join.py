sentence = 'Hello, welcome to this training!'
# gives me all the words that are separated by space
print(sentence.split())
# every time it finds a comma or _ it will split the sentence.
print(sentence.split(','))
print(sentence.split('-'))

names = 'jhonatan, rafael, carol, amanda, jefferson'
print(names.split())
print(names.split(','))

hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
# if you put for example 3 on the side it does the function of separating 3 times and then stops.
print(hashtags.split('#', 3))

# How to concatenate (combine) strings
hashtags_separated_by_space = hashtags.split(' ')
print(hashtags_separated_by_space)
print(','.join(hashtags_separated_by_space))
print('.'.join(hashtags_separated_by_space))
print(' '.join(hashtags_separated_by_space))

# Exercises:
sentence1 = 'Challenge string manipulation'
sentence2 = 'jhonatan, rafael, carol, camilla'

print(sentence1.split())
print(sentence2.split(','))

words1 = sentence1.split()
words2 = sentence2.split(',')

print(','.join(words1))
print(' &'.join(words2))
