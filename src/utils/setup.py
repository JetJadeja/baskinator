from utils.tree import DecisionTree
import os

# TODO: This file should be moved to a parameter of the function get_tree()
file = open(f"{os.getcwd()}/src/data/csv_data.txt", "r")
nodes = file.read().split("\n")

question_to_nodes = {}

def get_tree():
    # TODO: Note on opening files in python: it is considered good practice to use
    #  a with context block: https://peps.python.org/pep-0343/ 
    #  for example: 
    #  with open(fname) as f: 
    #    # what to do with f... 
    root = None

    for node in nodes:
        node = node.replace('"', '')
        info = node.split(",")

        if(len(info) == 1): continue

        # Is root node
        if info[1] == "-1":
            root = DecisionTree(info[0])
            question_to_nodes[info[0]] = root

        else:
            parent = question_to_nodes[info[1]]
            if info[2] == "Yes":
                parent.insert_yes(info[0])
                question_to_nodes[info[0]] = parent.yes

            else:
                parent.insert_no(info[0])
                question_to_nodes[info[0]] = parent.no

    return root

def preorder(root):
    #if root is None return
    if root==None:
        return
    #traverse root
    print(root.data)
    #traverse left subtree
    preorder(root.yes)
    #traverse right subtree
    preorder(root.no) 

