import collections

def binary_search(lst, target):  # binary_search(t_item, d_pair)
    left = 0
    right = len(lst)

    while left < right:
        mid = (left + right) // 2
        if lst[mid][0] == target[0]:
            return lst[mid][1] >= target[1]
        elif target[0] < lst[mid][0]:
            right = mid
        else:
            left = mid + 1
    return False

def score_check(str):
    alphabet = {"a": 1, "b": 3, "c": 2, "d": 2, "e": 1, "f": 3, "g": 3, "h": 1, "i": 1, "j": 4, "k": 4, "l": 2, "m": 2, "n": 1, "o": 1, "p": 3, "q": 4, "r": 1, "s": 1, "t": 1, "u": 2, "v": 3, "w": 3, "x": 4, "y": 3, "z": 4}
    score = 0
    for char in str:
        score += alphabet[char]
    return score


# テストケースの読み込み
print("どの入力ファイルを選びますか？")
print("small.txt：1  medium.txt：2  large.txt：3")
txt = int(input())
if txt == 1:
    ft = open("small.txt", "r")
    fout = open("small_answer.txt", "w")
elif txt == 2:
    ft = open("medium.txt", "r")
    fout = open("medium_answer.txt", "w")
elif txt == 3:
    ft = open("large.txt", "r")
    fout = open("large_answer.txt", "w")
else:
    print("ファイルが存在しません")
    exit()
testcase = ft.readlines()
ft.close()


for i, word in enumerate(testcase):
    testcase[i] = ''.join(sorted(word))  # testcaseの単語自身をソートした
    
testcase_items = []
for word in testcase:
    item = list(collections.Counter(list(word)).items())
    testcase_items.append(item)


# 事前にソートした辞書を読み込む
f = open("sort_words.txt", "r") 
new_dictionary = f.readlines()
f.close()
for i, words in enumerate(new_dictionary):
    new_dictionary[i] = words.split()
    
new_dictionary_items = []
for word in new_dictionary:
    item = list(collections.Counter(list(word[0])).items())
    new_dictionary_items.append(item)


for t_item in testcase_items:
    max_anagram = ""
    for i, d_item in enumerate(new_dictionary_items):
        exist = True
        for d_pair in d_item:
            if binary_search(t_item, d_pair) == False:
                exist = False
        if exist:
            if score_check(max_anagram) < score_check(new_dictionary[i][1]):
                max_anagram = new_dictionary[i][1]
    #print(max_anagram)
    fout.write(max_anagram)
    fout.write("\n")

fout.close()
                
                
            
    
    


