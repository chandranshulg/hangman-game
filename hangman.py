print("Welcome to Hangman by Chandranshu")

import random

# List of possible words
words = ["python", "hangman", "programming", "developer", "challenge","leave","consume"]

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word(words)
    guessed_letters = set()
    incorrect_guesses = set()
    attempts = 6

    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            attempts -= 1
        
        if attempts == 0:
            print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
