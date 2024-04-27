class Node:
	def __init__(self,data):
                self.data = data
                self.next = None
	
class Linkedlist:
        def __init__(self):
                self.head = None
        def Print_ll(self):
                if self.head is None:
                        print("Linked list is empty")
                else:
                        n = self.head
                        while n is not None:
                                print(n.data)
                                n = n.next
        def add_at_beginning(self, data):
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node


LL = Linkedlist()
LL.add_at_beginning(10)
LL.add_at_beginning(89)
LL.Print_ll()

                               
                