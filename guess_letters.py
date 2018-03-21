from drawings import*
# winner, head, r_arm, l_arm, l_leg, total, body


def guess_letters(word):
    guessed = "_" * len(word)
    guessed = list(guessed)

    word = list(word)

    lstGuessed = []

    letter = ''
    count = 7
    while count != 0:
        if letter.upper() in lstGuessed:
            # checks if was used before
            letter = ''
            print("Already guessed!!")

        elif letter.upper() in word:
            # checks if the letter in the word
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        else:
            # prints the result so far
            print(''.join(guessed))
            if letter is not '':
                # adds to the list of used letters
                lstGuessed.append(letter.upper())
            letter = input("guess letter: ")
            if letter.upper() not in word and letter.upper() not in lstGuessed and letter !='' :
                # counts guesses and draws a pics accordingly
                count -= 1
                if count == 6:
                    print(head())
                elif count == 5:
                    print(body())
                elif count == 4:
                    print(l_arm())
                elif count == 3:
                    print(r_arm())
                elif count == 2:
                    print(l_leg())
                elif count == 1:
                    print(total())
                    break

        if '_' not in guessed:
            # if the is no more letter to guess in the lst word player wins
            print('==================\n'
                  'The word is:')
            print(''.join(guessed))
            print(winner())
            break
