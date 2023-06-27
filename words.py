def print_upper_words(words):
    '''print each word from a list on a seperate line, uppercased'''
    for word in words:
        print(word.upper())

word_list = ['dog', 'cat', 'hamster', 'rabbit', 'bird']
print_upper_words(word_list)


def print_upper_wordsE(words):
    '''print words from a list that start with the letter e, upper or lower'''
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

word_list = ['english', 'algebra', 'Engineering', 'science']
print_upper_wordsE(word_list)


def print_upper_words_specified(words, must_start_with):
    '''print words from a list that start with any of the specified letters, in uppercase'''
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter):
                print(word.upper())

word_list = ['soccer', 'football', 'baseball', 'basketball', 'Golf']
letters = {'s', 'g', 'b'}

print_upper_words_specified(word_list, letters)
