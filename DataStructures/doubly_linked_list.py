class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.prev = None
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
        

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = None
            new_node.prev = None
        else:
            cur = self.head
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        new_node = Node(data)
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                next_node = cur.next
                next_node.prev = new_node
                new_node.next = next_node
                cur.next = new_node
                new_node.prev = cur
            cur = cur.next

    def add_before_node(self, key, data):
        new_node = Node(data)
        prev_node = None
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                prev_node = cur.prev
                prev_node.next = new_node
                new_node.next = cur
                cur.prev = new_node
                new_node.prev = prev_node
            cur = cur.next

    def delete(self, key):
        cur = self.head
        prev = None
        while cur:
            if cur.prev is None and cur.data == key:
                nxt = cur.next
                self.head = nxt
                nxt.prev = None
                return
            elif cur.next is None and cur.data == key:
                prev = cur.prev
                prev.next = None
                return
            elif cur.data == key:
                prev = cur.prev
                nxt = cur.next
                prev.next = nxt
                nxt.prev = prev
            cur = cur.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            prev = cur.prev
            nxt = cur.next
            cur.next = prev
            cur.prev = nxt
            cur = nxt
        if prev:
            self.head = prev.prev

    def remove_duplicates(self):
        temp = []
        cur = self.head
        while cur:
            if cur.data not in temp:
                temp.append(cur.data)
            else:
                if cur.next:
                    prev = cur.prev
                    nxt = cur.next
                    nxt.prev = prev
                    prev.next = nxt
                else:
                    if cur.data in temp:
                        prev = cur.prev
                        prev.next = None
            
            cur = cur.next
            
    def pairs_with_sum(self, sum_val):
        pairs = []
        p = self.head
        q = None

        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))
# dllist.reverse()
# dllist.add_before_node(4, 5)
# dllist.delete(4)
# dllist.prepend(0)
# dllist.append(8)
# dllist.append(4)
# dllist.append(4)
# dllist.append(6)
# dllist.append(4)
# dllist.append(8)
# dllist.append(4)
# dllist.append(10)
# dllist.append(12)
# dllist.append(12)

# 
# dllist.remove_duplicates()
dllist.print_list()