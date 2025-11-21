#!/usr/bin/python3
def no_c(word: str):
    new_word = ""
    for w in word:
        if w == "c" or w == "C":
            continue
        new_word += w
    return new_word
