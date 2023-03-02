# python3

import sys
import threading

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
def compute_height(node):
    # Write this function
    max_height = 0
    for child in node.children:
        max_height = max(max_height, compute_height(child))
    return max_height + 1

def create_tree(n, mode, file=None):
    parent_index=[]
    nodes={}
    if "I" in mode:
        values = input().split()
    else:
        values = file.readline().split()
    for i in range(n):
        parent_index.append(int(values[i]))
        nodes[i] = Node(i)
          
    for i in range(n):
        if parent_index[i] != -1:
            nodes[parent_index[i]].add_child(nodes[i])
        
        else:
            root = nodes[i]

    return root

def main():
    print("Input Mode: ")
    mode = input()
    if "I" in mode:
        print("Input: ")
        n = int(input())
        root = create_tree(n, mode)
        height = compute_height(root)
        print(height)

    else:
        print("Input File: ")
        filename= input()
        if "a" in filename:
            print("Filename containing a is not allowed")
            return
        folder = './test/'
        file = open(folder + filename, 'r')
        n = int(file.readline())
        root = create_tree(n, mode, file)
        height = compute_height(root)
        print(height)
        
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
