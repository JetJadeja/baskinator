import numpy
import re
import os
from collections import deque

def main():
    codec = Codec()
    tokens = codec.txtToTokens("testPost.txt")
    print("Main Ran");
    print(tokens)
    print(codec.deserialize(tokens))
    codec.updateTxt("testPost.txt", tokens)

class TreeNode:
  def __init__(self, value, left, right):
    self.value = value # data
    self.left = left  # references to other nodes
    self.right = right

  def setLeft(self, node): # creates parent-child relationship
    self.left = node
    
  def setRight(self, node): # creates parent-child relationship
    self.right = node


class Codec:
 def updateNodesToAdd(self, player: str, question: str):
   file = open(os.getcwd() + "/nodestoadd.txt", "a")
   file.append("After question: " + question + " new player: " + player + "\n");
   file.close()
 def updateTxt(self, fileName:str, data):
   file = open(os.getcwd() + "/" + fileName, "w")
   for i in data:
     file.write(i);
   file.close()
   return
 def txtToTokens(self, fileName: str):
         file = open(os.getcwd() + "/" + fileName, "r")
         out = []
         data = file.read().splitlines()
         for line in data:
           for c in line.split('|'):
             if not c.isspace():
               out.append(c)
         file.close()
         return out;
 def deserialize(self, data):
   stk = []
   for i in data:
     if i.startswith("?"):
       stk.append(TreeNode(i, stk.pop(), stk.pop()))
     else:
       stk.append(TreeNode(i, None, None))
   return stk.pop()

 def serialize(self, root):
     res = []
     if root:
         res = self.serialize(root.left)
         res = res + self.serialize(root.right)
         res.append("|" + root.data)
     return res
