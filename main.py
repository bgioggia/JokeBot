import time
import api
import jokes

"""
main
"""
if __name__ == '__main__':
    word = api.get_word()
    print(word)
    noun = api.verify_noun(word)
    print(noun)
    if noun:
        time.sleep(.35)
        print(api.singularize_word(word))
