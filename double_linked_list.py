class Cell():
    """ The class Cell allows to represent a list from chained elements of type Cell. Each element of the 
    list contains a value, a pointer towards the next element and a pointer towards the previous element. """
    
    def __init__(self):
        """ Creates an instance of class Cell
        input   -- self : instance of class Cell
        """
        self.value = object
        self.next = None
        self.prev = None
        
    def __str__(self):
        """ Returns a string representing the self Cell
        input   -- self : instance of class Cell
        output  -- string, representation of the self cell
        """
        result = str(self.value) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.value)
        result += ', prev:'
        if self.prev == None:
            result += 'None'
        else:
            result += str(self.prev.value)
        return '{ ' + result + ' }' 
        
        
class DoubleLinkedList:
    """ The class DoubleLinkedList allows to represent a list from chained elements of type Cell. Each element 
    of the list contains a value, a pointer towards the next element and a pointer towards the previous element. """
    
    def __init__(self):
        """ Creates an instance of class DoubleLinkedList
        input   -- self : instance of class DoubleLinkedList
        """
        self.mfirst = None   # First cell in the list
        self.mlast = None    # Last cell in the list
        self.size = 0        # Number of elements in the list
        
    def __str__(self):
        """ Returns a string representing DoubleLinkedList self
        input   -- self : instance of class DoubleLinkedList
        output  -- string
        """
        msg = '['
        if not self.is_empty_list():
            e = self.mfirst
            while e.next != None:
                msg += str(e.value) + ','
                e = e.next
            msg += str(e.value)
        return msg + ']'
        
    def size_list(self):
        """ Give the number of elements in the list
        input   -- self : instance of class DoubleLinkedList
        output  -- n : int, the size of the list
        """
        return self.size
        
    def is_empty_list(self):
        """ Returns True if and only if Liste self is empty
        input   -- self : instance of class DoubleLinkedList
        output  -- v : bool
        """
        return self.mfirst == None
        
    def insert_first(self, v):
        """ Inserts the value v at the head of the list
        input   -- self : instance of class DoubleLinkedList
                -- v : value of type object to insert at the first position
        output  -- self in which the element of value v has been inserted at the head of the list
                    the size of the list is updated
        """
        m = Cell()
        m.value = v
        m.prev = None
        if self.mfirst == None:
            m.next = None
            self.mlast = m
        else:
            self.mfirst.prev = m
            m.next = self.mfirst
        self.mfirst = m
        self.size += 1

        
    def insert_last(self,v):  
        """ Inserts the value v at the end of the list
        input   -- self : instance of class DoubleLinkedList
                -- v : value of type object to insert at the last position
        output  -- self in which the element of value v has been inserted at the end of the list
                    the size of the list is updated 
        """
        if self.mfirst == None:
            self.insert_first(v)
        else:
            m = Cell()
            m.value = v
            m.next = None
            self.mlast.next = m
            m.prev = self.mlast
            self.mlast = m
            self.size += 1
        
    def insert_before(self, v, p):
        """ Returns the list in which the element of value v has been inserted before the first cell of value p
        input   -- self : instance of class DoubleLinkedList
                -- v : value of type object to insert
                -- p : value of the cell before which the value should be inserted
        output  -- self in which the element of value v has been inserted before the first cell of value p
        """
        #TODO

    def insert_after(self, v, p):
        """ Returns the list in which the element of value v has been inserted after the first cell of value p
        input   -- self : instance of class DoubleLinkedList
                -- v : value of type object to insert
                -- p : value of the cell after which the value should be inserted
        output  -- self in which the element of value v has been inserted after the first cell of value p
        """
        #TODO
        
    def insert_at(self,v,i):
        """ Returns the list in which the element of value v has been inserted at index i
        input   -- self : instance of class DoubleLinkedList
                -- v : value of type object to insert
                -- i : int index at which the element of value v is inserted
                    exception when the index i is too small or too big
        output  -- self in which the element of value v has been inserted at index i of the list
                    the size of the list is updated
        """
        #TODO
        
    def get_first(self):
        """ Returns the first element of the list (of type Cell)
        input   -- self : instance of class DoubleLinkedList
                pre-cond: is not empty
        output  -- p : element of type Cell
        """
        return self.mfirst
    
    def get_at(self, i):
        """ Returns the element at the given index in the list (of type Cell)
        input   -- self : instance of class DoubleLinkedList
                -- i : int, index of the element
                pre-cond: self is not empty
        output  -- p : element of type Cell
        """
        if i>self.size-1:
            return
        p=self.mfirst
        for _ in range(i):
            p=p.next
        return p
        
    def get_last(self):
        """ Returns the last element of the list (of type Cell)
        input   -- self : instance of class DoubleLinkedList
                pre-cond: self is not empty
        output  -- p : element of type Cell
        """
        #TODO
        
    def delete_at(self,i):
        """ Returns the list in which the element at index i has been deleted
        input   -- self : instance of class DoubleLinkedList
                -- i : int, index of the element to be deleted
        output  -- self in which the element at index i has been deleted
                    the size of the list is updated 
        """
        #TODO
    
if __name__ == '__main__':
    print('Hello DoubleLinkedList !')
