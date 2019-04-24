from __future__ import print_function
import json
from pattern.en import lexeme
import string

def decompress_tags (text):
    text = text.replace('<s>', '<span color="brown">')
    text = text.replace('<k>', '<span color="green">')
    text = text.replace('<c>', '<span color="yellow">')
    text = text.replace('</>', '</span>')
    text = text.replace('<x>', '<span>')
    return text


for letter in list(string.ascii_lowercase):
    filepath = 'C:\\DicData\\' + letter + '5.txt'
    with open(filepath) as f:
        data = json.load(f)
    for w in data:
        print('|'.join(lexeme(w['lemma'].encode('utf-8'))))
        print(decompress_tags(w['description']).encode('utf-8'))
        print('')

