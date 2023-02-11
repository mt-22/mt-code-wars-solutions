def to_camel_case(text):
    string = ""
    for index, letter in enumerate(text):
        if text[index-1] == '_' or text[index-1] == '-':
            string += letter.upper()
        else: string += letter
    return string.replace('_', '').replace('-', '')