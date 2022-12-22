def get_upper_val(char):
    return ord(char) - 13 - 25

def get_lower_val(char):
    return ord(char) - 96

def get_val(char):
    if char.isupper():
        return get_upper_val(char)
    else:
        return get_lower_val(char)


def get_output(filename):
    score = 0
    with open(filename, 'r') as f:
        for line in f:
            s = set()
            #split the line
            tmp_score = 0

            half = len(line)//2
            print(f"first half: {line[:half]}")
            print(f"second half: {line[half:]}")

            for char in line[:half]:
                s.add(char)
            
            counted = set()
            for char in line[half:]:
                if char in s and char not in counted:
                    print(f"{char} in both")
                    tmp_score += get_val(char)
                    counted.add(char)

            print(f"tmp score: {tmp_score}")
            score += tmp_score
            print(f"tmp score: {score}\n")
            

    return score

res = get_output('input.txt')

print(res)




                
            
