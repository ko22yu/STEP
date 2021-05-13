def binary_search(lst, target):
    left = 0
    right = len(lst)

    while left < right:
        mid = (left + right) // 2
        if lst[mid][0] == target:
            return lst[mid][1]
        elif target < lst[mid][0]:
            right = mid
        else:
            left = mid + 1
    print("Error!")


def better_solution(random_word, dictionary):
    new_dictionary = []
    for words in dictionary:
        new_dictionary.append(words.split())

    sorted_random_word = ''.join(sorted(random_word))  # random_wordの単語自身をソートしたもの
    anagram = binary_search(new_dictionary, sorted_random_word)
    return anagram


def main():
    print("文字列を入力してください(英語)")
    str = input()
    
    # 事前にソートした辞書を読み込む
    try:
        f = open("sort_words.txt", "r") 
        new_dictionary = f.readlines()
    finally:
        f.close()

    print(better_solution(str, new_dictionary))



if __name__ == '__main__':
    main()
