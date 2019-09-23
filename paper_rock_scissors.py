from paper_rock_scissor_core import *


if __name__ == '__main__':
    print("Welcome to Paper Rock Scissor v.01")
    while(True):
        clear_screen()
        print("Do you want to:")
        print("1. You play with a robot?")
        print("2. Robot play with a robot?")
        print("3. Exit?")
        ans = input("")
        if ans in ["1", "2", "3"]:
            if ans == "1":
                play(TypeOfPlayer.REAL, TypeOfPlayer.ROBOT_1)
            if ans == "2":
                play(TypeOfPlayer.ROBOT_1, TypeOfPlayer.ROBOT_2)
            if ans == "3":
                exit()



    