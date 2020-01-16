# Wrap each of the 4 blocks of code in function definitions, then use the timeit module to
# time each one.
#
# Remember to import timeit at the start of the file.
#
# My solution will use a slightly different approach, to save time in the video. The test of
# whether your solution works is if successfully times all 4 approaches to capitalising the 
# characters and words in text

import timeit

text = "what have the romans ever done for us"

def capital_str():
    capitals = [char.upper() for char in text]
    return capitals
    # print(capitals)


# use map
def map_capital_str():
    map_capitals = list(map(str.upper, text))
    # print(map_capitals)
    return map_capitals

def capital_word():
    words = [word.upper() for word in text.split()]
    # print(words)
    return words


# use map
def map_capital_word():
    map_words = list(map(str.upper, text.split()))
    # print(map_words)
    return map_words

if __name__ == "__main__":
    # print(timeit.timeit("capital_str()", setup="from __main__ import capital_str", number=1000))
    # print(timeit.timeit("map_capital_str()", setup="from __main__ import map_capital_str", number=1000))
    # print(timeit.timeit("capital_word()", setup="from __main__ import capital_word", number=1000))
    # print(timeit.timeit("map_capital_word()", setup="from __main__ import map_capital_word", number=1000))

    print(timeit.timeit(capital_str, number=100000))
    print(timeit.timeit(map_capital_str, number=100000))
    print(timeit.timeit(capital_word, number=100000))
    print(timeit.timeit(map_capital_word, number=100000))

