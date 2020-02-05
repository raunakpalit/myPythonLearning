class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        cur_node = self.head
        
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0: 
            self.head = cur_node.next
            cur_node = None
            return
        
        count = 1
        prev = None
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next
        
        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1
        
        cur_1.next, cur_2.next = cur_2.next, cur_1.next
        
    def reverse_list(self):
        # A -> B -> C -> D -> 0
        # D -> C -> B -> A -> 0
        # A <- B <- C <- D <- 0

        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_list(self, list2):
        cur_node_1 = self.head #1
        cur_node_2 = list2.head #2

        merged_list = None

        if not cur_node_1:
            return cur_node_2
        if not cur_node_2:
            return cur_node_1

        if cur_node_1 and cur_node_2:
            if cur_node_1.data <= cur_node_2.data:
                merged_list = cur_node_1
                cur_node_1 = merged_list.next
            else:
                merged_list = cur_node_2
                cur_node_2 = merged_list.next

            new_head = merged_list

        while cur_node_1 and cur_node_2:
            if cur_node_1.data <= cur_node_2.data:
                merged_list.next = cur_node_1
                merged_list = cur_node_1
                cur_node_1 = merged_list.next
            else:
                merged_list.next = cur_node_2
                merged_list = cur_node_2
                cur_node_2 = merged_list.next
        
        if not cur_node_1:
            merged_list.next = cur_node_2
        if not cur_node_2:
            merged_list.next = cur_node_1
        
        return new_head

    def remove_duplicates(self):
        # Original List: 1 -> 6 -> 1 -> 4 -> 2 -> 2 -> 4
        # After removal of duplicates: 1 -> 6 -> 4 -> 2
        temp_list = []
        cur_node = self.head
        prev_node = None
        # temp_list.append(cur_node.data)
        while cur_node:
            if cur_node.data in temp_list:
                prev_node.next = cur_node.next
            else:
                temp_list.append(cur_node.data)
                prev_node = cur_node
            
            cur_node = cur_node.next


# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.reverse_list()
# # llist.swap_nodes("B", "D")
# # llist.prepend("E")
# # llist.insert_after_node(llist.head.next, "F")
# # llist.delete_node("B")
# # llist.delete_node_at_pos(3)
# llist.print_list()
# print(llist.length())

# llist1 = LinkedList()
# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.append(9)
# llist1.append(10)

# llist2 = LinkedList()
# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)

# llist1.merge_list(llist2)
# llist1.print_list()

llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)
llist.append(4)
llist.append(4)
llist.append(9)
llist.append(9)
llist.prepend(50)

llist.remove_duplicates()
llist.print_list()
