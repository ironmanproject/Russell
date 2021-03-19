#!/usr/bin/env python3


def find_commands(keywords, phrase):
  if 'weather' in keywords:
    if 'week' in keywords:
      print('This week looks beautiful!')
    elif 'tomorrow' in keywords:
      print('Tomorrow will be similar to today.')
    else:
      print('Currently it is Sunny with a high of 75 degrees.')
  if 'time' in keywords:
    if 'meeting' or 'appointment' in keywords:
      print('Your next event is at 6pm')
    else:
      print('The current time is {}'.format(ctime(time()))
  if 'your name' in phrase:
    print('I am named after my maker\'s grandfather')
  else:
    print('I am unsure of the answer to your inquiry.')
    print('I will make note of it so that I can answer it next time.')
    with open(new_questions.txt, 'a') as f:
      f.write(phrase)

