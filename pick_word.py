import random
def pick_word():
    words = []
    with open('sowpods.txt') as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip()
            words.append(word)

    random_word = words[random.randint(0, len(words)+1)]
    return random_word
