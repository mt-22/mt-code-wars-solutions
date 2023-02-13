#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    return  ' '.join(str(alph.index(x.lower()) + 1)  for x in text if x.isalpha())