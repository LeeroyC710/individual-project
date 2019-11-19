sentence = input('Enter a string:')
vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
count = 0
for char in sentence:
   if char in vowel: 
          count += 1
   else: 
    continue
            
print('There are {} vowels in the string: \'{}\''.format(count,sentence))