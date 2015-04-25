#!/usr/bin/python

# A simple program to find my kids names in the dictionary to show them a
# little programming.

_WORDS = '/usr/share/dict/words'

def getWords():
  print 'Getting words from {0}...'.format(_WORDS)
  f = open(_WORDS)
  lines = f.readlines()
  print 'I found {0} words.'.format(len(lines))
  return lines

def findByName(words, name):
  print '---- Searching for {0}...'.format(name)
  for word in words:
    smallword = word.lower()
    if name.lower() in smallword:
      print '{0} is in {1}!'.format(name, word.strip())

def findMyWords():
  print 'Hi Blake, Reade, and Piper!'
  words = getWords()
  findByName(words, 'Reade')
  findByName(words, 'Blake’)
  findByName(words, 'Piper')

if __name__ == '__main__':
  findMyWords()
