#############################
# temp basic wordle example #
#############################

# TODO
#   fix layout so that things are clearer
#   Check users guess is a real word
#   randomly pick a hidden word each game


hidden_word = "later"  # Word the user has to guess
correct_guesses = "XXXXX"  # current collection of correct letters
yellow_descriptor = "     "  # empty string to be filled with correct letter descriptors
guesses_remaining = 6  # how many guesses the user has before game ends


# updates the correct_guesses string to store that the letter has been found
def Update_Guesses_String(index, char):
    global correct_guesses
    correct_guesses = correct_guesses[0:index] + char + correct_guesses[index + 1 :]


# print the guessed word again, this time with the correct letters,
# but wrong positions highlighted
def print_yellow_descriptor(index, users_guess):
    print(users_guess)
    global yellow_descriptor
    yellow_descriptor = (
        yellow_descriptor[0:index] + "-" + yellow_descriptor[index + 1 :]
    )
    print(yellow_descriptor)


def check_character_location(users_guess, char):
    index1 = users_guess.find(char)
    index2 = hidden_word.find(char)

    if index1 == index2:
        Update_Guesses_String(index2, char)
    else:
        print_yellow_descriptor(index1, users_guess)


def character_found(users_guess, char):
    check_character_location(users_guess, char)


# take the users guessed word as input
# compare the guessed word with the hidden word one character at a time
# to see if character exists in hidden word
def check_word(users_guess):
    if not users_guess:
        return

    for char in users_guess:
        if char in hidden_word:
            character_found(users_guess, char)


def game_won():
    print("Word Found!!")


def game_lost():
    print("Word was not found!!, the word was... " + hidden_word)


print(hidden_word)


# Until the word is correctly guessed
# Ask the user for a guess at the word
# ensure they have entered a 5 letter word
# check if that word is correct or contains letter within the hidden word
def get_users_guess():
    user_input = input("Please guess a word: ").lower()

    if len(user_input) != 5:
        return

    global guesses_remaining
    guesses_remaining -= 1

    return user_input


def play_game():
    while correct_guesses != hidden_word and guesses_remaining > 0:
        global yellow_descriptor
        yellow_descriptor = "     "
        print("Hidden Word: " + correct_guesses)
        print("Guessed Left:    " + str(guesses_remaining))
        user_input = get_users_guess()
        check_word(user_input)
        print("-----------------")

    if guesses_remaining > 0:
        game_won()
    else:
        game_lost()
        game_lost()


def intro():
    print("Welcome to Python Wordle!")
    print("Guess the hidden word by gussing 5 letter words")
    print(
        "if your guess contains the correct letter in the CORRECT position then the hidden words letter will be revealed"
    )
    print(
        "if your guess contains the correct letter in the WRONG position then the letter in your guess will be highlighted (underlined)"
    )
    print("but the hidden letter will not be unvieled until it's found")
    print("You have 6 guesses to find the word")
    print("GOOD LUCK!")


# main
intro()
play_game()