'''
Implementation of a binary search tree vs a red black tree

'''

import random

#these classes create BST and RB Trees
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        self.color = False
        
class RBNode:
    def __init__(self, value=None):
        self.data= value
        self.color = (value is not None)
        if value is not None:
            self.left = RBNode()
            self.right = RBNode()
        else:
            self.left = None
            self.right = None
class RBTree:
    def __init__(self, value):
        self.root = RBNode(value)
        self.root.color = False
#################################################        
def BST_Insert(tree, node): #inserts a BST node in the usual way
    if tree is None:
        tree = node
    else:
        if tree.data > node.data:
            if tree.left == None:
                tree.left = node
            else:
                BST_Insert(tree.left, node)
        else:
            if tree.right == None:
                tree.right = node
            else:
                BST_Insert(tree.right, node)
                
def RB_Insert(tree, node):
    if tree == None:
        return RBTree(node)
    else:
        tree.root = RecRB_Insert(tree.root, node)
        tree.root.color = False
        return tree
    
def RecRB_Insert(current, node):
    if current.left == None and current.right == None: #current node is a leaf
        return RBNode(node)
    elif current.data < node:
        current.right = RecRB_Insert(current.right, node)
        if current.color == True:
            return current
        elif current.right.color == True: # current's right child is Red
            if current.right.right.color == True: # current's right grandchild is Red, R-R: Case 1
                return fixTree(current, node, 1)
            elif current.right.left.color == True: # current's left grandchild is Red, R-L, Case 2
                return fixTree(current, node, 2)    
            else:
                return current # no rebalance required
        else:
            return current # current's right child is black, no action needed
    elif current.data > node:
        current.left = RecRB_Insert(current.left, node)
        if current.color == True:
            return current
        elif current.left.color == True:
            if current.left.right.color == True:
                return fixTree(current, node, 3) # current's right grandchild is Red, L-R, Case 3
            elif current.left.left.color == True:
                return fixTree(current, node, 4) # left grand child is red, L-L Case 4
            else:
                return current
        else:
            return current

def fixTree(current, node, case):
    if case == 1: # current's right branch, current's right child is red and current's right grandchild is red
        child = current.right
        sibling = current.left
        if sibling.color == True: #simple recoloring needed
            child.color = False
            sibling.color = False
            current.color = True
            return current
        else:
            grandchild = child.right # RR case
            current.right = child.left
            child.left = current
            child.color = False
            current.color = True
            return child   
    elif case == 2: # current's right branch, current's right child is red and current's left grandchild is red
        child = current.right
        sibling = current.left
        if sibling.color == True: #simple recoloring needed
            child.color = False
            sibling.color = False
            current.color = True
            return current
        else: # RL case
            grandchild = child.left 
            child.left = grandchild.right
            current.right = grandchild.left
            grandchild.right = child
            grandchild.left = current
            grandchild.color = False
            current.color = True
            return grandchild
        
    elif case == 3: # current's left branch, current's left child is red, current's right grandchild is red
        child = current.left
        sibling = current.right
        if sibling.color == True:
            child.color = False
            sibling.color = False
            current.color = True
            return current
        
        else: # sibling is black, need to double rotate, since this is the LR case
            grandchild = child.right
            child.right = grandchild.left
            current.left = grandchild.right
            grandchild.left = child
            grandchild.right = current
            grandchild.color = False
            current.color = True
            return grandchild
        
    elif case == 4: # current's left branch, current's left child is red, current's left grandchild is red
        child = current.left
        sibling = current.right
        if sibling.color == True:
            child.color = False
            sibling.color = False
            current.color = True
            return current
        
        else: #single rotation case, since this is the LL case
            grandchild = child.left
            current.left = child.right
            child.right = current
            child.color = False
            current.color = True
            return child
        
def search(tree, value): #BST search
    if tree != None:
        if tree.data == value:
            print tree.data
        else:
            if tree.data > value:
                print tree.data
                search(tree.left, value)
            else:
                print tree.data
                search(tree.right, value)
    else:
        print "search value not in tree"
        return

def RBSearch(tree, value): #RB Search: Call RBSearch(tree.root, value)
    if tree != None:
        if tree.data == value:
            if tree.color == True:
                print tree.data, "Red"
            else:
                print tree.data, "Black"
        else:
            if tree.data > value:
                if tree.color == True:
                    print tree.data, "Red"
                else:
                    print tree.data, "Black"
                RBSearch(tree.left, value)
            else:
                if tree.color == True:
                    print tree.data, "Red"
                else:
                    print tree.data, "Black"
                RBSearch(tree.right, value)
    else:
        print "search value not in tree"
        return
                
def RBTotalDepth(tree, depth=1): # makes sure leaves aren't included
    if tree is None:
        return 0
    elif tree.left is None:
        return 0
    elif tree.right is None:
        return 0
    return depth + RBTotalDepth(tree.left, depth+1) + RBTotalDepth(tree.right, depth+1)

def total_depth(tree, depth=1): # calculates total depth of a BST
    if tree is None:
        return 0
    return depth + total_depth(tree.left, depth+1) + total_depth(tree.right, depth+1)

def printTree(tree): #prints a tree: need printTree(tree.root) for RB, printTree(tree) for a BST
    if not tree:
        return
    if tree.data == None:
        return
    printTree(tree.left)
    print tree.data
    printTree(tree.right)

# Experiment
setSize = [20, 50, 100, 500, 2500]

for i in setSize:
    subset = []
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    for j in range(500):
        subset = []
        subset = random.sample(xrange(100000), i) # generates permutation
        
        tree1 = RB_Insert(None, subset[0]) 
        tree2 = Node(subset[0])
        index = 1
        while index != len(subset)-1:
            RB_Insert(tree1, subset[index])
            BST_Insert(tree2, Node(subset[index]))
            index +=1
        RBTotal = RBTotalDepth(tree1.root)
        BSTTotal = total_depth(tree2)
        ratio = float(BSTTotal)/float(RBTotal) # computes ratio
        
        if ratio >= 0.5 and ratio < 0.75:
            score1 +=1
        elif ratio >= 0.75 and ratio < 1.0:
            score2 += 1
        elif ratio >= 1.0 and ratio < 1.25:
            score3 += 1
        else: # score is greater or equal to 1.25
            score4 += 1
            
    print "For set size i =", i;
    print "The ratio was between 0.5 and 0.75", "{0:.2f}%".format((float(score1)/500.00)*100), "of the time";
    print "The ratio was between 0.75 and 1.0", "{0:.2f}%".format((float(score2)/500.00)*100), "of the time";
    print "The ratio was between 1.0 and 1.25", "{0:.2f}%".format((float(score3)/500.00)*100), "of the time";
    print "The ratio was greater or equal to 1.25", "{0:.2f}%".format((float(score4)/500.00)*100), "of the time";
    print "\n"
    
