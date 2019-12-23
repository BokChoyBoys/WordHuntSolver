import json
import time
start_time = time.time()

def move(n, words, word, n_so_far): #Go thru each letter
    if word in word_over_three_letters:
        good_words.append(word)
    if words == [] or len(word) == 16:
        return
    for x in combos_lst[n]:
        if x not in n_so_far:
            y = list(n_so_far)
            y.append(x)
            move(x, check_let(word, words, len(word)), word + letters[x], y)


def check_let(letter, words, n):  #Checks letter if matches in words
    x = []
    for word in words:
        if word[0:n] == letter:
            x.append(word)
    return x

with open("dictionary.json") as data:
    words = json.load(data)

word_over_three_letters = []
letters = "ttadsapahunolfbh"
letter = letters[0]

combos_lst = [[1, 4, 5],
          [0, 2, 4, 5, 6],
          [1, 3, 5, 6, 7],
          [2, 6, 7],
          [0, 1, 5, 8, 9],
          [0, 1, 2, 4, 6, 8, 9, 10],
          [1, 2, 3, 5, 7, 9, 10, 11],
          [2, 3, 6, 10, 11],
          [4, 5, 9, 12, 13],
          [4, 5, 6, 8, 10, 12, 13, 14],
          [5, 6, 7, 9, 11, 13, 14, 15],
          [6, 7, 10, 14, 15],
          [8, 9, 13],
          [8, 9, 10, 12, 14],
          [9, 10, 11, 13, 15],
          [10, 11, 14]]

for word in words: #Removes <2 letter words
    if len(word) > 2 and len(word) < 17:
        word_over_three_letters.append(word)

good_words = []

for l in range(16):
    move(l, word_over_three_letters, letters[l], [l])
print(sorted(good_words, key=len, reverse = True))
print(time.time() - start_time)
