# #Linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None


# class DoubleLL:
#     def __init__(self):
#         self.head=None

#     def display(self):
#         if (self.head==None):
#             print("empty")
        
#         else:
#             temporary=self.head

#             while temporary:
#                 print(temporary.data,"->", end="")
#                 temporary=temporary.next
#             print("None")

#     def search(self,value):
#             temporary=self.head
#             nodeNumber=1

#             while temporary:
#                 if(temporary.data==value):
#                     print(value, "found", )
#                     print("at node",nodeNumber)
#                     return
#                 temporary=temporary.next
#                 nodeNumber += 1
                
#             print(value, "not found")
                


# l=DoubleLL()
# n1=Node(6)
# l.head=n1
# n2=Node(5)
# n1.next=n2
# n2.prev=n1
# n3=Node(9)
# n2.next=n3
# n3.prev=n2
# n4=Node(11)
# n3.next=n4
# n4.prev=n3
# l.display()
# l.search(11)


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if(self.head==None):
            print("Empty")

        else:
            temporary=self.head

            while temporary:

                print(temporary.data,"->", end="")
                temporary=temporary.next
            print("None")

    def search(self,value):
        temporary=self.head
        nodeNumber = 1

        while temporary:
            if(temporary.data==value):
                print(value,"found")
                print("at the node", nodeNumber)
                return
            temporary=temporary.next
            nodeNumber += 1

        print("value not found")


l=DoubleLL()
n1=Node(2)
l.head=n1
n2=Node(5)
n1.next=n2
n2.prev=n1
n3=Node(8)
n2.next=n3
n3.prev=n2
n4=Node(7)
n3.next=n4
n4.prev=n3
n4.next=None
l.display()
l.search(2)


