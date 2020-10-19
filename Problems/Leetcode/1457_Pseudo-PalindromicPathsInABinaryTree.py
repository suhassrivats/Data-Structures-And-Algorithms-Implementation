# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    For each root to node path which is computed using DFS , check palindrome if
    the length of string(path from root to node) is"
    case 1 : ODD
    One charactrer in string can have odd number of occurences , remaining all
    should have even ocurences
    ex : 12312 - only 3 has odd number of occurences
    case2 : EVEN
    All characters in string should have even number of occurences:
    ex: 1212 , 1111 , 2233 are palindromes
    1112 , here 1 has odd number of occurences so not a palindrome
    """

    def __init__(self):
        self.count = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.countPath(root, "")
        return self.count

    def countPath(self, node, s):
        if not node:
            return None
        if not node.left and not node.right:
            s += str(node.val)
            if self.isPalindrome(s):
                self.count += 1
        if node.left:
            self.countPath(node.left, s+str(node.val))
        if node.right:
            self.countPath(node.right, s+str(node.val))

    def isPalindrome(self, s):
        n = len(s)
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        # flag is True when odd, False when even
        flag = n % 2 != 0

        for c in d:
            # One charactrer in string can have odd number of occurences,
            # remaining all should have even ocurences
            # ex : 12312 - only 3 has odd number of occurences
            if d[c] % 2 != 0:
                if not flag:
                    return False
                flag = False
        return True
