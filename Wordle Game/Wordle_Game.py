#############################
# temp basic wordle example #
#############################

# update correct_guesses if the letter is in the chosen(hard coded) word

hidden_word = "later"  # Word the user has to guess
correct_guesses = "XXXXX"  # current collection of correct letters
yellow_descriptor = "     "
guesses_remaining = 6  # how many guesses the user has before game ends
print(hidden_word)


# updates the correct_guesses string to store that the letter has been found
def Update_Guesses_String(index, char):
    global correct_guesses
    correct_guesses = correct_guesses[0:index] + char + correct_guesses[index + 1 :]


# print the guessed word again, this time with the correct letters,
# but wrong positions highlighted
def print_yellow_descriptor(index, users_guess):
    print(users_guess)
    global yellow_descriptor
    yellow_descriptor = yellow_descriptor[0:index] + "-" + yellow_descriptor[index + 1 :]
    print(yellow_descriptor)


def check_character_location(users_guess, char):
    index1 = users_guess.find(char)
    index2 = hidden_word.find(char)
    print("char location in users input: " + str(index1))
    print("char location in hidden word: " + str(index2))

    if index1 == index2:
        print("GREEN LETTER FOUND")
        Update_Guesses_String(index2, char)
    else:
        print("YELLOW LETTER FOUND")
        print_yellow_descriptor(index1, users_guess)


def character_found(users_guess, char):
    print("char found: " + char)
    check_character_location(users_guess, char)


# take the users guessed word as input
# compare the guessed word with the hidden word one character at a time
# to see if character exists in hidden word
def check_word(users_guess):
    if not users_guess:
        return

    if users_guess == hidden_word:
        print("user guessed the word")
        correct_guesses == users_guess
        return

    for char in users_guess:
        if char in hidden_word:
            character_found(users_guess, char)


def game_won():
    print("Word Found!!")


def game_lost():
    print("Word was not found!!, the word was... " + hidden_word)


# Until the word is correctly guessed
# Ask the user for a guess at the word
# ensure they have entered a 5 letter word
# check if that word is correct or contains letter within the hidden word
while correct_guesses != hidden_word and guesses_remaining > 0:
    yellow_descriptor = "     "
    print("Correct Letters: " + correct_guesses)
    print("Guessed Left:    " + str(guesses_remaining))
    user_input = input("Please guess a letter: ").lower()

    if len(user_input) != 5:
        continue

    guesses_remaining -= 1
    check_word(user_input)
    print("-----------------")

if guesses_remaining > 0:
    game_won()
else:
    game_lost()
    game_lost()