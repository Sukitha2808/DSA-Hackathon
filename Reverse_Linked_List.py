class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse_linked_list(head):
    if not head or not head.next: 
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head  
    head.next = None       
    return new_head 
def display(head):
    if head == None:
        print("Linked List is empty")
        return 
    temp=head
    llst=[]
    while(temp):
        llst.append(str(temp.data)) 
        temp = temp.next
    print(llst)


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(90)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print("Before Reversing\n")
display(node1)
result=reverse_linked_list(node1)
print("After Reversing\n")
display(result)

        
 