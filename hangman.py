from guess_letters import guess_letters
from pick_word import pick_word

# picks random word via pick_word.py module
word = pick_word()
print('\nLet\'s begin our Hangman game.')
print('The word consists of '+str(len(word))+' letters')
guess_letters(word)
print('\n'+word)