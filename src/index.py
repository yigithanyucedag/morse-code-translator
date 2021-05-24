import readline
import pyperclip
from simple_term_menu import TerminalMenu
from datetime import datetime

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

# Menu Action Codes
TRANSLATE_PLAIN_TEXT_TO_MORSE_CODE = 0
TRANSLATE_MORSE_CODE_TO_PLAIN_TEXT = 1
SHOW_HISTORY = 2

def terminate():
    print("\033[1mThanks for using morsepro\033[0m 👋")
    quit()

def show_sub_options(text): 
    options = ["Copy to clipboard", "Main menu", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        pyperclip.copy(text)
        show_sub_options(text)
    elif menu_entry_index == 2:
        terminate()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

class Stack:
   def __init__(self):
      self.head = Node("head")
      self.size = 0
 
   def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.data) + "\n"
         cur = cur.next
      return out[:-3]  
    
   def isEmpty(self):
      return self.size == 0
 
   def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      self.size += 1

print("""                                                
                                                
  _ __ ___   ___  _ __ ___  ___ _ __  _ __ ___  
 | '_ ` _ \ / _ \| '__/ __|/ _ \ '_ \| '__/ _ \ 
 | | | | | | (_) | |  \__ \  __/ |_) | | | (_) |
 |_| |_| |_|\___/|_|  |___/\___| .__/|_|  \___/ 
                               | |              
                               |_|              """)
                               
print("\033[96m\033[1mWelcome to morsepro v0.1-beta\033[0m")
print("\033[96mCreated by github.com/yigithanyucedag\033[0m\n")

stack = Stack()

while True:
    terminal_menu = TerminalMenu(["Plain text to morse code", "Morse code to plain text", "Show History", "Exit"])
    selected_action = terminal_menu.show()

    if selected_action == TRANSLATE_PLAIN_TEXT_TO_MORSE_CODE:
        print("\033[1mPlease type a plain text\033[0m")
        text = str(input("> "))
        char_list = LinkedList()

        last_node = char_list.add_first(Node(text[0].lower()))
        for i in text[1:]:
            node = Node(i.lower())
            last_node.next = node
            last_node = node

        output = []
        for node in char_list:
            output.append(dataset.get(node.data))
        
        output = " ".join(output)
        print(f"Morse code: {output}\n")
        stack.push(f"(Plain text to morse code) From: {text} To: {output} Time: {datetime.now()}")
        show_sub_options(output)
    elif selected_action == TRANSLATE_MORSE_CODE_TO_PLAIN_TEXT:
        print("\033[1mPlease type a morse code\033[0m")
        code = str(input("> "))
        code_list = LinkedList()
        splitted = code.split(" ")
        last_node = code_list.add_first(Node(splitted[0]))
        for i in splitted[1:]:
            node = Node(i)
            last_node.next = node
            last_node = node

        output = []
        for node in code_list:
            output.append(list(dataset.keys())[list(dataset.values()).index(node.data)])

        output = "".join(output)
        print(f"Plain text: {output}\n")
        stack.push(f"(Morse code to plain text) From: {code} To: {output} Time: {datetime.now()}")
        show_sub_options(output)
    elif selected_action == SHOW_HISTORY:
        if stack.isEmpty():
            print("History is empty!\n")
        else:
            print("\033[1mHistory:\033[0m 📖")
            print(f"{stack}\n")
        options = ["Main menu", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 1:
            terminate()
    else:
        terminate()