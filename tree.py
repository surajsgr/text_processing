class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)

                else:
                    self.right.insert(data)
        else:
            self.data=data


    def printtree(self):

        if self.left:
            self.left.printtree()
        print(self.data),

        if self.right:
            self.right.printtree()

    def inorder(self,root):
        res=[]
        if root:
            res=self.inorder(root.left)
            res.append(root.data)
            res=res+self.inorder(root.right)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorder(root))