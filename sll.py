
class linkst:
    '''Singly linked list, with pythonic features.  The list has pointers to both the first and the last node.'''
    __slots__ = ['data', 'next'] #memory efficient
    def __init__(self, iterable=(), data=None, next=None):
        '''Provide an iterable to make a singly linked list.  Set iterable to None to make a data node for internal use.'''
        if iterable is not None: 
            self.data, self.next = self, None
            self.extend(iterable)
        else: #a common node
            self.data, self.next = data, next

    def empty(self):
        '''test if the list is empty'''
        return self.next is None


    def append(self, data):
        '''append to the end of list.'''
        last = self.data
        self.data = last.next = linkst(None, data)
        #self.data = last.next

    def insert(self, data, index=0):
        '''insert data before index.  Raise IndexError if index is out of range'''
        curr, cat = self, 0
        while cat < index and curr:
            curr, cat = curr.next, cat+1
        if index<0 or not curr:
            raise IndexError(index)
        new = linkst(None, data, curr.next)
        if curr.next is None: self.data = new
        curr.next = new

    def reverse(self):
        '''reverse the order of list in place'''
        current, prev = self.next, None
        while current: #what if list is empty?
            next = current.next
            current.next = prev
            prev, current = current, next
        if self.next: self.data = self.next
        self.next = prev

    def delete(self, index=0):
        '''remvoe the item at index from the list'''
        curr, cat = self, 0
        while cat < index and curr.next:
            curr, cat = curr.next, cat+1
        if index<0 or not curr.next:
            raise IndexError(index)
        curr.next = curr.next.next
        if curr.next is None: #tail
            self.data = curr #current == self?

    def remove(self, data):
        '''remove first occurrence of data.  Raises ValueError if the data is not present.'''
        current = self
        while current.next: #node to be examined
            if data == current.next.data: break
            current = current.next #move on
        else: raise ValueError(data)
        current.next = current.next.next
        if current.next is None: #tail
            self.data = current #current == self?

    def __contains__(self, data):
        '''membership test using keyword 'in'.'''
        current = self.next
        while current:
            if data == current.data:
                return True
            current = current.next
        return False

    def __iter__(self):
        '''iterate through list by for-statements.  return an iterator that must define the __next__ method.'''
        itr = linkst()
        itr.next = self.next
        return itr #invariance: itr.data == itr

    def __next__(self):
        '''the for-statement depends on this method to provide items one by one in the list.  return the next data, and move on.'''
        #the invariance is checked so that a linked list
        #will not be mistakenly iterated over
        if self.data is not self or self.next is None:
            raise StopIteration()
        next = self.next
        self.next = next.next
        return next.data

    def __repr__(self):
        '''string representation of the list'''
        return 'linkst(%r)'%list(self)

    def __str__(self):
        '''converting the list to a string'''
        return '->'.join(str(i) for i in self)


    #note: this is NOT the class lab! see file linked.py.
    def extend(self, iterable):
        '''takes an iterable, and append all items in the iterable to the end of the list self.'''
        last = self.data
        for i in iterable:
            last.next = linkst(None, i)
            last = last.next
        self.data = last

    def index(self, data):
        '''TODO: return first index of data in the list self.  Raises ValueError if the value is not present.'''
        #must not convert self to a tuple or any other containers
        current, idx = self.next, 0
        while current:
            if current.data == data: return idx
            current, idx = current.next, idx+1
        raise ValueError(data)

