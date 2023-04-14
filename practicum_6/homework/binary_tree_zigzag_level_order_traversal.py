from collections import deque
import yaml
from typing import Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order_traversal(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])
    is_reverse = False

    while queue:
        level = []
        size = len(queue)

        for i in range(size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if is_reverse:
            level.reverse()

        result.append(level)
        is_reverse = not is_reverse

    for el in result:
        while None in el:
            el.remove(None)

    return result

def build_tree(arr: list[Any]) -> list[TreeNode]:
    m = []
    for i in range(len(arr)):
        new_node = TreeNode()
        new_node.val = arr[i]
        m.append(new_node)
    for i in range(len(m)):
        if (2*i + 1) >= len(m):
            continue
        m[i].left = m[2*i + 1]
        m[i].right = m[2*i + 2]

    return m





if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "./binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = []
        if bt:
            zz_traversal = zigzag_level_order_traversal(bt[0])
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
