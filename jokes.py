import sex_with_me
import pickup_lines
import bar_jokes
import yo_mama
import back_in_my_day
import random

"""
noun
adjective

string -> string
"""
def back_in_my_day():
    word = random.choice(back_in_my_day.back_in_my_day_word)
    prompt = 'Back In My Day:\n' \
             'Back in my day we didn\'t have ' + word + ', ________.\n'
    return prompt


"""
adjective

string -> string
"""
def yo_mama():
    word = random.choice(yo_mama.yo_mama_word)
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
    word = random.choice(sex_with_me.sex_with_me_word)
    prompt = 'Sex With Me:\n' \
             'Sex with me is like ' + word + ', ________.\n'
    return prompt


"""
noun

string -> string
"""
def bar_joke():
    word = random.choice(bar_jokes.bar_joke_word)
    prompt = '185:\n' \
             '___ ' + word + ' walk into a bar, ________.\n'
    return prompt


"""
noun

string -> string
"""
def pickup_lines():
    word = random.choice(pickup_lines.pickup_lines_word)
    prompt = 'Pickup Lines:\n' \
             'Hey _____, are you ' + word + '? Because ________.\n'
    return prompt



