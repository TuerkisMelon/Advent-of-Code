from get_file_from_server import get


if __name__ == "__main__":
    session_cookie = str(input("insert session cookie>"))
    g = get("https://adventofcode.com/2022/day/4/input", {"session": session_cookie})
    inp = g.get_file().splitlines()

    counta = 0
    countb = 0
    for line in inp:
        groupa = line.split(",")[0].split("-")
        groupb = line.split(",")[1].split("-")

        groupa[0] = int(groupa[0])
        groupa[1] = int(groupa[1])
        groupb[0] = int(groupb[0])
        groupb[1] = int(groupb[1])

        if groupa[0] >= groupb[0] and groupb[1] >= groupa[1]:
            counta += 1
        elif groupb[0] >= groupa[0] and groupa[1] >= groupb[1]:
            counta += 1
        
        if groupa[0] <= groupb[0] and groupa[1] >= groupb[0]:
            countb += 1
        elif groupa[0] >= groupb[0] and groupa[0] <= groupb[1]:
            countb += 1


    #969 < e < 913
    print("Part 1", counta)
    print("Part 2", countb)
