#!/usr/bin/env python3
# if user_word begins with a,e,i,o,u then append? the string "way" to the end of the word
user_word = input("Please enter a word to translate into pig latin: ")

if user_word[0] in 'aeiou':
    print(f"{user_word}way")

# if the word begins with a constinent, then take first letter, put it at the end of the word, and end with "ay"

else:
    print(f"{user_word[1:]}{user_word[0]}ay")


