#!/usr/bin/env python3

user_word_str = input("Please enter a word for a Ubbi Dubbi translation: ")

output = []

for letter in user_word_str:
    if letter in 'aeiou':
        output.append((user_word_str.replace(f"{letter}", f"ub{letter}")))
    else:
        output.append(letter)
print(''.join(output))




#book example solution:
#
#word = input("Enter a word: ")
#output = []
#for letter in word:
#if letter in 'aeiou': output.append(f'ub{letter}')
#else: output.append(letter)
#print(''.join(output))