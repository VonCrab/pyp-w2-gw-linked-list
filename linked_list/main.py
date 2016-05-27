class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        return self.elem == other.elem

    def __repr__(self):
        return "Node: {0} with next node: {1}".format(self.elem, self.next)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):

        self.start = None
        self.end = None
            
        if elements:
            for element in elements:
                self.append(element)

    def __str__(self):
        return '[' + ', '.join(str(i) for i in self) + ']'


    def __len__(self):
        length = 0
        for i in self:
            length += 1
        return length

    def __iter__(self):
        current = self.start
        ordered_nodes = []
        
        while current:
            ordered_nodes.append(current)
            current = current.next
            
        return iter(ordered_nodes)

    def __getitem__(self, index):
        for i, node in enumerate(self):
            if i == index:
                return node.elem

    def __add__(self, other):

        new_list = []
        
        for node in self:
            new_list.append(node.elem)
        for node in other:
            new_list.append(node.elem)
            
        return LinkedList(new_list)

    def __iadd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if self.count() != other.count():
            return False
        
        for x, y in zip(self, other):
            if not x == y:
                return False
        
        return True

    def append(self, elem):
        new_node = Node(elem)
        if self.start is None:
            self.start = new_node
        else:
            self.end.next = new_node
        
        self.end = new_node

    def count(self):
        return len(self)

    def pop(self, index=None):
        
        if self.start is None:
            raise IndexError()
            
        if len(self) <= index:
            raise IndexError()

        if index is None:
            index = len(self) - 1
        
        if index == 0:
            return_value = self.start.elem
            self.start = self.start.next
            
        else:
            for i, node in enumerate(self):
                if i == index - 1:
                    return_value = node.next.elem
                    node.next = node.next.next

        return return_value
