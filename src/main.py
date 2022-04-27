import os
import sys
from pprint import pprint
from art import text2art

sys.path.append(os.path.realpath("."))
import inquirer

title = text2art("BASKINATOR", font='big')


def display(question: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{title}\n\n")
    questions = [
        inquirer.List(
            "answer",
            message=question,
            choices=["Yes", "No", "I don't know"],
        ),
    ]

    answers = inquirer.prompt(questions)
    return answers["answer"]

display("Do you like school?")