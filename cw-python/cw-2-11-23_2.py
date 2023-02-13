#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed 
# (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
def spin_words(sentence):
    sentence_arr = sentence.split()
    resp = []
    for word in sentence_arr:
        if len(word) >= 5:
            resp.append(word[::-1])
        else: resp.append(word)
    return ' '.join((x for x in resp))