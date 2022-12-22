# load into memory
mx = 0 
sum = 0

with open("input.txt", "r") as f:
    for line in f:
        x = line[:-1]
        if x:
            x = int(x)
        else:
            x = 0

        if line == '\n':
            mx = max(mx, sum)
            print(x, sum, mx)
            sum = x
        else:
            sum += x
        print(x,  sum, mx)

mx = max(mx, sum)            

print(mx) 




