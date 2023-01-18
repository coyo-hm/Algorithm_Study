class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회(Preorder Traversal)
def pre_oreder(node):
    print(node.data, end="")
    if node.left_node != None:
        pre_oreder(tree[node.left_node])
    if node.right_node != None:
        pre_oreder(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_oreder(node):
    if node.left_node != None:
        in_oreder(tree[node.left_node])
    print(node.data, end="")
    if node.right_node != None:
        in_oreder(tree[node.right_node])
        
# 후위 순회(Postorder Traversal)
def post_oreder(node):
    if node.left_node != None:
        post_oreder(tree[node.left_node])
    if node.right_node != None:
        post_oreder(tree[node.right_node])
    print(node.data, end="")

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_oreder(tree["A"])
print()
in_oreder(tree["A"])
print()
post_oreder(tree["A"])