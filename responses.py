import console_colors as C

class Responses:

    def __init__(self, input_file):
        self._input_file = input_file
        self._responses = {}
        

    @property
    def file(self): 
        return self._input_file

    @property
    def responses(self):
        return self._responses

    def read(self):
        # Read the content of the input file and populate the responses
        # dictionary variable instance above. Use the responses as keys and
        # categories as values
        with open(self._input_file) as file:
            lines = file.readlines()
            for line in lines:
                (key, val) = line.strip().split(":")
                self._responses[key] = val



    def display(self):
        # Sort magic8 responses in alphabetical order and display then on the screen. 
        # Call this function in your main loop for menu option b
        if len(self._responses) == 0:
            print(C.CColors.WARNING,"Response is empty, please load in a file with Menu Option A",C.CColors.ENDC)
            return

        self._sort()
        for key, value in self._responses.items():
            print(key, value)
      
    def _sort(self):
        # Private function to sort a list of items in ascending order 
        # use this function to print responses by in alphabetical order 
        responses = list(self._responses.items())
        n = len(responses)
        for bottom in range(n-1):
            mp = bottom
            for i in range(bottom + 1, n):
                if responses[i][0] < responses[mp][0]:
                    mp = i
            responses[bottom], responses[mp] = responses[mp], responses[bottom]
        self._responses = dict((k[0], k[1])for k in responses)


    def write(self):
        output = input("Enter a file name: ")
        with open(output,"w+") as file:
            for key, value in self._responses.items():
                file.write(f"{key}: {value} \n")
        # this function should write the respones to user supplied output file
        # prompt the user to enter file name then dump the content of responses
        # to the file
        pass

    def add(self):
        # Extra credit 
        # Update the responses container. i.e. prompt the user to enter a new response 
        # and its category. Add the response to the dictionary
        response, category = input("Enter a response and category seperated by a comma: ").split(",")
        self._responses[response] = category




