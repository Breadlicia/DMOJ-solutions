phrase=input().lower()
anagram=input().lower()
phrase=phrase.replace(" ","")
anagram=anagram.replace(" ","")
phrase=list(phrase)
anagram=list(anagram)
phrase.sort()
anagram.sort()
if phrase == anagram:
    print("Is an anagram.")
else:
    print("Is not an anagram.")

# What I came up with by myself:
# if len(phrase) == len(anagram):
#     checker = [value for value in phrase if value in anagram]
#     if len(checker)==len(phrase):
#         print("Is an anagram.")
#     else:
#         print("Is not an anagram.")
# else:
#     print("Is not an anagram.")