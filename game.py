from responses import Responses 
from magic8 import Magic8
from menu import Menu, MenuOption
from console_colors import CColors as c
import time

class GameLoop:
    def __init__(self):
        self._done = False
        self._responses_object = None # Responses instance 
        self._magic8 = None # Magic8 instance 
        self._menu = Menu()
        self._keep_asking = True

    def start(self, user=None):
        # This function implements the entire game loop 
        # Displays the menu 
        # captures input 
        # Invokes the appropriate function for each menu option. 
        self._responses_object = Responses("input.txt")
        self._magic8 = Magic8(self._responses_object)
        self._menu.select(user)

        while not self._done:
            if self._menu.selection == MenuOption.A:
                self._responses_object.read()
            elif self._menu.selection == MenuOption.B:
                print(f"{c.BOLD} {c.FAIL}")
                while self._keep_asking:
                    question = input("What do you want to ask the Magic8 Ball? ")
                    self._magic8.shake()
                    question2 = input("Play again (Y/N)? ")
                    if question2 == "N" or question2 == "n":
                        print("Thank you for playing!")
                        self._keep_asking = False
                print(f"{c.ENDC}")
            elif self._menu.selection == MenuOption.C:
                print(f"{c.BOLD} {c.CYAN}")
                self._responses_object.display()
                print(f"{c.ENDC}")
            elif self._menu.selection == MenuOption.D:
                print(f"{c.BOLD} {c.FAIL}")
                self._responses_object.write()
                print(f"{c.ENDC}")
            elif self._menu.selection == MenuOption.E:
                self._responses_object.add()

            elif self._menu.selection == MenuOption.F:
                print("Thank you for playing, Goodbye!")
                self._done = True
                break
            self._menu.select(user)
        print(f"{c.ENDC}")

    def _end(self):
        self._done = True