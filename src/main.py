from pprint import pprint
from art import text2art
import inquirer

import os
import sys

from utils.serialization import retrieve_model, save_model
from utils.tree import DecisionTree
from utils.setup import get_tree, preorder

import random

sys.path.append(os.path.realpath("."))
title = text2art("BASKINATOR", font='big')

root = retrieve_model()

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

def reset_tree():
    tree = get_tree()
    save_model(tree)

reset_tree()

def display(root: str):
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
        display(node)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text2art(f"Your  player  is  {node.data}", font='big'))

if __name__ == "__main__":
    display(root)