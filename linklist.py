class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class InsertNode:
    def __init__(self):
        self.head=None
        self.length = 0

    def insert(self,newnode):
        if self.head is None:
            self.head=newnode

        else:
            finalnode=self.head
            while True:
                if finalnode.next is None:
                    break
                finalnode=finalnode.next
            finalnode.next=newnode
    def print(self):

        currentnode=self.head
        while True:

            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    # def lengthlist(self):
    #
    #     currentNode=self.head
    #
    #     while True:
    #         if currentNode is None:
    #             break
    #         else:
    #             self.length+=1
    #             currentNode=currentNode.next
    #     print(self.length)

    def InsertAtbegining(self,newNode):

        if self.head is None:
            self.head=newNode
        currentNode=self.head
        self.head=newNode
        self.head.next=currentNode
    def InsertAtEnd(self,newnode):
        lastnode=self.head
        while True:
            if lastnode.next is None:
                temporarynode=lastnode
                temporarynode.next=newnode
                break
            lastnode=lastnode.next
    def InsertAtMiddle(self,newnode,pos):

        currentnode=self.head
        currpos=1
        while True:

            if currpos==pos:
                temporarynode=previousnode
                temporarynode.next = newnode

                newnode.next = currentnode
                break
            else:
                previousnode=currentnode
                currentnode=currentnode.next
                currpos+=1





node1=Node(5)
insert=InsertNode()
insert.insert(node1)
node2=Node(7)
insert.insert(node2)
node3=Node(10)
insert.insert(node3)


node4=Node(34)
insert.InsertAtbegining(node4)
node5=Node(44)
insert.InsertAtEnd(node5)
node6=Node(50)
insert.InsertAtMiddle(node6,4)
insert.print()
# insert.lengthlist()