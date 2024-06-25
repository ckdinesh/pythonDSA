# To do
# 1.create a func for insert_data from a List
# 2.get length func
# 3.remove the element at index
# 4. insert( 0,"")

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data, None)
                return
            itr = itr.next

    def get_length(self):
        l = 0
        itr = self.head
        if itr is None:
            return l
        else:
            while itr:
                l += 1
                itr = itr.next
        return l

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next

        print(listr)

    def remove_at(self, index):
        if self.head is None:
            return None

        itr = self.head
        if index == 1:
            self.head = itr.next
        else:
            idx = 1
            while itr:
                if idx == index - 1:
                    itr.next = itr.next.next
                    return
                idx += 1
                itr = itr.next

    def insert_values(self, lst):
        for i in lst:
            self.insert_at_end(i)

    def insert_after_value(self, data_after, data_to_insert):

        itr=self.head

        while itr:

            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node

            itr=itr.next



    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
        itr = self.head

        if itr is None:
            return
        if itr.data == data:
            self.head = itr.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    #ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()
    ll.remove_by_value("grap"
                       "")
    ll.print()
    # ll.insert_at_beginning(45)
    # ll.insert_at_beginning(56)
    #ll.insert_at_end(67)
    # ll.insert_at_end(99)
    # ll.insert_at_beginning(78)
    # ll.remove_at(3)