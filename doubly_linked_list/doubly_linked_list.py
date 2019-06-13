"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            item = ListNode(value)
            self.head = item
            self.tail = item
            self.head.next = self.tail
            self.tail.prev = self.head
            self.head.prev = None
            self.tail.next = None
        
        elif self.head == self.tail:
            old_head = self.head
            self.head = ListNode(value, old_head.prev, old_head)
            old_head.prev = self.head
        
        else:
            new_node = ListNode(value, self.head.prev, self.head)
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        head = self.head
        self.delete(self.head)
        return head.value

    def add_to_tail(self, value):
        self.length += 1
        
        if not self.head and not self.tail:
            item = ListNode(value)
            self.head = item
            self.tail = item
            self.head.next = self.tail
            self.tail.prev = self.head
            self.head.prev = None
            self.tail.next = None


        elif self.head == self.tail:
            old_tail = self.tail
            self.tail = ListNode(value, old_tail, old_tail.next)
            old_tail.next = self.tail

        else:
            new_node = ListNode(value, self.tail, self.tail.next)
            self.tail.next = new_node
            self.tail = new_node


    def remove_from_tail(self):
        if not self.head or not self.tail:
            return None
        tail = self.tail
        self.delete(self.tail)
        return tail.value

    def move_to_front(self, node):
        if not self.head and not self.tail:
            return None
        
        if self.head == self.tail:
            return None
        else:
            self.delete(node)
            self.add_to_head(node.value)

    def move_to_end(self, node):
        if not self.head and not self.tail:
            return None
        
        if self.head == self.tail:
            return None
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return None
        node_prev = node.prev
        node_next = node.next
        node.prev = None
        node.next = None
        
        if node_prev:
            node_prev.next = node_next
        
        if node_next:
            node_next.prev = node_prev
        
        if node == self.head:
            self.head = node_next
        
        if node == self.tail:
            self.tail = node_prev

    def get_max(self):
        if not self.head and not self.tail:
            return None
        maxval = 0
        current = self.head
        while current:
            # print(current.value)
            if current.value > maxval:
                maxval = current.value
            current = current.next
        return maxval
