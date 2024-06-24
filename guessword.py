import random

def choose_word():
    words = ['python', 'programming', 'hangman', 'developer', 'algorithm', 'function', 'variable', 'loop', 'condition', 'dictionary']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def guess_word_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    correct_guesses = 0

    print("Welcome to the Guess the Word game!")
    print("Try to guess the word, one letter at a time.")
    print("You have 6 attempts to guess the correct word.\n")

    while attempts > 0:
        print(f"Word to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {attempts}")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!\n")
            correct_guesses += word_to_guess.count(guess)
        else:
            print("Wrong guess!\n")
            attempts -= 1

        if correct_guesses == len(set(word_to_guess)):
            print(f"Congratulations! You guessed the word '{word_to_guess}' correctly.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    guess_word_game()
