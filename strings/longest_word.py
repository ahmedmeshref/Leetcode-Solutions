import re


def LongestWord(sentence):
    # code goes here
    words = re.findall(r'[A-Za-z0-9]+', sentence)
    if not words:
        return ''
    # max_word_so_far = words[0]
    # for word in words:
    #     if len(max_word_so_far) < len(word):
    #         max_word_so_far = word
    return max(words, key=len)


# keep this function call here
print(LongestWord(input()))
