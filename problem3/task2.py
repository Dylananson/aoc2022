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
        count = 0
        set1 = set()
        set2 = set()
        set3 = set()
        cur = []

        for line in f:
            cur.append(line)

            #split the line

            if count == 0:
                set1 = set(line[:-1])
            if count == 1:
                set2 = set(line[:-1])
            if count == 2:
                set3 = set(line[:-1])
            print(count, cur, line, set1,set2,set3)
            count += 1

            tmp_score = 0
            if count == 3:
                count = 0
                similar = set1.intersection(set2).intersection(set3)
                print(f"{similar} in both")
                print(f"set1 in set2 {set1.intersection(set2)}")
                print(f"set2 in set3 {set2.intersection(set3)}")
                print(f"set1 in set3 {set1.intersection(set3)}")
                print(cur)
                cur = []
                set1 = set()
                set2 = set()
                set3 = set()
                for char in list(similar):
                    tmp_score += get_val(char)
                    score += tmp_score

                    print(f"tmp score: {tmp_score}")
                    print(f"score: {score}\n")
        

    return score

res = get_output('input.txt')

print(res)




                
            
