from copy import deepcopy
from linkedList import LinkedList

class SubSequence(LinkedList):
    """
    This class represents a SubSequence of Cards from the Deck.
    This class inherits from the LinkedList class.

    The CardSorter holds a Python list of these SubSequence objects.

    There are no instance variables for this class, except for those
    inherited from the LinkedList class.

    The class methods include 
    a. __init__: This method calls the LinkedList constructor 
                 using super()
    b. first_card: This method returns a reference to the Card at 
                   the head of the LinkedList without removing it.
    c. add_card: This method adds a Node to the front of the 
                 LinkedList containing the passed in Card.
    d. contains_card: This method searches the LinkedList for the 
                      passed in Card and returns true if Card is in 
                      this SubSequence, or False if not.               
    e. clone_subseq: This method returns a deep copy of this 
                     SubSequence. It traverses this SubSequence and 
                     adds a deepcopy of every Node at the end of the 
                     new SubSequence being returned.
    f. reverse_subseq: This method reverses this SubSequence in place.  
                       It uses three Node pointers: a current_node to 
                       walk the SubSequence, a prev_node to follow the 
                       current_node, and a next_node to grab the Node 
                       in front of current_node, as it walks the
                       LinkedList.
    g. __str__ : This method returns a string of the Cards in the 
                 SubSequence.                  
    """
    
    def __init__(self):
        """
        This method is the SubSequence constructor.  Call the
        LinkedList constructor using super()
        """
        
        super().__init__()
        
    def first_card(self):
        """
        This method returns a reference to the Card at the head 
        of the LinkedList without removing it.
        """
        
        return self._head.data
        
    def add_card(self, card):
        """
        This method adds a Node to the front of the LinkedList 
        containing the passed in Card
        """
        
        self.add_first(card)

    def contains_card(self, card):
        """
        This method searches the LinkedList for the passed in Card 
        and returns true if Card is in this SubSequence, or False
        if not.
        """
        current_node = self._head
        for c in range(self.get_size()):
            if card.compare(current_node.data) == 0:
                return True
            current_node = current_node.next
        return False
        
    def clone_subseq (self):
        """
        This method returns a deep copy of this SubSequence.  
        It traverses this SubSequence and adds a deepcopy of every 
        Node ( deepcopy is a method in the Python copy module. ).
        Add the copied Node at the END of the new SubSequence 
        being returned.
        """
        current_node = self._head
        clone_to_return = SubSequence()
        for n in range(self.get_size()):
            clone_to_return.add_last(deepcopy(current_node.data))
            current_node = current_node.next
        return clone_to_return
        
    def reverse_subseq (self):
        """
        This method reverses this SubSequence in place.  It uses 
        three Node pointers: a current_node to walk the SubSequence,
        a prev_node to follow the current_node, and a next_node to
        grab the Node in front of current_node, as it walks the
        LinkedList. 
        """
        
        prev_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self._head = prev_node
        return super().__str__()

    def __str__(self): 
        """
        This method returns a string containing the Cards
        in this SubSequence. 
        """
        
        return super().__str__()
    
       
