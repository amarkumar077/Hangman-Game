import random

words = ["python", "computer", "program", "school", "developer"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

guessed_letters = []

max_wrong_guesses = 6
wrong_guesses = 0

print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)


    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

if "_" not in guessed_word:
    print("================================")
    print(" Congratulations! You won!")
    print("The word was:", word)
    print("================================")
else:
    print("================================")
    print("Game Over!")
    print("The correct word was:", word)
    print("================================")