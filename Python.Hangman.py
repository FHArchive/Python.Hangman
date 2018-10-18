"""
Author Kieran
Year 2017 (ammended 10/18)

This is a game of hangman that runs in the command line or the Python Shell.
The user has 7 strikes and must guess the word (in this case from the list of
countries below.
"""
# This module is used to pick a random word from the list below
import random
# A list of random words 
wordsList = ['Afghanistan','Albania','Algeria','Angola','Antarctica',
             'Argentina','Australia','Austria','Azerbaijan','Bahamas',
             'Bangladesh','Barbados','Belarus','Belgium','Bermuda',
             'Bolivia','Botswana','Brazil','Bulgaria','Cambodia','Cameroon',
             'Canada','Cape Verde','Cayman Islands','Central African Republic',
             'Chad','Chile','China','Christmas Island','Colombia','Comoros',
             'Democratic Republic of Congo','Costa Rica','Croatia',
             'Cuba','Cyprus','Czech Republic','Denmark','Dominica','Dominican Republic',
             'Ecuador','Egypt','Estonia','Ethiopia','Falkland Islands','Fiji',
             'Finland','France','French Guiana','French Polynesia',
             'Gambia','Georgia','Germany','Ghana','Gibraltar','Great Britain',
             'Greece','Greenland','Grenada','Guinea',
             'Haiti','Honduras','Hong Kong','Hungary',
             'Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy',
             'Jamaica','Japan','Jordan','Kazakhstan','Kenya','North Korea','South Korea',
             'Latvia','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg',
             'Madagascar','Malawi','Malaysia','Maldives','Mali','Malta',
             'Mexico','Mongolia','Montenegro','Montserrat',
             'Morocco','Mozambique','Myanmar','Namibia','Norway','Pakistan',
             'Peru','Philippines','Poland','Romania','Russia','Senegal','Serbia',
             'Slovenia','Slovakia','Singapore','South Africa','Syria','Taiwan',
             'Turkey','Ukraine','United Kingdom','United States']
# A list of correct guesses
"""
The space is needed to win where there are two words 
"""
goodGuesses = [' ']
# A list of incorrect guesses
badGuesses = []
# The maximum number of strikes allowed
strikes = 7
# Flag for the end of the game. Start at false 
endGame = 0
# Flag to identify if the word has been guessed
complete = 0
# Get the random word
guessWord = wordsList[random.randint(0,len(wordsList)-1)]
# Make it uppercase
guessWord = guessWord.upper()
# Make it into a list 
guessList = list(guessWord)

"""
Method main
Inputs guessList: list of chars
Output [none]
The main method promts the user for a guess, converts this to uppercase and checks
to see if its in the word
"""
def main(guessList):
    # Get user input and make it upper case
    print ("Please enter a letter to guess the word")
    userGuess = input('>>>')
    userGuess = userGuess.upper()
    isInList = 0
    for i in range( len(guessList)):
        # isInList is true if the user input is in the guessList
        if userGuess == guessList[i]:
            isInList = 1
    if isInList == 1:
        # If it is, add it to the list of correct guesses
        goodGuesses.append(userGuess)
    elif isInList == 0:
        # If not, add it to incorrect guesses
        badGuesses.append(userGuess)

"""
This method checks for game over
"""
def isEndGame(guessWord):
    # Is the length of incorrect guesses longer than the number of strikes?
    if len(badGuesses) >= strikes:
        print ('Game Over')
        print ('The word was:',guessWord)
        endGame = 1
    else:
        endGame = 0
    return endGame

"""
This method checks for a win 
"""
def hasWon(guessWord):
    # Win by default 
    complete = 1
    for letter in guessWord:
        # If there is a letter in the word to guess that isn't in goodGuesses
        if letter not in goodGuesses:
            # The user has no longer won
            complete = 0
    if complete == 1:
        print('Win')
    return complete

"""
This method is used to draw the game. Print the number of strikes, the incorrect
guesses, the correct guesses and the word. For undiscovered letters, print '-'
"""
def draw(badGuesses, goodGuesses, guessWord,strikes):
    # Print the number of strikes 
    print("Strikes: {}/{}".format(len(badGuesses),strikes))
    print("")
    # Print the list of incorrect guesses
    print ('Incorrect letters: ',end='')
    for letter in badGuesses:
        print(letter, end=" ")
    print("\n")
    # Print the list of correct guesses
    print ('Correct letters: ',end='')
    for letter in goodGuesses[1:]:
        print(letter, end=" ")
    print("\n")
    # Print the word, use '-' for undiscovered letters
    for letter in guessWord:
        if letter in goodGuesses:
            print(letter, end="")
        else:
            print("-", end="")
    print("")

# Draw the game once 
draw(badGuesses, goodGuesses, guessWord,strikes)
# While gameOver = false and won = false 
while endGame == 0 and complete == 0:
    # Run the game back end...
    main(guessList)
    # Render the game 
    draw(badGuesses, goodGuesses, guessWord,strikes)
    # Is there a game over?
    endGame = isEndGame(guessWord)
    # Has the user won?
    complete = hasWon(guessWord)

