# Read the sentence and normalize it.
sentence = str(input('Enter a sentence: ')).strip().upper()
words = sentence.split()
joined_sentence = ''.join(words)

# Build the reversed sentence manually.
print('You entered the sentence {}'.format(joined_sentence))
reverse_text = ''
for letter in range(len(joined_sentence) - 1, -1, -1):
    reverse_text += joined_sentence[letter]

print('The reverse of {} is {}'.format(joined_sentence, reverse_text))

# Check whether the text is a palindrome.
if reverse_text == joined_sentence:
    print('We have a palindrome!')
else:
    print('The entered sentence is not a palindrome!')