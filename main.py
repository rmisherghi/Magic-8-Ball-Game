from game import GameLoop


if __name__ == '__main__':
    print("\n")
    gamer = None
    while not gamer or len(gamer) == 0:
        gamer = str(input("Enter your name: "))
    # print(f"Hi {gamer}")
    game = GameLoop()
    game.start(gamer)
