import time
import words
import jokes
import random


# this distribution of parts of speech should give all jokes roughly equal probability.
parts_of_speech = ['noun', 'noun', 'noun', 'noun', 'noun', 'adjective', 'adjective']  # , 'verb']

"""
main
"""
if __name__ == '__main__':
    print()
    print(jokes.back_in_my_day("apple"))
    print(jokes.back_in_my_day("pear"))
    """is_part = False
    word = ''
    part = random.choice(parts_of_speech)

    print(part)

    while not is_part:
        word = api.get_word()
        print(word)
        is_part = api.verify_part_of_speech(word, part)
        print(is_part)
        time.sleep(.35)
    print(api.singularize_word(word))"""



