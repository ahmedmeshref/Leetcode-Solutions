import re


def TreeConstructor(strArr):
    tree = {}
    for link in strArr:
        nodes = re.findall(r"[0-9]+", link)
        intNodes = list(map(lambda x: int(x), nodes))
        if intNodes[0] not in tree:
            tree[intNodes[0]] = [None] * 3
        if intNodes[1] not in tree:
            tree[intNodes[1]] = [None] * 3

        # If parent has a previous child
        if intNodes[0] == intNodes[1]:
            return False
        elif intNodes[0] > intNodes[1]:
            # If child > parent, then a right child
            if tree[intNodes[1]][2]:
                return False
            tree[intNodes[1]][2] = intNodes[0]
        else:
            if tree[intNodes[1]][1]:
                return False
            tree[intNodes[1]][1] = intNodes[0]

        # If the child got a parent already return false
        if tree[intNodes[0]][0]:
            return False
        tree[intNodes[0]][0] = intNodes[1]

    root = False
    for val in tree.values():
        if not val[0]:
            if not root:
                root = True
            else:
                return False
    return True


# keep this function call here
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))

"""
check if the following can form a BST knowing that second val is parent of the first 
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true
"""
