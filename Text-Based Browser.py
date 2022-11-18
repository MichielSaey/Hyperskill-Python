import os
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore
# write your code here


class Browser:

    def __init__(self, path):
        self.current_tab = ''
        self.history = deque()
        self.path = path
        self.all_tabs = dict()

    def add_tab(self, name):
        os.chdir(self.path)

        r = requests.get('https://' + name)
        if r:
            with open(name.split('.')[0], 'w', encoding='utf-8') as file:
                contents = self.get_contents(r.content)
                file.write(contents)

            self.history.append(self.current_tab)
            self.current_tab = name

            return contents
        else:
            return 'Site not found'

    def open_tab(self, name):
        os.chdir(self.path)
        print(name)
        with open(name.split('.')[0], 'r', encoding='utf-8') as file:
            contents = file.read()

        self.history.append(self.current_tab)
        self.current_tab = name

        return contents

    def step_back(self):
        if not len(self.history) == 0:
            self.current_tab = self.history.pop()
            print(self.open_tab(self.current_tab))

    def get_contents(self, contents):
        soup = BeautifulSoup(contents, 'html.parser')
        output = ""

        tags = soup.find_all(["p", "a", "ul", "ol", "li"])

        for i in tags:
            if i.name == "a":
                output += Fore.BLUE + i.text + '\n'
                print(Fore.BLUE + i.text + '\n')
            else:
                output += i.text + '\n'

        print(output)
        return soup.get_text()

def main():
    directory = sys.argv[1]
    path = os.path.join(os.getcwd(), directory)

    # print(directory)
    # print(path)

    os.makedirs(path, exist_ok=True)
    browser = Browser(path)

    while True:
        cmd = input()

        if cmd in browser.all_tabs:
            print(browser.open_tab(cmd))
        elif cmd == "exit":
            return
        elif cmd == "back":
            browser.step_back()
        elif "." not in cmd:
            print("Invalid URL")
            continue
        else:
            print(browser.add_tab(cmd))


if __name__ == "__main__":
    main()
