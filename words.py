import urllib
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


"""
This function will return true if the word has a definition that matches
the given part of speech. If it does not, the function will return False.

string -> Boolean
"""
def verify_part_of_speech(word, posp):
    url = 'https://www.merriam-webster.com/dictionary/' + word

    # error Handling if word does not exist in webster
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError:
        print("Word not in Webster")
        return False

    # look through webster html to confirm the given posp matches that of the word
    u = urllib.request.urlopen(url)
    soup = BeautifulSoup(u, 'html.parser')
    parts_of_speech = soup.findAll('a', {'class': 'important-blue-link'})
    for part in parts_of_speech:
        if posp in part:
            return True
    return False


"""
This function will put any word into its singular present tense. 

string -> string
"""
def singularize_word(word):
    url = 'https://www.merriam-webster.com/dictionary/' + word
    u = urllib.request.urlopen(url)
    soup = BeautifulSoup(u, 'html.parser')
    singular = str(soup.findAll('h1', {'class': 'hword'})[0])
    singularized_word = ''
    reached_word = False
    for char in singular:
        if char is '<' and reached_word:
            return singularized_word
        if reached_word:
            singularized_word = singularized_word + char
        if char == '>':
            reached_word = True


"""
Gets a word using the random word api

void -> string
"""
def get_word():
    r = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    wrd = r.text
    wrd = wrd[2:(len(wrd)-2)]
    return wrd
