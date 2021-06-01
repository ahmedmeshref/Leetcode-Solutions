def PreorderTraversal(strArr):
    preorderArr = []

    def preOrderCalculator(node_ind, num_missing_leafs):
        # base case
        if node_ind >= len(strArr) or strArr[node_ind] == "#":
            return 2
        preorderArr.append(strArr[node_ind])
        left_child = (node_ind * 2) + 1 - num_missing_leafs
        val = preOrderCalculator(left_child, num_missing_leafs)
        num_missing_leafs += 2 if val else 0
        right_child = left_child + 1
        preOrderCalculator(right_child, num_missing_leafs)

    preOrderCalculator(0, 0)
    return ' '.join(preorderArr)


# keep this function call here
print(PreorderTraversal(["5", "2", "6", "1", "9", "10", "#", "#", "#", "#", "#", "4", "#"]))
