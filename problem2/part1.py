
rock = 1 # A, X
paper = 2 # B ,Y
scissors = 3 # C, Z

map = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

def get_win_score(p1, p2):
    loss = 0
    win = 6
    draw = 3
    #gets p2s score.
    if p1 == 'A':
        if p2 == 'X':
            return draw
        elif p2 == 'Y':
            return win 
        else:
            return loss
    elif p1 == 'B':
        if p2 == 'X':
            return loss 
        elif p2 == 'Y':
            return draw 
        else:
            return win
    elif p1 == 'C':
        if p2 == 'X':
            return win
        elif p2 == 'Y':
            return loss 
        else:
            return draw
    return 0

def make_test_input(input, filename):
    with open(filename, 'w') as f: 
        f.writelines(input)


def get_output(filename):
    score = 0    
    with open(filename, 'r') as f:
        for line in f:
            first = line[0]
            second = line[2]

            score += map[second]
            score += get_win_score(first,second)
            #print('first, second, win_score', first, second, get_win_score(first,second))
    return score

def generic_tester(input, expected_output):
    filename = 'test_input.txt'
    make_test_input(input, filename)
    with open(filename, 'r') as f:
        for line in f:
            print(line)
    result = get_output(filename)
    assert result == expected_output, f'expected: {expected_output}, actual: {result}'

def test_all_same():
    input = ['A X\n', 'B Y\n', 'C Z\n']
    generic_tester(input, 15)

def test_rock_paper():
    input = ['A Y']
    generic_tester(input, 8)

def test_rock_sci():
    input = ['A Z']
    generic_tester(input, 3)

def test_paper_rock():
    input = ['B X']
    generic_tester(input, 1)

def test_paper_sci():
    input = ['B Z']
    generic_tester(input, 9)

def test_sci_rock():
    input = ['C X']
    generic_tester(input, 7)

def test_sci_paper():
    input = ['C Y']
    generic_tester(input, 2)


test_all_same()
test_rock_paper()
test_rock_sci()
test_paper_rock()
test_paper_sci()
test_sci_rock()
test_sci_paper()

print(get_output('input.txt'))
