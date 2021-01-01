import time
import api
import jokes
import random

parts_of_speech = ['noun', 'adjective', 'verb']

"""
main
"""
if __name__ == '__main__':
    is_part = False

    part = random.choice(parts_of_speech)
    print(part)

    while not is_part:
        word = api.get_word()
        print(word)
        is_part = api.verify_part_of_speech(word, part)
        print(is_part)
        time.sleep(.35)
    print(api.singularize_word(word))



