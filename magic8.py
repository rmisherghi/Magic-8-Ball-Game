from responses import Responses
import random


class Magic8:

    def __init__(self, responses: Responses):
        self._responses = responses
        

    def shake(self): 
        # This function returns a random response from a list of magic8 responses
        # Use random module to generate a randum index between 0 and length or responses 
        if len(self._responses.responses) == 0:
            print("Response is empty, please load in a file with Menu Option A")
            return
        index = random.randint(0, len(self._responses.responses) - 1)
        response = list(self._responses.responses.keys())[index]
        category = list(self._responses.responses.values())[index]
        print(response, category)