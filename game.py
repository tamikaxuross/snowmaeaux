SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]


def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 
    'Sorry, you lose! The word was {snowman_word}' if the player loses
    """
    #creates dictonary to trach status of each letter in word  guessed or not 
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    #list to keep track of wrong guesses made by player
    wrong_guesses_list = []
#loop through each round, allow player 7 incorrect guesses max
    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        #print the current progress of the word, showing the correctly guessed word
        print_word_progress_string(snowman_word, correct_letter_guess_statuses)
        #display current state of snowman completed
        print_snowman_graphic(len(wrong_guesses_list))
        print(f"Wrong guesses so far: {', '.join(wrong_guesses_list)}")
        print(f"Remaining guesses: {SNOWMAN_MAX_WRONG_GUESSES - len(wrong_guesses_list)}")
        #get a letter guess from the player
        guess = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)
#check if the guessed letter is in the word
        if guess in snowman_word:
            #mark the guessed letter as correctly guessed
            correct_letter_guess_statuses[guess] = True 
        else: 
            #else add the wrong guess to the list and display wrong guess message 
            wrong_guesses_list.append(guess)  
            print("Wrong guess!")
            #if word is fully gues print win message andecit
        if is_word_guessed(snowman_word, correct_letter_guess_statuses):
            print_word_progress_string(snowman_word, correct_letter_guess_statuses)
            print("Congratulations, you win!")
            return
        #if loop ends, player made 7 incorrect guessed, print you lose message 
    print(f"Sorry, you lose! The word was {snowman_word}")



def print_snowman_graphic(wrong_guesses_count):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[user_input_string]): 
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string
    

def build_letter_status_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """

    letter_status_dict = {}
    for letter in snowman_word:
        letter_status_dict[letter] = False
    return  letter_status_dict
    

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It calls another function to generate a string representation of the  
    user's progress towards guessing snowman_word and prints this string.
    """

    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It creates and returns an output string that shows the correct letter 
    guess placements as well as the placements for the letters yet to be 
    guessed.
    """

    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string


def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """

    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True