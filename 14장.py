#트리는 재귀로 정의된 자기참조 자료구조, 항상 root에서부터 시작되며 단방향이다.
#그래프와 차이점으로 트리는 순환구조를 갖지 않는 그래프이며 하나의 부모 노드를 갖는다는 점이 있다.
#따라서 루트 또한 하나이다. 이진트리란 모든 노드의 차수가 2이하인 형태

#42번
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 예외처리
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(queue)):
                cur_root = queue.popleft()
                # 추출 노드의 자식 노드
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth


#43번
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0  # 재할당 하기 위해 class 변수로

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)  # 리프노드까지 탐색
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)  # 가장 긴 경로
            return max(left, right) + 1  # 존재하지 않는 자식 노드에는 -1 부여했기에 +1하는 것

        dfs(root)
        return self.longest


#44번
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_path = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 동일 값인지 구분
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.max_path = max(self.max_path, left + right)
            return max(left, right)

        dfs(root)
        return self.max_path


#45번
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()  # 부모 노드

            if node:
                node.left, node.right = node.right, node.left  # 동시에 값 변환해야

                queue.append(node.left)
                queue.append(node.right)

        return root


#46번
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        root = TreeNode(v1 + v2)   # root.val=v1+v2

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root

#47번
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        queue = collections.deque([root])
        result = ["#"]  # None 표현

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")

        return " ".join(result)

    def deserialize(self, data):
        if data == "# #":
            return None

        # tree구조 만들어주기
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        index = 2  # first root.left index

        while queue:
            node = queue.popleft()

            # node.left
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            # node.right
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root