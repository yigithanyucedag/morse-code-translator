from simple_term_menu import TerminalMenu

dataset = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}

inv_dataset = {v: k for k, v in dataset.items()}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, node):
        node.next = self.head
        self.head = node
        return node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

def translator(char, s):
    if s == 0:
        return dataset.get(char)
    else:
        return inv_dataset.get(char)

run = True
print("""                                                
                                                
  _ __ ___   ___  _ __ ___  ___ _ __  _ __ ___  
 | '_ ` _ \ / _ \| '__/ __|/ _ \ '_ \| '__/ _ \ 
 | | | | | | (_) | |  \__ \  __/ |_) | | | (_) |
 |_| |_| |_|\___/|_|  |___/\___| .__/|_|  \___/ 
                               | |              
                               |_|              """)
                               
print("\033[96m\033[1mWelcome to morsepro v0.1beta\033[0m")
print("\033[96mCreated by Yiğithan Yücedağ\033[0m\n")

while run:
    terminal_menu = TerminalMenu(["Plain text to morse code", "Morse code to plain text"])
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        print("Please type a plain text")
    else:
        print("Please type a morse code")

    text = str(input("> "))

    llist = LinkedList()

    if menu_entry_index == 1:
        splitted = text.split(" ")
        last_node = llist.add_first(Node(splitted[0])) # initially = head node
        for i in splitted[1:]:
            node = Node(i)
            last_node.next = node
            last_node = node
    else:
        last_node = llist.add_first(Node(text[0].lower())) # initially = head node
        for i in text[1:]: # exclude first char
            node = Node(i.lower())
            last_node.next = node
            last_node = node

    output = str()
    for node in llist:
        output += f"{translator(node.data, menu_entry_index)}{' ' if menu_entry_index == 0 else ''}"

    llist = LinkedList()

    print(f"Morse code: {output}\n") if menu_entry_index == 0 else print(f"Plain text: {output}\n")

    terminal_menu = TerminalMenu(["Start over", "Exit"])
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 1:
        run = False