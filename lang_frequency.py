import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath) as data_file:
            data = data_file.read()
    return data


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text)
    capital_words = [word.upper() for word in words]
    word_counts = Counter(capital_words)

    most_common = {(count, letter.lower()) for letter, count in word_counts.most_common(10)}
    return most_common

if __name__ == '__main__':
    print('Enter the filepath: ', end='')
    text = load_data(input())
    while text is None:
        print('Oops, looks like you have a mistype in filepath!'
              '\nPlease, enter the valid path to the file: ', end='')
        text = load_data(input())
    most_frequent_words = get_most_frequent_words(text)

    print('The most common words: ', end='')
    for count, word in most_frequent_words:
        print('%s: %s times; ' % (word, count), end='')
    print()
