
import random


WORDLIST_FILENAME = "words.txt"


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
    word_guessed_right = True
    
    for m in range(len(secret_word)):
        if not secret_word[m] in letters_guessed:
            word_guessed_right = False
            break
        
    return word_guessed_right         
        



def get_guessed_word(secret_word, letters_guessed):
    
    
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    global game_won
    game_state = ""
    for char in secret_word:
        if char in letters_guessed:
            game_state += char + " "
        else:
            game_state += "_ "    
            
    if not "_" in game_state:
       game_won = True
                     
    return game_state   



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    
    for character in letters_guessed:
        available_letters = available_letters.replace(character,"")
    
    return available_letters
    

def hangman(secret_word):
    '''
    
    takes letters and if they are appropriate shows the game state 
    with graphics and letters guessed so far
    '''
    letters_guessed = ""
    graphics_index = 0
    game_graphics = """
  +---+
  |   |
  |   
  |   
  |
  |
 ===
    
    ""","""
  +---+
  |   |
  |   0
  |   
  |
  |
 ===
    
    ""","""
  +---+
  |   |
  |   0
  |   |
  |
  |
 ===
    
    ""","""
  +---+
  |   |
  |   0
  |  /|
  |
  |
 ===    
    
    ""","""
  +---+
  |   |
  |   0
  |  /|\ 
  |
  |
 ===
  
    ""","""  
  +---+
  |   |
  |   0
  |  /|\ 
  |  / 
  |
 ===    

    ""","""
  +---+
  |   |
  |   0
  |  /|\ 
  |  / \ 
  |
 ===
 
   """

    
    i = 0
    while i < 6:
        letter_guess = input("Guess a letter : ")
        if letter_guess in get_available_letters(letters_guessed):
            letters_guessed += letter_guess
            if not letter_guess in secret_word:
                graphics_index +=1
                i += 1
            print(game_graphics[graphics_index])
            print("You have", 6-i , "guesses left")
            print("")
            print(get_guessed_word(secret_word, letters_guessed))
        elif letter_guess == "*" :
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:          
            print("use lovercase letters you haven't used yet one at a time!")
        if game_won == True:
            input(" You won! \nPlease input something to restart\n")
            break
    
    if is_word_guessed(secret_word, letters_guessed) == True:
        print("")
        print("You Won! restarting")
    else:
        print("")
        print("it was",secret_word)
        input("Game Over \nPlease input something to restart \n")
        print("Game over, restarting")
    
    


def match_with_gaps(my_word, other_word):
    """
    tests if a word with _ character matches with another
    """
    matching = True
    
    my_word = my_word.replace(" " , "")
    if len(my_word) == len(other_word):
        for p in range(len(my_word)):
            if my_word[p] != "_":
                if not my_word[p] == other_word[p]:
                    matching = False
    else:
        matching = False
    
    return matching   



def show_possible_matches(my_word):
    list_of_matches = []
    for q in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[q] ) == True :
            list_of_matches.append(wordlist[q])
    print(list_of_matches)        
            


secret_word = choose_word(wordlist)
game_won = False
game_state_start = """
  +---+          
  |   |      
  |           Welcome to the Hangman Game!
  |           Im thinking of a {} letters long word 
  |           You have 6 guesses left 
  |           You can get hints matching with your current state
 ===          By entering " * "

""".format(len(secret_word))

print(game_state_start)

hangman(secret_word)



