pyg = 'ay'

original = raw_input('Enter a word:')
vowels = ['a', 'e', 'i', 'o', 'u']
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  if first in vowels:
    new_word = word + pyg
    print new_word
  else:
    new_word = word[1:len(word)] + word[0] + pyg
    print new_word
else:
  print 'empty
