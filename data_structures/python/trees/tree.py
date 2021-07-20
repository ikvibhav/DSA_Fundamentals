class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None #leaf node termination
        self.right = None
    
    def insert(self, data):
        if data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
    
    def find(self, key):
        if key == self.data:
            return self  #Returns the current instance, ie. instance of Treenode
        if key > self.data and self.right is not None:
            return self.right.find(key)
        elif self.left is not None:
            return self.left.find(key)

    def get_max(self):
        rnode = self
        while rnode.right is not None:
            rnode = rnode.right
        return rnode.data

    def get_min(self):
        lnode = self
        while lnode.left is not None:
            lnode = lnode.left
        return lnode.data
    
    def inorder_display(self, node):
        if node:
            self.inorder_display(node.left)
            print(node.data)
            self.inorder_display(node.right)

    def inorder_successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        #Base Case
        if root is None:
            return root

        #Searching the key
        if key > root.data:
            root.right = self.delete_node(root.right, key)
        elif key < root.data:
            root.left = self.delete_node(root.left, key)
        else:
            #One child or None child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            if root.right is None:
                temp = root.left
                root = None
                return temp

            #Two Children
            in_succ = self.inorder_successor(root.right)
            root.data = in_succ.data
            root.right = self.delete_node(root.right, in_succ.data)

        return root        

#Initialising and inserting into the BST
my_root, my_data = 50, (40, 70, 60, 20, 99, 45)
print(f'my_root:{my_root}')
print(f'my_data:{my_data}')
my_tree = TreeNode(my_root)
for val in my_data:
    my_tree.insert(val)
print(f'root tree:{my_tree.data}')

#Finding min and max 
print(f'Min Value->{my_tree.get_min()}')
print(f'Max Value->{my_tree.get_max()}')

#finding a key
my_key = 20
node_found = my_tree.find(my_key)
if node_found is not None:
   print(f'key found is:{node_found.data}')
else:
   print(f'key not found')

#Inorder Display
my_tree.inorder_display(my_tree)
print(" ")

#Delete a node
my_tree.delete_node(my_tree, 70)

my_tree.inorder_display(my_tree)