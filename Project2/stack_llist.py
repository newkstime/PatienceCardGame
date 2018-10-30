class _StackNode():
    """
    This class represents the Node of a Stack implemented as a 
    LinkedList.
    
    The instances variables of this class include:
    1. self.item: holds the item for the StackNode.
    2. self.next: holds the pointer to the next StackNode.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 each instance variable to the passed in parameters.
    """
    
    def __init__(self, item, link):
        """
        This method is the constructor and it initializes each
        instance variable to the passed in parameters.
        """
        
        self.item = item
        self.next = link
        
class Stack():
    """
    This Stack class is a singly LinkedList implementation of a Stack.
    
    The instances variables of this class include:
    1. self._top: holds the pointer to the top StackNode of the Stack
    2. self._size: holds the number of StackNode on the Stack.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 the Stack instance variables.
    b. is_empty: This method returns True, if the Stack  is empty or 
                 False otherwise.
    c. __len__: This method returns the number of items in the Stack.
    d. peek: This method returns the top item on the Stack without 
             removing it.
    e. pop: This method removes and returns the top item on the Stack.
    f. push: This method pushes an item onto the top of the Stack.
    g. __str__: This method returns the contents of the Stack as a 
                string. 
    """
    
    def __init__(self):
        """
        This method is the constructor and it initializes the Stack 
        instance variables, creating an empty Stack.
        """
        
        self._top = None
        self._size = 0
        
    def is_empty(self):
        """
        This method returns True if the Stack is empty or False 
        otherwise.
        """
        
        return len(self) == 0

    def __len__(self):
        """
        This method returns the number of items in the Stack.
        """
        
        return self._size

    def peek(self):
        """
        This method returns the top item on the Stack without 
        removing it.
        """
        
        return self._top.item

    def pop(self):
        """
        This method removes and returns the top item on the Stack.
        """
        if self._top is None:
            return None
        else:
            popped = self._top.item
            self._top = self._top.next
            self._size -= 1
            return popped

    def push(self, item):
        """
        This method pushes an item onto the top of the Stack.
        """
        
        self._top = _StackNode(item, self._top)
        self._size += 1
        
    def __str__(self):
        """
        This method returns the contents of the Stack as a string
        """
        
        stack_contents = ""
        node = self._top
        for x in range(self._size):
            stack_contents += str(node.item) + " "
            node = node.next
        return stack_contents
