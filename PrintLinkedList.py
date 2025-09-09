class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def PrintLinkedList(head):
    if head == None:
        print("Linked List is empty")
        return 
    temp=head
    while(temp):
        print(temp.data)
        temp = temp.next


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
PrintLinkedList(node1)

        
 