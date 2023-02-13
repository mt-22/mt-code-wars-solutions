#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters 
# is an isogram. Assume the empty string is an isogram. Ignore letter case.
def is_isogram(string):
    map = {}
    if len(string) <= 0: return True
    for index, letter in enumerate(string):
        if str(letter).lower() in map:
            return False
        map[letter.lower()] = index
    return True