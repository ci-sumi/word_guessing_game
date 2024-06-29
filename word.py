import random

# List of words to choose from
word_list = ['python', 'java', 'kotlin', 'javascript']

# Choose a random word from the list
word = random.choice(word_list)

# Number of allowed wrong guesses
max_attempts = 6

# Variables to track game state
guesses = ''
attempts_left = max_attempts

print("Welcome to the Word Guess Game!")
print("Try to guess the word, one letter at a time.")

while attempts_left > 0:
    # Display the current state of the word
    display_word = ''.join([char if char in guesses else '_' for char in word])
    print(f"\nCurrent word: {display_word}")
    
    if '_' not in display_word:
        print("Congratulations! You've guessed the word:", word)
        break
    
    # Get a guess from the user
    guess = input("Guess a letter: ").lower()
    
    # Check if the guessed letter is in the word
    if guess in word:
        print("Good guess!")
        guesses += guess
    else:
        attempts_left -= 1
        print(f"Wrong guess. You have {attempts_left} attempts left.")
    
    if attempts_left == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

print("Game Over. Thanks for playing!")

