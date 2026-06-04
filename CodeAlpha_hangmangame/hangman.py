import random

HANGMAN = [
"""
 -----
 |   |
     |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

words = ["apple", "tiger", "house", "river", "plant"]

def play_game():

    word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n=== HANGMAN GAME ===")

    while wrong_guesses < max_wrong_guesses:

        print(HANGMAN[wrong_guesses])

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed Letters:", guessed_letters)

        if "_" not in display_word:
            print("\n🎉 Congratulations!")
            print("You guessed the word:", word)
            return

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print("❌ Wrong Guess")
            print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

    print(HANGMAN[6])
    print("\n💀 Game Over!")
    print("The word was:", word)


while True:

    play_game()

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        print("\nThanks for playing!")
        break