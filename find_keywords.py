#!/usr/bin/env python3

string = 'Hey Russell, where does your name come from?'

keywords = []
phrase = ''
dull_words = ['hey', 'Russell', 'does', 'come']
new_questions = ./new_questions.txt

def find_keywords(string):
  phrase = string.replace(',', '')
  words = phrase.split()
  for word in string:
    if word not in dull_words:
      keywords.append(word)
  return phrase
  return keywords


def find_commands(keywords, phrase):
  if 'weather' in keywords:
    if 'week' in keywords:
      print('This week looks beautiful!')
    elif 'tomorrow' in keywords:
      print('Tomorrow will be similar to today.')
    else:
      print('Currently it is Sunny with a high of 75 degrees.')
  elif 'time' in keywords:
    if 'meeting' or 'appointment' in keywords:
      print('Your next event is at 6pm')
    else:
      print('The current time is {}'.format(ctime(time())))
  elif 'your name' in phrase:
    print('I am named after my maker\'s grandfather')
  else:
    print('I am unsure of the answer to your inquiry.')
    print('I will make note of it so that I can answer it next time.')
    with open(new_questions, 'a') as f:
      f.write(phrase)


find_keywords(string)
find_commands(keywords, phrase)
