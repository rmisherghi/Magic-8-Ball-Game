class CColors:
    # Helper class to print colored outputs on console 
    # You can get up 10 extra credit points for using this class
    # in your project. Take a look at example usage below 

    MENU = '\033[96m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    
    # example usage 

    # Line 
    print(CColors.BOLD, "CSCI 1410", CColors.ENDC)
    print(CColors.MENU, "CSCI 1410", CColors.ENDC)
    print(CColors.UNDERLINE, "CSCI 1410", CColors.ENDC)

    # block 

    print(CColors.FAIL)
    print("CSCI 1410 ")
    print("Fundamentals of Computing using Python")
    print(CColors.ENDC)