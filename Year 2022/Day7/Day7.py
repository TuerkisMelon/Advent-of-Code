with open("input.txt", "r") as f:
    inp = f.read().splitlines()

path = ""
folders = {"/root":0}

for line in inp:
    line = line.split(" ")
    if line[0] == "$":
        if line[1] == "ls":
            pass
        else:
            if line[2] == "/":
                path = "/root"
            elif line[2] == "..":
                path = path[:path.rindex("/")]
            else:
                path = path + "/" + line[2]
                folders[path] = 0
    else:
        if line[0] != "dir":
            temp_path = path
            while temp_path != "":
                folders[temp_path] += int(line[0])
                temp_path = temp_path[:temp_path.rindex("/")]

#1
sum = 0
for folder in folders:
    val = folders[folder]
    if val < 100000:
        sum += val

print(f"Aufg 1 {sum}")


#2
curr_size = folders["/root"]
max_size = 70000000
available_size = max_size - curr_size
needed_size = 30000000
remaining_size = needed_size - available_size

delete_candidates = []

for folder in folders:
    val = folders[folder]
    if val >= remaining_size:
        delete_candidates.append([folder, val])

        
changed = True
while changed:
    changed = False
    for i in range(len(delete_candidates) -1):         #sorting delete candidates
        val = delete_candidates[i][1]
        if val > delete_candidates[i+1][1]:
            changed = True
            temp = delete_candidates[i]
            delete_candidates[i] = delete_candidates[i+1]
            delete_candidates[i+1] = temp

print(delete_candidates)
print(f"Aufg 2 {delete_candidates[0]}")
