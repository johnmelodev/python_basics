keyboard = 'keyboard'
print(keyboard[2])
print(keyboard[-1])
print(keyboard[1:5])
print(keyboard[3:])
print(keyboard[-3:])
print(keyboard.index('l'))
print(keyboard[keyboard.index('l')])
# to access the last occurrence of a character in a string
phrase = 'Clean Code'
print(phrase.rindex('C'))

library = 'Library'
print(library.index('o'))

phrase = 'application development'
# rindex to get from back to front. and index to get normal
index_d = phrase.rindex('d')
index_s = phrase.rindex('s')
print(phrase[index_d:index_s+1])
