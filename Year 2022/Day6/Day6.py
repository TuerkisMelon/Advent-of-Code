with open("input.txt", "r") as f:
    inp = f.read()

#1
marker = ""
marker_pos = -1
for i in range(len(inp)-4):
    if len(marker) == 4:
        break
    else:
        marker_pos += 1
        marker = inp[marker_pos:marker_pos+4]
        for char in marker:
            if len(marker.replace(char, "")) != 3:
                marker = ""

print(f"Aufg 1: {marker_pos + 4} {marker}")

#2
marker = ""
marker_pos = -1
for i in range(len(inp)-14):
    if len(marker) == 14:
        break
    else:
        marker_pos += 1
        marker = inp[marker_pos:marker_pos+14]
        for char in marker:
            if len(marker.replace(char, "")) != 13:
                marker = ""

print(f"Aufg 2: {marker_pos + 14} {marker}")
