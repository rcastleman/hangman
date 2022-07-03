from hangman_art import stages, logo
from hangman_words import word_list
import random
# from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 7

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

display = []
guess_list = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"You've already tried {','.join(guess_list)} and you have {lives} lives left.")
    guess = input("Guess a letter: ").lower()
    # clear()
    if guess in guess_list:
        print(f"You've already tried '{guess}'")
    guess_list.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Sorry, '{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was '{chosen_word}'")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
