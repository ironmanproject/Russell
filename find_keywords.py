#!/usr/bin/env python3

"""Test Variables"""
string = 'hey Russell, where does your name come from?'

keywords = []
dull_words = ['hey', 'Russell', 'does', 'come']
def find_keywords(string):
    for word in string:
        if word in dull_words:
            continue
        keywords.append(word)
    print(keywords)
