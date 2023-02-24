from abc import ABC, abstractmethod
class Interface(ABC):
    @abstractmethod
    def Push(self,data):
        pass
    @abstractmethod
    def Pop(self):
        pass
    @abstractmethod
    def traverse(self):
        pass

class Node:
    def __init__(self,data):
        self.data = data
        self.address = None

class Stack(Interface):

    def __init__(self):
        self.head = None

    def Push(self,data):
        new_node  = Node(data)
        new_node.address = self.head
        self.head = new_node

    def Pop(self):
        if self.head==None:
            return
        else:
            tmp = self.head
            self.head = tmp.address
            tmp.address = None
        
            
    def traverse(self):
        print("here is our Stack : ",end= "\n")
        tmp = self.head
        if tmp == None:
            print("No element in List")
        else:
            while tmp.address != None:
                print(tmp.data, end = "-->")
                tmp = tmp.address
            print(tmp.data)


class Queue(Interface):
    def __init__(self):
        self.head = None

    def Push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            tmp = self.head
            while (tmp.address != None):
                tmp = tmp.address
            tmp.address = new_node

    def Pop(self):
        if self.head==None:
            return
        else:
            tmp = self.head
            self.head = tmp.address
            tmp.address = None

    def traverse(self):
        
        print("here is our Queue : ",end= "\n")
        tmp = self.head
        if tmp == None:
            print("No element in List")
        else:
            while tmp.address != None:
                print(tmp.data, end = "<--")
                tmp = tmp.address
            print(tmp.data)




        



    

if __name__ == "__main__" :
    stack = Stack()
    stack.Push(10)
    stack.Push(20)
    stack.Push(30)
    stack.traverse()
    stack.Pop()
    stack.traverse()

    queue = Queue()
    queue.Push(30)
    queue.Push(40)
    queue.Push(50)
    queue.traverse()
    queue.Pop()
    queue.traverse()

