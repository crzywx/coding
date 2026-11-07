def match_words(words):
    crt = 0
    lst = []
    for word in words:
        if len(word) > 0 and word[0] == word[-1]:
            crt += 1
            lst.append(word)

    print("List of words that start and end with the same\n" , lst)
    return crt

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words that start and end with the same letters:" , count)



