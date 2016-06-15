#!/usr/bin/env python3
# coding: utf-8

import json

md5_answer = "4624d200580677270a54ccff86b9610e"
PHRASE = ''.join(sorted("poultryoutwitsants"))


# Experimenting with some structures to figure out how to approach multi word
# anagram solving.
# One thing would be to sort each word and try to do stuff with it but it feels
# like its taking us to the wrong path.
# The other cool thing that might be funnier to work with would be to create
# a histogram of each work by counting its letters and then try to see what
# math we can apply there to make our life easy. Cheers, wip!


def parse(data):
    """
    :param data: wordlist file that provided as language dictionary
    :return: canditate: a hashmap (dictionary) where we group the words, using
    as key their sorted characters.
    """
    canditates = {}
    for line in data:
        line = line.strip().lower()
        sorted_word = ''.join(sorted(line))

        if is_canditate(sorted_word):
            if sorted_word not in canditates:
                canditates[sorted_word] = []
            canditates[sorted_word].append(line)

    return canditates


def is_canditate(sorted_word, input_phrase):

    for idx, character in enumerate(sorted_word):
        if character not in input_phrase:
            break

        input_phrase = input_phrase.replace(character, "")
        # Our phrase, contains all the digits of the word!
        if len(sorted_word) == idx + 1:
            return True

    return False


def match_keys(word_keys, input_phrase):
    for word_key in word_keys:
        if is_canditate(word_key, input_phrase):
            reduced_phrase = input_phrase - word_key
            match_keys(word_keys, reduced_phrase)


def main():
    with open('wordlist') as input_file:
        canditates = parse(input_file)

    with open('canditates.json', 'w') as out_file:
        json.dump(canditates, out_file)

    match_keys(canditates.keys(), PHRASE)


if __name__ == '__main__':
    main()
