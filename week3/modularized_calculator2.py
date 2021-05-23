#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1


def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1


def read_brackets_left(line, index):
    token = {'type': 'BRACKETS_LEFT'}
    return token, index + 1


def read_brackets_right(line, index):
    token = {'type': 'BRACKETS_RIGHT'}
    return token, index + 1


def found_inside_brackets(tokens):
    # 渡されたtokensのリストから最も内側の()の位置を求める
    right = tokens.index({'type': 'BRACKETS_RIGHT'})
    for index in range(right, -1, -1):
        if tokens[index]['type'] == 'BRACKETS_LEFT':
            left = index
            break  # 最初に見つかったものをleftに代入する
    # print("found_inside_brackets : \n", "left : ", left, "right : ", right, "\n")  # デバッグ用
    return (left, right)


def tokenize(line):
    tokens = []
    index = 0  # 今見ている位置
    while index < len(line):
        if line[index].isdigit():  # 今見ているものが数字なら
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_brackets_left(line, index)
        elif line[index] == ')':
            (token, index) = read_brackets_right(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    # print("tokenize : ", tokens, "\n")  # デバッグ用
    return tokens


def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token

    # 1回目の評価で'*'と'/'を処理する
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'TIMES':
            number = tokens[index-1]['number'] * tokens[index+1]['number']
            tokens[index-1:index+2] = [{'type': 'NUMBER', 'number': number}]
        elif tokens[index]['type'] == 'DIVIDE':
            number = tokens[index-1]['number'] / tokens[index+1]['number']
            tokens[index-1:index+2] = [{'type': 'NUMBER', 'number': number}]
        index += 1

    # 2回目の評価で'+'と'-'を処理する
    index = 1
    answer = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1

    # print("evaluate : ", tokens, "\n")  # デバッグ用
    return answer


def evaluate_inside_brackets(tokens):
    while {'type': 'BRACKETS_LEFT'} in tokens and {'type': 'BRACKETS_RIGHT'} in tokens:
        (left, right) = found_inside_brackets(tokens)
        answer_inside_brackets = evaluate(tokens[left+1:right])  # ()内だけを渡して計算を行ってもらう
        tokens[left:right+1] = [{'type': 'NUMBER', 'number': answer_inside_brackets}]
        # print("evaluate_inside_brackets : ", tokens, "\n")  # デバッグ用
    return tokens


def test(line):
    tokens = tokenize(line)
    tokens = evaluate_inside_brackets(tokens)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1")
    test("1+2")
    test("1.0+2")
    test("1.0+2.0")
    test("1.0+2.1-3")
    test("3.0+4*2-1/5")
    test("3+4.0*2-1.0/5")
    test("3.0+4.0*2.0-1.0/5.0")
    test("3.0*4-5-10.0/2")
    test("(3.0+4*(2-1))/5")
    test("(3.0+4.0*(2-1))/5")
    test("(3.0+4.0*(2-1.0))/5")
    test("(3.0+4.0*(2.0-1.0))/5.0")
    test("((3*4+2)/2)*1.5")
    test("3.0+((2*1.5)/3.0)")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    tokens = evaluate_inside_brackets(tokens)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
