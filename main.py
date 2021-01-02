import time
import words
import jokes
import random

"""

string, string -> string
"""
def prompt_from_word(word, part):
    if part == 'noun':
        jokes_list = [jokes.worlds_worst(word), jokes.back_in_my_day(word), jokes.sex_with_me(word),
                      jokes.bar_joke(word), jokes.pickup_lines(word)]
        return random.choice(jokes_list)
    elif part == 'adjective':
        jokes_list = [jokes.back_in_my_day(word), jokes.yo_mama(word)]
        return random.choice(jokes_list)



"""
void -> string
"""
def prompt():
    # this distribution of parts of speech should give all jokes roughly equal probability.
    parts_of_speech = ['noun', 'noun', 'noun', 'noun', 'noun', 'adjective', 'adjective']  # , 'verb']
    is_part = False
    word = ''
    part = random.choice(parts_of_speech)

    while not is_part:
        word = words.get_word()
        is_part = words.verify_part_of_speech(word, part)
        time.sleep(.35)

    joke = prompt_from_word(word, part)
    return joke

"""
main
"""
if __name__ == '__main__':
    print()
    print('placeholder')



