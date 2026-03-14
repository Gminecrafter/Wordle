print("")
print("Wordle".center(40, "="))

rules = """

    Each guess must be a valid five-letter word.

    The color of a letter will change to show you how close your guess was.

    If the letter turns green, the letter is in the word, and it is in the correct spot.

    If the letter turns yellow, the letter is in the word, but it is not in the correct spot.

    If the letter turns white, the letter is not in the word.
    
    You have 6 guesses.

    At the end, the word is revealed.

"""

print(f"Rules:\n{rules}")


#Variables
guesses = 0
past = []
board = ""

import random

#Colors
green  = "\033[32m"
yellow = "\033[33m"
grey  = "\033[0m"

with open("words.txt") as f:
    words = f.read().lower().splitlines() # turns each line into a list item


word = random.choice(words)  # secret word only from real answers

print("Type 'give-up' to give up")

while True:
    final = ""
    guesses += 1
    if guesses == 7:
        print("You ran out of guesses!")
        print("The word was:", word)
        break
    while True:
        guess = input("Guess: ").lower().strip()

        if guess == "give-up":
            print(f"You gave up after {guesses-1} tries")
            print(f"The word was {word}")
            input("\nPress enter to exit ")
            exit()

        if guess not in words: 
            print(guess, "is not valid")
            continue
        elif guess in past:
            print("You've already guessed", guess)
            continue
        elif len(guess) != 5:
            print("You're guess must be 5 letters long")
        else: break


      
    past.append(guess)  
    for i, letter in enumerate(guess):
        if letter not in word:
            final += f"{grey}{letter.upper()}"
        elif letter in word:
            if letter == word[i]:
                final += f"{green}{letter.upper()}"
            else:
                final += f"{yellow}{letter.upper()}"
    print(f"{grey}")
    
    board += f"{final}\n"

    if guess == word:
        print(f"CORRECT! You guessed {guesses} times")
        print(board)
        break
    else: print(board)
    
    print(f"{grey}")

input("\nPress enter to exit ")
