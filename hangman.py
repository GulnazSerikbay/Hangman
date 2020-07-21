from words import cmu     #imports list from words.py file


category = input("Choose one: GENERAL/CMU?").upper()

def get_word():
    while category == "general":
        word = random.choice(general) #randomly chooses from general
    else:
        word = random.choice(cmu) #randomly chooses from cmu

    return word.upper()



def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[lives]


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = [] #what letters have been guessed
    guessed_words = []
    print("Hey let's get started! Can you guess the word?'")
   # print("You have " + lives + " lives.")
    print(word_completion + "\n")

    while not guessed and lives > 0:
        guess = input("Try to guess the hidden word: ").upper() #receiving the use input "guess"

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter, man..." + guess)

            elif guess not in word:
                print("Nope, " + guess + " is not in the word.\n (-_-)")
                lives = lives - 1
                print("You have " + lives + "lives.")
                guessed_letters.append(guess)

            else:
                print("Well done! " + guess + "is in the word. Keep going!")
                guessed_letters.appenf(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_words:
                print("You've already guessed this word!" + guess)
            elif guess != word:
                print(guess + "is not the actual word. (*_*)")
                lives = lives - 1
                print("You have " + lives + "lives.")
                guesses_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Please, try again")
        print(display_hangman(lives))
        print(word_completion + "\n")
    if guessed:
        print("YAAAY! You've guessed the word! Winner!")
    else:
        print("OOH! You lost! Sorry, sure, you will win next time! The word was " + word)









def main():

    word = get_word()
    play(word)

    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)



if __name__ == "__main__":
    main()

