from get_file_from_server import get

if __name__ == "__main__":
    session_cookie = str(input("insert session cookie>"))
    g = get("https://adventofcode.com/2022/day/1/input", {"session": session_cookie})
    inp = g.get_file()

