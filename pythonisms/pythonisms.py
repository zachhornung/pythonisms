class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        self.head = Node(value, self.head)
        self.length += 1

    def includes(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False

    def __str__(self):
        string = ''
        current = self.head
        while current:
            string += f'{current.value} --> '
            current = current.next
        string += 'None'
        return string


    def append(self, value):
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(value)
                self.length += 1
                break
            current = current.next


    def insert_before(self, value, new_value):
        current = self.head
        previous = None
        while current:
            if self.head.value == value:
                self.insert(new_value)
                break
            if current.value == value:
                previous.next = Node(new_value, current)
                self.length += 1
                break
            previous = current
            current = current.next

    def insert_after(self, value, new_value):
        current = self.head
        insert_before_this = current.next
        while current:
            if self.head.value == value:
                self.insert_before(insert_before_this.value, new_value)
                break
            if current.value == value:
                current.next = Node(new_value, insert_before_this)
                self.length += 1
                break
            current = current.next
            insert_before_this = current.next

    def kth_from_end(self, num):
        if num < 0:
            return 'Given number cannot be negative'
        if self.length == 1:
            return f'There is only one node in this linked list. Its value is {self.head.value}'
        if num > self.length:
            return 'Given number is outside of range'
        
        current = self.head
        for _ in range(1, self.length-num):
            current = current.next
        return current.value

    def __iter__(self):
      def my_generator():
        current = self.head
        while current:
          yield current.value
          current = current.next
      return my_generator()
        



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next