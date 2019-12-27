import json
import time

with open("dictionary.json") as data:
    o_words = json.load(data)
start_time = time.time()

def anagrams(letters):

    def solve(words, word, n_so_far):
        if word in set_words and word not in good_words:
            good_words.append(word)
        if words == [] or len(word) == 6:
            return
        l_word = len(word)
        for x in range(6):
            if x not in n_so_far:
                copy_n_so_far = list(n_so_far)
                copy_n_so_far.append(x)
                solve([w for w in words if w[:l_word] == word], word + letters[x], copy_n_so_far)

    good_words = []
    words_to_six = []
    for word in o_words:  # Removes >6 letter words
        if len(word) > 2 and len(word) < 7:
            words_to_six.append(word)

    set_words = set(words_to_six)

    solve(words_to_six, "", [])

    print(sorted(good_words, key=len, reverse=True))
    print(time.time() - start_time)

def wordhunt(letters):

    def move(n, words, word, n_so_far):  # Go thru each letter
        if word in set_words and word not in good_words:
            good_words.append(word)
        if words == [] or len(word) == 16:
            return
        l_word = len(word)
        for x in combos_lst[n]:
            if x not in n_so_far:
                copy_n_so_far = list(n_so_far)
                copy_n_so_far.append(x)
                move(x, [w for w in words if w[:l_word] == word], word + letters[x], copy_n_so_far)

    word_over_three_letters = []

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

    for word in o_words:  # Removes <3 >16 letter words
        if len(word) > 2 and len(word) < 17:
            word_over_three_letters.append(word)

    set_words = set(word_over_three_letters)

    good_words = []

    for l in range(16):
        move(l, word_over_three_letters, letters[l], [l])
        
    print(sorted(good_words, key=len, reverse=True))
    print(time.time() - start_time)

#wordhunt("rorddmflbceiibae")
anagrams("eahnsl")
