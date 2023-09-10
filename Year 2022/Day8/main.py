with open("input.txt", "r") as f:
    inp = f.read().splitlines()


#1
def check_largest(ls:list, num):
    num = int(num)
    for x in ls:
        x = int(x)
        if x >= num:
            return False
    return True

visible = []
for y in range(len(inp)):

    visible.append([])
    for x in range(len(inp[y])):
        visible[y].append("-")
    if y == 0 or y == len(inp)-1:       #first and last row
        for x in range(len(inp[y])):
            visible[y][x] = inp[y][x]
    else:

        for x in range(len(inp[y])):
            tree = inp[y][x]
            if x == 0 or x == len(inp[y]) -1:   #first and last tree
                visible[y][x] = tree
            else:
                if check_largest(inp[y][:x], tree): #left
                    visible[y][x] = "<" + tree
                if check_largest(inp[y][x+1:], tree): #right
                    visible[y][x] = tree + ">"
                    
                ls = []     #vertical list
                for row in inp:
                    ls.append(row[x])
                if check_largest(ls[:y], tree): #up
                    visible[y][x] = "u" + tree
                if check_largest(ls[y+1:], tree): #down
                    visible[y][x] = tree + "d"

sum = 0
for y in visible:   #pretty print
    #print(y)
    for x in y:
        if x != "-":
            sum += 1
print(f"Aufg1: {sum} trees visible")


#2
visible = inp

visible_score = []
for y in range(len(inp)):
    visible_score.append([])
    for x in range(len(inp[y])):
        visible_score[y].append(0)
        num = int(inp[y][x])
        u = 0
        d = 0
        l = 0
        r = 0
        ls = []     #vertical list
        for row in inp:
            ls.append(row[x])
        if y != 0:      #up
            for j in range(len(ls[:y])):
                elem = ls[y-j-1]
                u += 1
                if int(elem) >= num:
                    break
        if y != len(inp[y])-1:      #down
            for elem in ls[y+1:]:
                d += 1
                if int(elem) >= num:
                    break
        if x != 0:      #left
            for j in range(len(inp[y][:x])):
                elem = inp[y][x-j-1]
                l += 1
                if int(elem) >= num:
                    break
        if x != len(inp)-1: #right
            for elem in inp[y][x+1:]:
                r += 1
                if int(elem) >= num:
                    break
        #print(f"{u} * {l} * {r} * {d} = {u * d * l * r} {num} {inp[y]} {x}")
        visible_score[y][x] = u * d * l * r

max_score = 0
for y in visible_score:   #pretty print
    #print(y)
    for x in y:
        if x > max_score:
            max_score = x

print(f"Aufg2: {max_score} highest scenic score")
