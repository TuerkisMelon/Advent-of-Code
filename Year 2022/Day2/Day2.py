from get_file_from_server import get


if __name__ == "__main__":
    session_cookie = str(input("insert session cookie>"))
    g = get("https://adventofcode.com/2022/day/2/input", {"session": session_cookie})
    inp = g.get_file().splitlines()

    calc_points_win = 0
    calc_points_lose = 0
    for game in range(len(inp)):
        enemy = inp[game].split(" ")[0]
        player = inp[game].split(" ")[1]

        if enemy == "A":
            if player == "X":
                calc_points_win += 1 + 3 # Draw
                calc_points_lose += 3 + 0 # Lose Part 2
            elif player == "Y":
                calc_points_win += 2 + 6 # Win
                calc_points_lose += 1 + 3 # Draw Part 2
            elif player == "Z":
                calc_points_win += 3 + 0 # Lose
                calc_points_lose += 2 + 6 # Win Part 2
            else:
                print(f"ERROR char undefined {enemy} {player}")
        elif enemy == "B":
            if player == "X":
                calc_points_win += 1 + 0 # Lose
                calc_points_lose += 1 + 0 # Lose Part 2
            elif player == "Y":
                calc_points_win += 2 + 3 # Draw
                calc_points_lose += 2 + 3 # Draw Part 2
            elif player == "Z":
                calc_points_win += 3 + 6 # Win
                calc_points_lose += 3 + 6 # Win Part 2
            else:
                print(f"ERROR char undefined {enemy} {player}")
        elif enemy == "C":
            if player == "X":
                calc_points_win += 1 + 6 # Win
                calc_points_lose += 2 + 0 # Lose Part 2
            elif player == "Y":
                calc_points_win += 2 + 0 # Lose
                calc_points_lose += 3 + 3 # Draw Part 2
            elif player == "Z":
                calc_points_win += 3 + 3 # Draw
                calc_points_lose += 1 + 6 # Win Part 2
            else:
                print(f"ERROR char undefined {enemy} {player}")
        else:
            print(f"ERROR char undefined {enemy} {player}")


    print(f"Points when won: {calc_points_win}")
    print(f"Points when lost: {calc_points_lose}")
