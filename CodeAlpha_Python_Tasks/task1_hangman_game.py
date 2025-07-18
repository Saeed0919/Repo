
import random

words = ["python", "hangman", "developer", "code", "program"]
chosen_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
display_word = ["_" for _ in chosen_word]

while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print(f"Incorrect! Attempts left: {attempts}")

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)
