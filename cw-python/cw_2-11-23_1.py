#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).
#  The next words should be always capitalized.
def to_camel_case(text):
    string = ""
    for index, letter in enumerate(text):
        if text[index-1] == '_' or text[index-1] == '-':
            string += letter.upper()
        else: string += letter
    return string.replace('_', '').replace('-', '')