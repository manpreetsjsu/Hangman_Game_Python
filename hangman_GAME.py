# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    result = []
    for element in sorted(secretWord):
        if element in lettersGuessed:
            result.append(element)
    result.sort()
    a=sorted(secretWord)
    #a.sort()
    if result==a:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result1=''
    for element1 in secretWord:
        if element1 in lettersGuessed:
            result1=result1+element1
        if element1 not in lettersGuessed:
            #print(result1)
            result1=result1+ ' _ ' 
    return result1


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    a=string.ascii_lowercase
    for element2 in a:
        if element2 in lettersGuessed:
            a=a.replace(element2,"")
    return a
        

def hangman(secretWord):
    #type this in shell for secretWord=chooseWord(wordlist).lower()
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) + " letters long")
    print("-----------")
    guess=[]
    count=1
    num=8
    while num<=8 and num>=1:
        print("You have "+ str(num) +" guesses left")
        print("Available letters : "+ str(getAvailableLetters(guess)))
        guess1=input("Please guess a letter :").lower()
        if guess1 in guess:
            print("Oops! You've already guessed that letter:"+ str(getGuessedWord(str(secretWord),guess)))
            print("-----------")
            continue
        guess=guess+list(guess1)
        
        if guess1 in secretWord:
            print("Good Guess :"+ str(getGuessedWord(str(secretWord),guess)))
            print("-----------")
            
        elif guess1 not in secretWord:
            num=num-1
            count=count+1
            print("Oops! That letter is not in my word :"+ str(getGuessedWord(str(secretWord),guess)))
            print("-----------")
            
        if  isWordGuessed(secretWord,guess) == True:
          
            print("Congratualations, you won!")
            break
        elif count >8:
            print("Sorry, you ran out of guess. The word was :" + str(secretWord))
            break
    return None

hangman(chooseWord(wordlist).lower())