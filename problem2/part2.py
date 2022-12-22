
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

    p1s = ['A','B','C']
    p1s = p1s + p1s

    p2s = ['X','Y','Z']
    p2s = p2s + p2s
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

def determine_alt_move(p1, win_lose_draw):
    #return alternative move
    if win_lose_draw == 'X':
        #lose
        if p1 == 'A':
            return 'Z'
        elif p1 == 'B':
            return 'X'
        else:
            return 'Y'
    elif win_lose_draw == 'Y':
        if p1 == 'A':
            return 'X'
        elif p1 == 'B':
            return 'Y'
        else:
            return 'Z'
        #draw
    else:
        #win
        if p1 == 'A':
            return 'Y'
        elif p1 == 'B':
            return 'Z'
        else:
            return 'X'

def make_test_input(input, filename):
    with open(filename, 'w') as f: 
        f.writelines(input)


def get_output(filename):
    score = 0    
    with open(filename, 'r') as f:
        for line in f:
            first = line[0]
            second = determine_alt_move(first, line[2])

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

# def test_all_same():
#     input = ['A X\n', 'B Y\n', 'C Z\n']
#     generic_tester(input, 15)
#x=lose,y=draw,z=win
def test_rock_win():
    input = ['A Z']
    generic_tester(input, 8)

def test_rock_lose():
    input = ['A X']
    generic_tester(input, 3)

def test_rock_draw():
    input = ['A Y']
    generic_tester(input, 4)

def test_paper_win():
    input = ['B Z']
    generic_tester(input, 9)

def test_paper_lose():
    input = ['B X']
    generic_tester(input, 1)

def test_paper_draw():
    input = ['B Y']
    generic_tester(input, 5)

def test_sci_win():
    input = ['C Z']
    generic_tester(input, 7)

def test_sci_lose():
    input = ['C X']
    generic_tester(input, 2)

def test_sci_draw():
    input = ['C Y']
    generic_tester(input, 6)

test_paper_win()
test_paper_lose()
test_paper_draw()
test_rock_win()
test_rock_lose()
test_rock_draw()
test_sci_win()
test_sci_lose()
test_sci_draw()

print(get_output('input2.txt'))
