import requests

class get:
    def __init__(self, path:str, cookie):
        self.path = path
        self.req = None
        self.cookie = cookie
    
    def get_file(self):
        self.req = requests.get(self.path, cookies=self.cookie)
        return self.req.text



if __name__ == "__main__":
    g = get("https://adventofcode.com/2022/day/1/input", {"session": "<your session cookie>"})
    print(g.get_file())
