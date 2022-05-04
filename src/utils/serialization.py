from tree import DecisionTree
import os

file = open(f"{os.getcwd()}/src/data/csv_data.txt", "r")
nodes = file.read().split("\n")

question_to_nodes = {}

def write_tree(root):
    csv_data = "\n".join(create_csv_array(root, None, None, is_root=True))

    file.write(csv_data)
    file.close()

def create_csv_array(root, parent, yes, is_root=False):
    serialized_nodes = []

    if is_root: 
        serialized_nodes.append(f'"{root.data}",-1,""')

    else:
        serialized_nodes.append(f'"{root.data}","{parent}","{"Yes" if yes else "No"}"')

    if not root.data.endswith("?"):
        return serialized_nodes

    serialized_nodes = [*serialized_nodes, *create_csv_array(root.yes, root.data, True)]
    serialized_nodes = [*serialized_nodes, *create_csv_array(root.no, root.data, False)]

    return serialized_nodes

def get_tree():
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