from collections import Counter

def is_anagram(s1,s2):
    if Counter(s1)==Counter(s2):
        return "It is an anagram!"
    else:
        return "It is not anagram"

s1=input("Enter a word: ")
s2=input("Enter another word: ")
print(is_anagram(s1,s2))