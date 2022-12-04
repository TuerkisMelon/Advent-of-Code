from get_file_from_server import get


if __name__ == "__main__":
    session_cookie = str(input("insert session cookie>"))
    g = get("https://adventofcode.com/2022/day/3/input", {"session": session_cookie})
    inp = g.get_file().splitlines()

    score_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5], ["f", 6], ["g", 7], ["h", 8], ["i", 9], ["j", 10], ["k", 11], ["l", 12], ["m", 13], ["n", 14], ["o", 15], ["p", 16], ["q", 17], ["r", 18], ["s", 19], ["t", 20], ["u", 21], ["v", 22], ["w", 23], ["x", 24], ["y", 25], ["z", 26], ["A", 27], ["B", 28], ["C", 29], ["D", 30], ["E", 31], ["F", 32], ["G", 33], ["H", 34], ["I", 35], ["J", 36], ["K", 37], ["L", 38], ["M", 39], ["N", 40], ["O", 41], ["P", 42], ["Q", 43], ["R", 44], ["S", 45], ["T", 46], ["U", 47], ["V", 48], ["W", 49], ["X", 50], ["Y", 51], ["Z", 52]]
    newinp = []
    for line in inp:
        temp = []
        length = int(len(line) / 2)
        temp.append(line[0:length])
        temp.append(line[length:len(line)])
        newinp.append(temp)

    priority_score = 0
    for elem in newinp:
        for char in score_list:
            if char[0] in elem[0] and char[0] in elem[1]:
                priority_score += char[1]

    print("Part 1:", priority_score)

    priority_score = 0
    for x in range(0, len(newinp), 3):
        for char in score_list:
            if char[0] in inp[x]:
                if char[0] in inp[x + 1]:
                    if char[0] in inp[x + 2]:
                        priority_score += char[1]
    
    print("Part 2:", priority_score)
