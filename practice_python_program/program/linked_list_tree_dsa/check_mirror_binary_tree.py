"""
Interview Question: How do you check if a Binary Tree is symmetric (a mirror of itself)?

Interview Explanation:
"A tree is symmetric if its left subtree is a mirror reflection of its right subtree.
I write a recursive helper `is_mirror(t1, t2)`:
- Base cases: both None -> True; one None -> False; values differ -> False.
- Recursive step: `is_mirror(t1.left, t2.right)` and `is_mirror(t1.right, t2.left)`."
"""

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode | None) -> bool:
    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    return is_mirror(root, root)

if __name__ == "__main__":
    root = TreeNode(1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3))
    )
    print("Is Binary Tree Symmetric?", is_symmetric(root))
