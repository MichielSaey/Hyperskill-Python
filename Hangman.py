import random

# Write your code here
words = ["python", "java", "swift", "javascript"]
n_attempts = 8

wins = 0
losses = 0


def letter_checker(letter, guessed_letters, guessed_letters_false):
    if not len(letter) == 1:
        print("Please, input a single letter.")
        return False
    elif not letter.islower():
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    elif letter in guessed_letters or letter in guessed_letters_false:
        print("You've already guessed this letter.")
        return False
    else:
        return True


def game_of_hangman():
    global wins, losses

    word_to_guess = random.choice(words)
    available_letters = set(word_to_guess)
    guessed_letters = []
    guessed_letters_false = []
    n_attempts_used = 0
    word_guessed = False

    for i in range(0, len(word_to_guess)):
        guessed_letters.append("-")

    while not word_guessed and n_attempts_used < n_attempts:
        print("")
        print("".join(guessed_letters))
        letter = input("Input a letter: ")
        while not letter_checker(letter, guessed_letters, guessed_letters_false):
            print("")
            print("".join(guessed_letters))
            letter = input("Input a letter: ")

        if letter in available_letters:
            for i in range(0, len(word_to_guess)):
                if letter == word_to_guess[i]:
                    guessed_letters[i] = word_to_guess[i]
        else:
            n_attempts_used += 1
            guessed_letters_false.append(letter)
            print(f"That letter doesn't appear in the word. # {n_attempts - n_attempts_used} attempts")

        if "-" not in guessed_letters:
            word_guessed = True

    if not word_guessed:
        print("You lost!")
        losses += 1
    else:
        print(f"You guessed the word {''.join(guessed_letters)}!")
        print("You survived!")
        wins += 1

    return


def results():
    print(f"You won: {wins} times.")
    print(f"You lost: {losses} times.")


def main():
    while True:
        print("")
        print(f"H A N G M A N # {n_attempts} attempts")
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit')
        selection = input()
        if selection == "play":
            game_of_hangman()
        elif selection == "results":
            results()
        elif selection == "exit":
            return


if __name__ == "__main__":
    main()
