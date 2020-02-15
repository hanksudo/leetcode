class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None:
            return -1

        if index == 0:
            return self.head.val

        current = self.head
        for _ in range(index):
            current = current.next
            if current is None:
                return -1

        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head:
            node.next = self.head
        else:
            self.tail = node

        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
                if current is None:
                    return

            if current.next is None:
                self.addAtTail(val)
            else:
                node = Node(val)
                node.next = current.next
                current.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
                if current is None:
                    return

            if current.next:
                current.next = current.next.next
            else:
                current.next = None

            if not current.next:
                self.tail = current


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
assert obj.get(0) == -1
obj.addAtHead(2)
assert obj.get(0) == 2
assert obj.get(1) == -1
obj.addAtHead(1)
assert obj.get(0) == 1
assert obj.get(1) == 2
assert obj.get(2) == -1
obj.addAtTail(3)
assert obj.get(2) == 3

obj.addAtIndex(0, 5)
assert obj.get(0) == 5
obj.deleteAtIndex(0)
assert obj.get(0) == 1

obj.addAtIndex(1, 5)
assert obj.get(1) == 5
obj.deleteAtIndex(1)
assert obj.get(1) == 2

obj.addAtIndex(2, 5)
assert obj.get(2) == 5
obj.deleteAtIndex(2)
assert obj.get(2) == 3

obj.deleteAtIndex(3)  # nothing happen

# for _ in range(8):
#     print(obj.get(_))

commands = ["MyLinkedList", "addAtHead", "addAtTail", "addAtTail", "get", "get", "addAtTail", "addAtIndex", "addAtHead", "addAtHead", "addAtTail", "addAtTail", "addAtTail", "addAtTail", "get", "addAtHead", "addAtHead", "addAtIndex", "addAtIndex", "addAtHead", "addAtTail", "deleteAtIndex", "addAtHead", "addAtHead", "addAtIndex", "addAtTail", "get", "addAtIndex", "addAtTail", "addAtHead", "addAtHead", "addAtIndex", "addAtTail", "addAtHead", "addAtHead", "get", "deleteAtIndex", "addAtTail", "addAtTail", "addAtHead", "addAtTail", "get", "deleteAtIndex", "addAtTail", "addAtHead", "addAtTail", "deleteAtIndex", "addAtTail", "deleteAtIndex", "addAtIndex", "deleteAtIndex", "addAtTail", "addAtHead", "addAtIndex", "addAtHead", "addAtHead", "get", "addAtHead", "get", "addAtHead", "deleteAtIndex", "get", "addAtHead", "addAtTail", "get", "addAtHead", "get", "addAtTail", "get", "addAtTail", "addAtHead", "addAtIndex", "addAtIndex", "addAtHead", "addAtHead", "deleteAtIndex", "get", "addAtHead", "addAtIndex", "addAtTail", "get", "addAtIndex", "get", "addAtIndex", "get", "addAtIndex", "addAtIndex", "addAtHead", "addAtHead", "addAtTail", "addAtIndex", "get", "addAtHead", "addAtTail", "addAtTail", "addAtHead", "get", "addAtTail", "addAtHead", "addAtTail", "get", "addAtIndex"]
parameters = [[], [84], [2], [39], [3], [1], [42], [1, 80], [14], [1], [53], [98], [19], [12], [2], [16], [33], [4, 17], [6,8], [37], [43], [11], [80], [31], [13,23], [17], [4], [10,0], [21], [73], [22], [24,37], [14], [97], [8], [6], [17], [50], [28], [76], [79], [18], [30], [5], [9], [83], [3], [40], [26], [20,90], [30], [40], [56], [15,23], [51], [21], [26], [83], [30], [12], [8], [4], [20], [45], [10], [56], [18], [33], [2], [70], [57], [31, 24], [16, 92], [40], [23], [26], [1], [92], [3,78], [42], [18], [39, 9], [13], [33, 17], [51], [18, 95], [18, 33], [80], [21], [7], [17, 46], [33], [60], [26], [4], [9], [45], [38], [95], [78], [54], [42, 86]]
expecteds = [None, None, None, None, -1, 2, None, None, None, None, None, None, None, None, 84, None, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, None, None, None, None, 37,None, None, None, None, None, 23,None, None, None, None, None, None, None, None, None, None, None, None, None, None, 19, None, 17, None, None, 56, None, None, 31, None, 17,None,12,None, None, None, None, None, None, None, 40, None, None, None, 37, None, 76, None, 42,None, None, None, None, None, None, 80, None, None, None, None, 43, None, None, None, 40, None]

def print_singly_linked_list(node, sep):
    while node:
        print(node.val, end='')

        node = node.next

        if node:
            print(sep, end='')
    print()

def concat_linked_list(node, sep=" "):
    values = []
    values.append(node.val)
    while node.next:
        node = node.next
        values.append(node.val)

    return sep.join(map(str, values))

llist = MyLinkedList()
count = 0
for idx, command in enumerate(commands):
    parameter = parameters[idx]
    expected = expecteds[idx]
    # print(idx, command, parameter)
    if command == "MyLinkedList":
        continue
    elif command == "addAtHead":
        llist.addAtHead(parameter[0])
        count += 1
    elif command == "addAtTail":
        llist.addAtTail(parameter[0])
        count += 1
    elif command == "addAtIndex":
        llist.addAtIndex(parameter[0], parameter[1])
        count += 1
    elif command == "deleteAtIndex":
        count -= 1
        llist.deleteAtIndex(parameter[0])
    elif command == "get":
        print(llist.get(parameter[0]), expected)
        assert llist.get(parameter[0]) == expected

    print("count", count, len(concat_linked_list(llist.head).split()))
    print_singly_linked_list(llist.head, " ")
    print()
