from get_file_from_server import get


if __name__ == "__main__":
    session_cookie = str(input("insert session cookie>"))
    g = get("https://adventofcode.com/2022/day/1/input", {"session": session_cookie})
    inp = g.get_file().splitlines()

    cal_list = []
    elf_list = []
    elf = {
        "num": 0,
        "calories": 0
    }
    curr_elf = {
        "num": 0,
        "calories": 0
    }
    for i in range(len(inp)):
        if inp[i] == "":
            if curr_elf["calories"] > elf["calories"]:
                elf = curr_elf.copy()
                elf_list.append(elf)
            cal_list.append(curr_elf["calories"])
            curr_elf["num"] += 1
            curr_elf["calories"] = 0
        else:
            curr_elf["calories"] += int(inp[i])
    if curr_elf["calories"] != 0:
        if curr_elf["calories"] > elf["calories"]:
                elf = curr_elf.copy()
                elf_list.append(elf)
        cal_list.append(curr_elf["calories"])

    cal_list.sort()

    print(cal_list)
    print(elf_list)
    print("top elf")
    print(elf)
    print("total calories of the top three elves")
    print(f"{cal_list[len(cal_list) - 1]} + {cal_list[len(cal_list) - 2]} + {cal_list[len(cal_list) - 3]} = {int(cal_list[len(cal_list) - 1]) + int(cal_list[len(cal_list) - 2]) + int(cal_list[len(cal_list) - 3])}")
