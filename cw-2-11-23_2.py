def spin_words(sentence):
    sentence_arr = sentence.split()
    resp = []
    for word in sentence_arr:
        if len(word) >= 5:
            resp.append(word[::-1])
        else: resp.append(word)
    return ' '.join((x for x in resp))