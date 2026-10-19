import random
# Word list
WORDS = ["python", "program", "computer", "software",
    "student", "developer", "education", "science",
    "keyboard", "internet", "project", "function",
    "variable", "database", "algorithm", "university",
    "technology", "information", "hangman", "practice",
    "country","america","computer","following","current",
    "computer","insurance","another","why","shall","property",
    "class","cd","still","money","quality","every","listing","content",
    "country","private","little","visit","save","tools","low","reply","customer",
    "december","compare","movies","include","college","value","article","york","man",
    "card","jobs","provide"]

# ASCII Hangman stages: 0 to 6 incorrect guesses
HANGMAN_STAGES = [
"""
 Stage 0:
  ______
  | |
  |
  |
 _|_
 """,
 """
Stage 1:
  ______
  | |
  | O
  |
 _|_
 """,
 """
Stage 2:
  ______
  | |
  | O
  | |
 _|_
 """,
 """
Stage 3:
  ______
  | |
  | O
  | /|
 _|_
""",
"""
Stage 4:
  ______
  | |
  | O
  | /|\
 _|_
""",
"""
Stage 5:
  ______
  | |
  | O
  | /|\
 _|_ /
""",
"""
Stage 6:
  ______
  | |
  | O
  | /|\
 _|_ / \
    """
]

def play_hangman():
    secret_word = random.choice(WORDS).lower()
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("\n===== WELCOME TO HANGMAN =====")
    print("Guess the hidden word one letter at a time!")
    print("You have 6 incorrect guesses available.")

    while len(wrong_guesses) < max_attempts:

        print(HANGMAN_STAGES[len(wrong_guesses)])

        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", display_word)
        print("Wrong guesses:", len(wrong_guesses), "/", max_attempts)

        if wrong_guesses:
            print("Incorrect letters:", " ".join(sorted(wrong_guesses)))

        remaining = max_attempts - len(wrong_guesses)
        print("Attempts remaining:", remaining)

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter! Try another.")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_guesses.add(guess)
            print("Incorrect guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + secret_word.upper())
            print("Congratulations! You guessed the word!")
            print("You won the game!")
            break
    else:
        print(HANGMAN_STAGES[6])
        print("\nGame Over! You ran out of attempts.")
        print("The correct word was:", secret_word.upper())


if __name__ == "__main__":
    while True:
        play_hangman()

        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.strip().lower() != "y":
            print("Thanks for playing Hangman!")
            break