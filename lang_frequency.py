import re
from collections import Counter


def load_data(filepath):
    if filepath != '':
        with open(filepath) as data_file:
            data = data_file.read()
    else:
        data = -1
    return data


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text)
    cap_words = [word.upper() for word in words]
    word_counts = Counter(cap_words)

    s = 'Most common: '
    for letter, count in word_counts.most_common(10):
        s = format('%s%s ' % (s, letter.lower()))
    print(s)

if __name__ == '__main__':
    print('Enter the filepath:')
    text = -1
    while text == -1:
        text = load_data(input())
    get_most_frequent_words(text)
