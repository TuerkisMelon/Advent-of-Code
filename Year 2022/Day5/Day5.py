from get_file_from_server import get


if __name__ == "__main__":
    session_cookie = str(input("insert session cookie>"))
    g = get("https://adventofcode.com/2022/day/5/input", {"session": session_cookie})
    inp = g.get_file().splitlines()
    

    container = {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    }
    container2 = {}
    sec1 = []
    move = [1]
    for line in inp:
        if move != [1]:
            if "move" in line: 
                line = line.replace("move", "")
                comm = [None, None, None]
                comm[0] = int(line.split("from")[0])
                comm[1] = int(line.split("from")[1].split("to")[0])
                comm[2] = int(line.split("to")[1])
                move.append(comm)
        else:
            if "1" in line:
                move = []
            else:
                sec1.append(line)

    coll = 0
    for entry in sec1:
        entry = entry.replace("    ", "|")
        entry = entry.replace("[", "")
        entry = entry.replace("]", "")
        entry = entry.replace(" ", "")
        row = 0
        for elem in entry:
            if elem != "|":
                container[row].append(elem)
            else:
                pass
            row += 1
        coll += 1
        
    container2 = container.copy()

    for movement in move:
        count = movement[0]
        fro = movement[1]-1
        dest = movement[2]-1
        cargo_fro = container[fro][0:count].copy()
        cargo_to = container[dest].copy()
        cargo_fro2 = container2[fro][0:count].copy()
        cargo_to2 = container2[dest].copy()

        for cargo in cargo_fro:
            cargo_to.insert(0,cargo)
        container[dest] = cargo_to.copy()

        cargo_fro2.reverse()
        container2[dest].reverse()
        for cargo in cargo_fro2:
            container2[dest].append(cargo)
        cargo_fro2.reverse()
        container2[dest].reverse()

        container[fro] = container[fro][count:].copy()
        container2[fro] = container2[fro][count:].copy()

    res = ""
    res2 = ""
    for elem in container:
        print(elem, container[elem])
        if container[elem] != []:
            res += container[elem][0]

    print("Part 2")
    for elem in container2:
        print(elem, container2[elem])
        if container2[elem] != []:
            res2 += container2[elem][0]

    print("Part 1", res)
    print("Part 2", res2)
