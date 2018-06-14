#Hangman game created by Saim Akhtar
import string
import random
from os import system
WORDLIST_FILENAME = "words.txt"
def loadWords():
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
global alpha
global word
word=chooseWord(wordlist).lower()

alpha=string.ascii_lowercase
def availableletters(guess):
    global alpha
    alpha=alpha.replace(guess,'')
    return alpha
def rightguess(show,guessedletter):
    global word
    for i in range(len(word)):
        if word[i] is guessedletter:
            show=show[:i] + guessedletter + show[i+1:]
    return show
def guessaword():
    global word
    global alpha
    guesses=8
    repeatedletters=[]
    lenofword=len(word)
    show=''
    for i in range(lenofword):
        show=show + '_'
    while guesses >0 and show != word:
        print("Available letters are: ",alpha)
        print("Guesses left:",guesses)
        print("Guess a word that is",lenofword,"letters long")
        for i in show:
            print(i,end=' ')
        guessedletter=input("Guess a letter: ")
        guessedletter.lower()
        if guessedletter in repeatedletters:
            print("The Letter",guessedletter," is already used")
            print("-----------------")
        elif guessedletter in word and guessedletter not in repeatedletters:
            alpha=availableletters(guessedletter)
            show=rightguess(show,guessedletter)
            repeatedletters.append(guessedletter)
            print("-----------------")
        elif guessedletter not in word and guessedletter not in repeatedletters:
            guesses-=1
            repeatedletters.append(guessedletter)
            alpha=availableletters(guessedletter)
            print("The letter",guessedletter,"is not in the word")
            print("-----------------")
    if show == word:
        for i in show:
            print(i,end=' ')
        print()
        print("You won the game")
    elif show != word:
        print("Sorry you lost it")
        print("The secret word is :",word)

def hangman():
    print("                     LET THE HANGMAN GAME BEGIN")
    print("          ---------------------------------------------       ")
    guessaword()
if __name__ == "__main__":
    hangman()
    system("pause")
