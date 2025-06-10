def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ''.join([l if l in guesses else '_' for l in secret_word])
        print(display_word)
        return all (l in guesses for l in secret_word)
    
    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower().strip()
    print("\n" * 5)

    hangman = make_hangman(secret)

    while True: 
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a letter.")
            continue

        guessed_all = hangman(guess)
        if guessed_all:
            print("Congratulations! You guessed the word.")
            break 