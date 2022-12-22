# load into memory
mx = 0 
sum = 0
top_three = [0, 0, 0]

def check_in_top_three(sum, top_three):
    top_three.append(sum)
    top_three = sorted(top_three, reverse=True)

    return top_three[:-1] 

def sum_list(lst):
    total = 0
    for val in lst:
        total += val
    return total

with open("input.txt", "r") as f:
    for line in f:
        x = line[:-1]
        if x:
            x = int(x)
        else:
            x = 0

        if line == '\n':
            top_three = check_in_top_three(sum, top_three) 
            print(x, sum, top_three, sum_list(top_three))
            sum = x
        else:
            sum += x
        print(x,  sum, mx)

mx = max(mx, sum)            

top_three = check_in_top_three(sum, top_three)

total = 0

for val in top_three:
    total += val

print(top_three, total)




