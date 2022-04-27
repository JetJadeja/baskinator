from pprint import pprint
from art import text2art
import inquirer

import os
import sys

from utils.tree import DecisionTree
from utils.setup import get_tree, preorder

import random

sys.path.append(os.path.realpath("."))
title = text2art("BASKINATOR", font='big')

class DecisionTree:
    def __init__(self, data):
        self.yes = None
        self.no = None
        self.data = data

    def insert_yes(self, data):
        self.yes = DecisionTree(data)
        return self.yes

    def insert_no(self, data):
        self.no = DecisionTree(data)
        return self.no


tree = get_tree()

def play(root: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{title}\n\n")
    questions = [
        inquirer.List(
            "answer",
            message=root.data,
            choices=["Yes", "No", "I don't know"],
        ),
    ]

    answer = inquirer.prompt(questions)["answer"]
    
    if answer == "Yes": node = root.yes
    if answer == "No": node = root.no
    if answer == "I don't know": node = [root.yes, root.no][random.randint(0, 1)]

    root.yes if answer == "Yes" else root.no

    if node.data.endswith("?"):
        play(node)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text2art(f"Your  player  is  {node.data}", font='big'))
        
        questions = [
            inquirer.List(
                "answer",
                message="Was I right?",
                choices=["Yes", "No"],
            ),
        ]

        if inquirer.prompt(questions)["answer"] == "No":
            os.system('cls' if os.name == 'nt' else 'clear')
            new_name = input("Enter the name of your player: ")

            players_to_add = open(f"{os.getcwd()}/src/data/players-to-add.txt", 'a')
            players_to_add.write(f"{new_name}\n")
            players_to_add.close()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print(text2art("WELCOME  TO  BASKINATOR", font='big'))
    print("""
_____________________________$$$$
____________________________$$$$$$
____________________________$$$$$$
_____________________________$$$$
_____________________________$$
_____________________________$$
____________________________$$$
____________________________$$$
_____________________$$$$___$$$
_____________________$$$$$_$$$
_____________________$$$$$$$$
______________________$$$$$$
____________________$$$$$$$$
___________________$$$$$$$$$$
__________________$$$$$$$$$$$
_________________$$$__$$$$$$$
________________$$$____$$$$$$
_______________$$_____$$$$$$$
_____________$$$_____$$$$$$$$$
____________$$$_$___$$$$$$$$$$$
__________________$$$$$$$$$$$$$$$_
________________$$$$$$$$_$$$$$$$$$$
______________$$$$$$$________$$$$$$$$$
___________$$$$$$$_______________$$$$$$$
_________$$$$$$_____________________$$$$$$
_______$$$$$__________________________$$$$$
_____$$$$$______________________________$$$$$$_$$
$$$$$$$___________________________________$$$$$$$
_$$$$$______________________________________$$
    
    """)

    questions = [
        inquirer.List(
            "answer",
            message="Would you like to play?",
            choices=["Yes", "No", "Teach me"],
        ),
    ]

    decision = inquirer.prompt(questions)["answer"]

    if(decision == "Yes"):
        play(tree)

    if(decision == "No"):
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

    if(decision == "Teach me"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text2art("WELCOME  TO  BASKINATOR", font='big'))
        print("Baskinator is an Akinator-inspired game about Basketball players.")
        print("Before the game begins, think of a famous basketball player. Baskinator will ask you questions about your player in order to identify them.\n\n\n\n")

        questions = [
            inquirer.List(
                "answer",
                message="Ready?",
                choices=["Let's Do It", "No"],
            ),
        ]

        if inquirer.prompt(questions)["answer"] == "No":
            exit()

        play(tree)
