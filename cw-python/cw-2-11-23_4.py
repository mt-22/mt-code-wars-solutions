#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    area = '(' + ''.join(str(x) for x in n[:3]) + ')'
    return f'{area} {"".join(str(x) for x in n[3:6])}-{"".join(str(x) for x in n[6:])}'