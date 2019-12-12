'''
This file implents a tenery tree class. 

allCombination method gives all the possible combinations given
a string made up by integers and transform each of integers into 
possible alphabets regarding the keyboard on cell phone.

treePath gives all the path from root to leaves.

'''
class teneryTree:

    def __init__(self,headNode):
        self.value = headNode
        self.left = None
        self.middle = None
        self.right = None
        self.extra = None

    def setLeft(self, node):
        self.left = teneryTree(node)
    def setMiddle(self, node):
        self.middle = teneryTree(node)
    def setRight(self, node):
        self.right = teneryTree(node)

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getMiddle(self):
        return self.middle
    
    def getValue(self):
        return self.value
    

class solution:
    def allCombination(self, tree, s:str):
        if len(s) == 0:
            return None
        
        asc = ord(s[0])
        tree.setLeft( asc + 47 + (asc-50)*2 )
        tree.setMiddle( asc + 48 + (asc-50)*2  )
        tree.setRight( asc + 49 + (asc-50)*2 )

        self.allCombination(tree.getLeft(), s[1:])
        self.allCombination(tree.getMiddle(), s[1:])
        self.allCombination(tree.getRight(), s[1:])

        return treePath(tree, '', [])



def treePath(tree:teneryTree, path, result):
    '''
    Give all the paths from root to leaves by using recursion.

    Return a lsit.
    '''
    if not tree.getLeft()t:
        ## This is leaf node
        ## Add the path to the result list.
        result.append(path + '->'+chr(tree.getValue()))

    if tree.getLeft():
        ## This still is a parent node.
        treePath(tree.getLeft(), path + '->' + chr(tree.getValue()), result)
        treePath(tree.getMiddle(), path + '->' + chr(tree.getValue()), result)
        treePath(tree.getRight(), path +'->' + chr(tree.getValue()), result)
    return result

t2 = teneryTree(49)
s = solution()
s.allCombination(t2, '23')

