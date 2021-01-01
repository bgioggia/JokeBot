"""
vowel_start determines if a given string starts with a vowel
for grammatical purposes.

string -> boolean
"""
def vowel_start(word):
    vow = str.lower(word[0])
    vowels = ['a', 'e', 'i', 'o', 'u']
    return vow in vowels


"""
noun

string -> string
"""
def worlds_worst(word):
    prompt = 'World\'s Worst:\n\n' \
               'Respond with a quote from the world\'s worst ' + word + '!\n'
    return prompt


"""
noun
adjective

string -> string
"""
def back_in_my_day(word):
    prompt = 'Back In My Day:\n' \
               'Fill in the following blank with your Joke!\n\n'\
               'Back in my day we didn\'t have ' + word + ', ________\n'
    return prompt


"""
adjective

string -> string
"""
def yo_mama(word):
    prompt = 'Yo Mama:\n' \
               'The world is full of Yo Mama jokes.\nTry making this one a compliment!\n\n'\
               'Yo mama is so ' + word + '\n' \
               '(how ' + word + ' is she?)\n' \
               'She\'s so ' + word + ', that ________\n'
    return prompt


"""
noun

string -> string
"""
def sex_with_me(word):
    if vowel_start(word):
        prompt = 'Sex With Me:\n' \
                 'It\'s easy to make a bad sex joke.\n Try to be clever and creative instead of ' \
                 'going for shock value with he following prompt!\n\n'\
                 'Sex with me is like an' + word + ', ________\n'
    else:
        prompt = 'Sex With Me:\n' \
                 'It\'s easy to make a bad sex joke.\n Try to be clever and creative instead of ' \
                 'going for shock value with he following prompt!\n\n'\
                 'Sex with me is like a' + word + ', ________\n'
    return prompt


"""
noun

string -> string
"""
def bar_joke(word):
    prompt = '185:\n' \
             'Come up with a clever pun or story for the following prompt!\n' \
             'you can choose any number you want at the start!,\n\n'\
             '185 ' + word + '(s) walk into a bar, ________\n'
    return prompt


"""
noun

string -> string
"""
def pickup_lines(word):
    if vowel_start(word):
        prompt = 'Pickup Lines:\n' \
             'Come up with your best pickup line using the following prompt!\n' \
             'Remember being creepy isn\'t funny or attractive!,\n\n'\
             'Hey <honorific>, are you a ' + word + ' because ________\n'
    else:
        prompt = 'Pickup Lines:\n' \
             'Come up with your best pickup line using the following prompt!\n' \
             'Remember being creepy isn\'t funny or attractive!,\n\n'\
             'Hey <honorific>, are you an ' + word + ' because ________\n'
    return prompt



