"""
Interview Question: How do you perform Level Order Traversal (BFS) on a Binary Tree in Python?

Interview Explanation:
"I use a Queue (implemented via `collections.deque`).
Starting with the root node, I process nodes level by level. For each level, I record the values of all nodes in that level
and enqueue their left and right children. This returns a list of lists representing tree levels in O(n) time."
"""

from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Level Order Traversal:", level_order_traversal(root))
