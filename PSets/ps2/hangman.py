# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "hangman.txt"

hangman_pics = {
  0: """
       _____
      |   |
      O   |
     \|/  |
      |   |
     / \  |
      ____|____""",
  1: """
       _____
      |   |
      O   |
     \|/  |
      |   |
     /    |
      ____|____""",
  2: """
       _____
      |   |
      O   |
     \|/  |
      |   |
          |
      ____|____""",
  3: """
       _____
      |   |
      O   |
     \|   |
          |
          |
      ____|____""",
  4: """
       _____
      |   |
      O   |
      |   |
          |
          |
      ____|____""",
  5: """
       _____
      |   |
      O   |
          |
          |
          |
      ____|____""",
  6: """
       _____
      |   |
          |
          |
          |
          |
      ____|____"""
  
}


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
      if char not in letters_guessed:
        return False
    return True







def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for char in secret_word:
      if char in letters_guessed:
        guessed_word = guessed_word + char
      else:
        guessed_word = guessed_word + "_ "
    return guessed_word




def get_available_letters(letters_guessed, hint):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    filtered_letters = ""
    if hint:
      all_letters = string.ascii_lowercase + "*"
    else:
      all_letters = string.ascii_lowercase
    for char in all_letters:
      if char not in letters_guessed:
        filtered_letters += char
    return filtered_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings = 3
    letters_guessed = []
    greeting(secret_word)
    

    while guesses_left > 0 and warnings > -1:
      display_hangman(guesses_left)
      display_guesses_left(guesses_left)
      print_available_guesses(letters_guessed)
      user_input = input("Please guess a letter ").lower()
      while len(user_input) != 1 or user_input not in get_available_letters(letters_guessed, False):
        (warnings, guesses_left, letters_guessed, user_input) = handle_warnings(warnings, guesses_left, letters_guessed, user_input)

      letters_guessed.append(user_input)
      if is_word_guessed(secret_word, letters_guessed):
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        print("\n-----------------------------------------------\n")
        print(f"Congratulations, you won!")
        print_score(guesses_left, secret_word)
        guesses_left = 0
        return
      elif user_input in secret_word:
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
      else:
          if user_input not in "aeiouy":
            guesses_left -= 1
          else:
            guesses_left -= 2
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
    display_hangman(0)
    print("You're out of guesses! You lose!")
    print(f"My word was {secret_word}!")
    

def greeting(secret_word):
  print("Welcome to the game Hangman!")
  print(f"I am thinking of a word that is {len(secret_word)} letters long.")
  # print(secret_word)
  print('_ ' * len(secret_word))
  

def print_score(guesses_left, secret_word):
  score = guesses_left * len(secret_word)
  print(f"Your total score for this game is: {score}")

def display_hangman(guesses_left):
  print(hangman_pics[guesses_left])
  print("-----------------------------------------------")

def display_guesses_left(guesses_left):
  if guesses_left > 1:
    print(f"You have {guesses_left} guesses left.")
  else:
    print(f"You have {guesses_left} guess left.")

def print_available_guesses(letters_guessed):
  print(f"Available letters: {get_available_letters(letters_guessed, False)}")

def handle_warnings(warnings, guesses_left, letters_guessed, user_input):
  warnings -= 1
  if warnings == -1:
    print("That was your last warning. You lose a guess!")
    guesses_left -= 1
    warnings = 3
    if guesses_left > 0:
      display_guesses_left
      display_hangman(guesses_left)
      print_available_guesses(letters_guessed)
      user_input = input("Please guess a letter: ").lower()
  elif len(user_input) != 1:
    user_input = input(f"Please guess only a single letter. You now have {warnings} warnings left: ").lower()
    print("-----------------------------------------------")
  elif user_input not in string.ascii_lowercase:
    user_input = input(f"Please enter a valid letter. You now have {warnings} warnings left: ")
  elif user_input not in get_available_letters(letters_guessed, True):
    user_input = input(f"Oops! You've already guessed that letter. You now have {warnings} warnings left: ").lower()
    print("-----------------------------------------------")
  return (warnings, guesses_left, letters_guessed, user_input)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    blanks = {}
    used_letters = {}
    my_word = my_word.replace(" ", "")
    
    
    if len(my_word) != len(other_word):
      return False
    else: 
      for i in range(len(my_word)):
        if my_word[i] != "_" and other_word[i] in blanks:
          return False
        elif my_word[i] == "_" and other_word[i] in used_letters:
          return False
        elif my_word[i] != "_" and my_word[i] != other_word[i]:
          return False
        elif my_word[i] == "_":
          blanks[other_word[i]] = True
        else:
          used_letters[my_word[i]] = True
    return True






def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.
    '''
    matched_words = []
    for word in load_words():
      if match_with_gaps(my_word, word):
        matched_words.append(word)
    
    if len(matched_words) >= 1:
      str = " "
      print(str.join(matched_words))
    else:
      print("No matches found")




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings = 3
    letters_guessed = []
    greeting(secret_word)
    

    while guesses_left > 0 and warnings > -1:
      display_hangman(guesses_left)
      display_guesses_left(guesses_left)
      print_available_guesses(letters_guessed)
      user_input = input("Please guess a letter ").lower()
      while len(user_input) != 1 or user_input not in get_available_letters(letters_guessed, True):
        (warnings, guesses_left, letters_guessed, user_input) = handle_warnings(warnings, guesses_left, letters_guessed, user_input)
      if user_input != "*":
        letters_guessed.append(user_input)
      if is_word_guessed(secret_word, letters_guessed):
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        print("\n-----------------------------------------------\n")
        print(f"Congratulations, you won!")
        print_score(guesses_left, secret_word)
        guesses_left = 0
        return
      elif user_input == "*":
        print("Possible matches: ")
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print(get_guessed_word(secret_word, letters_guessed))
        print("\n-----------------------------------------------\n")
      elif user_input in secret_word:
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
      else:
          if user_input not in "aeiouy":
            guesses_left -= 1
          else:
            guesses_left -= 2
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
    display_hangman(0)
    print("You're out of guesses! You lose!")
    print(f"My word was {secret_word}!")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)


# show_possible_matches("a_ _ le")