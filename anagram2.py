import collections

def score_check(str):
    alphabet = {"a": 1, "b": 3, "c": 2, "d": 2, "e": 1, "f": 3, "g": 3, "h": 1, "i": 1, "j": 4, "k": 4, "l": 2, "m": 2, "n": 1, "o": 1, "p": 3, "q": 4, "r": 1, "s": 1, "t": 1, "u": 2, "v": 3, "w": 3, "x": 4, "y": 3, "z": 4}
    score = 0
    for char in str:
        score += alphabet[char]
    return score


def main():
    # テストケースの読み込み
    print("どの入力ファイルを選びますか？")
    print("small.txt：1  medium.txt：2  large.txt：3")
    txt = int(input())
    if txt == 1:
        fin = open("small.txt", "r")
        fout = open("small_answer.txt", "w")
    elif txt == 2:
        fin = open("medium.txt", "r")
        fout = open("medium_answer.txt", "w")
    elif txt == 3:
        fin = open("large.txt", "r")
        fout = open("large_answer.txt", "w")
    else:
        print("ファイルが存在しません")
        exit()
    try:
        testcase = fin.readlines()
    finally:
        fin.close()


    for i, word in enumerate(testcase):
        testcase[i] = ''.join(sorted(word))  # testcaseの単語自身をソートした


    # 事前にソートした辞書を読み込む
    f = open("sort_words.txt", "r")
    try:
        new_dictionary = f.readlines()
    finally:
        f.close()
    for i, words in enumerate(new_dictionary):
        new_dictionary[i] = words.split()


    for t_word in testcase:
        max_anagram = ""
        t_word_set = set(t_word)
        t_word_counter = collections.Counter(t_word)
        for d_word in new_dictionary:
            exist = True
            d_word_set = set(d_word[0])
            d_word_counter = collections.Counter(d_word[0])
            if t_word_set >= d_word_set:
                for d_char in d_word_set:
                    if t_word_counter[d_char] < d_word_counter[d_char]:
                        exist = False
                        break
                if exist:
                    if score_check(max_anagram) < score_check(d_word[0]):
                        max_anagram = d_word[1]
        print(max_anagram)
        fout.write(max_anagram)
        fout.write("\n")

    fout.close()


if __name__ == '__main__':
    main()
