import pickle
from setup import get_tree, preorder
import os

filename = f"{os.getcwd()}/src/data/info.txt"
tree = get_tree()

def save_model(model):
    outfile = open(filename,'wb')
    pickle.dump(model, outfile)
    outfile.close()

def retrieve_model():
    in_file = open(filename,'rb')
    model = pickle.load(in_file)
    in_file.close()

    return model

save_model(tree)