import random

# Write your code here
words = ["python", "java", "swift", "javascript"]

print("H A N G M A N")
print("Guess the word: ")
guessed_word = input()
if guessed_word == random.choice(words):
    print("You survived!")
else:
    print("You lost!")
