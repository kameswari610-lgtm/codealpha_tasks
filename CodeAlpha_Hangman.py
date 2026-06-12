def hangman_game():

    word = "kami"
    guessed_word = ["_"] * len(word)

    attempts = 6

    print("Welcome to Hangman Game")

    while attempts > 0 and "_" in guessed_word:

        print("\nWord:", " ".join(guessed_word))

        guess = input("Enter a letter: ").lower()

        if guess in word:

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

            print("Correct Guess!")

        else:
            attempts -= 1
            print("Wrong Guess!")
            print("Attempts Left:", attempts)

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)

    else:
        print("\nGame Over!")
        print("The word was:", word)


hangman_game()