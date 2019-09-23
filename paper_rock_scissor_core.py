import random
import os
import sys

class Options:
    PAPER = 'PAPER'
    ROCK = 'ROCK'
    SCISSORS = 'SCISSORS'

class TypeOfPlayer:
    REAL = "REAL"
    REAL2 = "REAL2"
    ROBOT_1 = "ROBOT_1"
    ROBOT_2 = "ROBOT_2"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Logic:
    def get_winner(p1, p2):
        pair = (p1.decision, p2.decision)
        win = None
        for option in Logic.OPTIONS:
            if option['pair'] == pair:
                win = option['winner']
                msg = option['message']
                print(msg)
                print("Winner is...")
                break
        if win == p1.decision:
            p1.increase_score()
            return p1
        elif win == p2.decision:
            p2.increase_score()
            return p2
        else:
            return None

    OPTIONS = [ 
            {'pair': (Options.PAPER, Options.ROCK), 'winner': Options.PAPER, 'message':'Paper covers rock!'},
            {'pair': (Options.PAPER, Options.SCISSORS), 'winner': Options.SCISSORS, 'message':'This is a tie!'},
            {'pair': (Options.PAPER, Options.PAPER), 'winner': None,'message':'This is a tie!'},
            {'pair': (Options.ROCK, Options.PAPER), 'winner': Options.PAPER,'message':'This is a tie!'},
            {'pair': (Options.ROCK, Options.SCISSORS), 'winner': Options.ROCK,'message':'Rock smashes scissors!'},
            {'pair': (Options.ROCK, Options.ROCK), 'winner': None,'message':'This is a tie!'},
            {'pair': (Options.SCISSORS, Options.PAPER), 'winner': Options.SCISSORS,'message':'Scisors cut paper!'},
            {'pair': (Options.SCISSORS, Options.ROCK), 'winner': Options.ROCK,'message':'This is a tie!'},
            {'pair': (Options.SCISSORS, Options.SCISSORS), 'winner': None,'message':'This is a tie!'}
    ]

class BasePlayer:
    def __init__(self, type_of_player):
        self.type = type_of_player
        self.decision = None

    def __str__(self):
        return self.type + " PLAYER" 

    def make_decision(self):
        if self.type == TypeOfPlayer.REAL:
            while(True):
                print("Player 1: Choose [P]aper [R]ock [S]cissor [E]xit")
                print("--------------------------------------------")
                ans = input("").lower()
                if ans in ['p', 'r', 's', 'e']:
                    if ans == 'p':
                        self.decision = Options.PAPER
                        break
                    if ans == 'r':
                        self.decision = Options.ROCK
                        break
                    if ans == 's':
                        self.decision = Options.SCISSORS
                        break
                    if ans == 'e':
                        clear_screen()
                        exit()
        if self.type == TypeOfPlayer.REAL2:
            while(True):
                print("Player 2: Choose [P]aper [R]ock [S]cissor [E]xit")
                print("--------------------------------------------")
                ans = input("").lower()
                if ans in ['p', 'r', 's', 'e']:
                    if ans == 'p':
                        self.decision = Options.PAPER
                        break
                    if ans == 'r':
                        self.decision = Options.ROCK
                        break
                    if ans == 's':
                        self.decision = Options.SCISSORS
                        break
                    if ans == 'e':
                        clear_screen()
                        exit()
        else:
            self.decision = self._make_random_decision()[0]

    def _make_random_decision(self):
        return random.choices([Options.ROCK, Options.SCISSORS, Options.PAPER], k=1)


class Player(BasePlayer):
    def __init__(self, type_of_player):
        self.score = 0
        super().__init__(type_of_player)

    def increase_score(self):
        self.score += 1



def play(p1_type, p2_type):
    clear_screen()
    p1 = Player(p1_type) 
    p2 = Player(p2_type)
    while(True):
        print("")
        print("")
        s = f"{p1} score = {p1.score} {p2} score = {p2.score}\r\n"
        print(s)
        p1.make_decision()
        p2.make_decision()
        print(str(p1) + ' picked ', p1.decision)
        print(str(p2) + ' picked ', p2.decision)
        print("")
        print(Logic.get_winner(p1, p2))
        print("")
        ans = input("Play again? [ENTER], [E]xit or go to [M]enu\r\n").lower()
        if ans == 'e':
            exit()
        if ans == 'm':
            return True
        clear_screen()