import readline
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

# Menu Action Codes
TRANSLATE_PLAIN_TEXT_TO_MORSE_CODE = 0
TRANSLATE_MORSE_CODE_TO_PLAIN_TEXT = 1
SHOW_HISTORY = 2

def show_sub_options(): 
    terminal_menu = TerminalMenu(["Main menu", "Exit"])
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 1:
        print("\033[1mThanks for using morsepro\033[0m 👋")
        quit()

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

def translator(char, type):
    if type == 0:
        return dataset.get(char)
    else:
        return inv_dataset.get(char)

print("""                                                
                                                
  _ __ ___   ___  _ __ ___  ___ _ __  _ __ ___  
 | '_ ` _ \ / _ \| '__/ __|/ _ \ '_ \| '__/ _ \ 
 | | | | | | (_) | |  \__ \  __/ |_) | | | (_) |
 |_| |_| |_|\___/|_|  |___/\___| .__/|_|  \___/ 
                               | |              
                               |_|              """)
                               
print("\033[96m\033[1mWelcome to morsepro v0.1beta\033[0m")
print("\033[96mCreated by Yiğithan Yücedağ\033[0m\n")

while True:
    terminal_menu = TerminalMenu(["Plain text to morse code", "Morse code to plain text", "Show History", "Exit"])
    selected_action = terminal_menu.show()

    if selected_action == TRANSLATE_PLAIN_TEXT_TO_MORSE_CODE:
        print("Please type a plain text")
        text = str(input("> "))
        char_list = LinkedList()

        last_node = char_list.add_first(Node(text[0].lower()))
        for i in text[1:]:
            node = Node(i.lower())
            last_node.next = node
            last_node = node

        output = str()
        for node in char_list:
            output += f"{translator(node.data, selected_action)} "
        
        print(f"Morse code: {output}\n")
        
        show_sub_options()
    elif selected_action == TRANSLATE_MORSE_CODE_TO_PLAIN_TEXT:
        print("Please type a morse code")
        code = str(input("> "))
        code_list = LinkedList()
        splitted = code.split(" ")
        last_node = code_list.add_first(Node(splitted[0]))
        for i in splitted[1:]:
            node = Node(i)
            last_node.next = node
            last_node = node

        output = str()
        for node in code_list:
            output += f"{translator(node.data, selected_action)}"

        print(f"Plain text: {output}\n")
        
        show_sub_options()
    elif selected_action == SHOW_HISTORY:
        print("Show history")
    else:
        print("\033[1mThanks for using morsepro\033[0m 👋")
        quit()