import sex_with_me as sex_with_me_words
import pickup_lines as pickup_lines_words
import bar_jokes as bar_jokes_words
import yo_mama as yo_mama_words
import back_in_my_day as back_in_my_day_words
import random

"""
noun
adjective

string -> string
"""
def back_in_my_day():
    word = random.choice(back_in_my_day_words.back_in_my_day_word)
    prompt = 'Back In My Day:\n' \
             'Back in my day we didn\'t have ' + word + ', ________.\n'
    return prompt


"""
adjective

string -> string
"""
def yo_mama():
    word = random.choice(yo_mama_words.yo_mama_word)
    prompt = 'Yo Mama:\n' \
               'Yo mama is so ' + word + '!\n' \
               '(How ' + word + ' is she?)\n' \
               'She\'s so ' + word + ', that ________.\n'
    return prompt


"""
noun

string -> string
"""
def sex_with_me():
    word = random.choice(sex_with_me_words.sex_with_me_word)
    prompt = 'Sex With Me:\n' \
             'Sex with me is like ' + word + ', ________.\n'
    return prompt


"""
noun

string -> string
"""
def bar_joke():
    word = random.choice(bar_jokes_words.bar_joke_word)
    prompt = '185:\n' \
             '___ ' + word + ' walk into a bar, ________.\n'
    return prompt


"""
noun

string -> string
"""
def pickup_lines():
    word = random.choice(pickup_lines_words.pickup_lines_word)
    prompt = 'Pickup Lines:\n' \
             'Hey _____, are you ' + word + '? Because ________.\n'
    return prompt



