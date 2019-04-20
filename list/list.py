class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # check whether index is valid
        if index < 0 or index > self.size - 1:
            return -1
        # if index in [0, size/2), get from head; otherwith get from tail
        if index < self.size / 2:
            current = self.head
            step = index
            while step > 0:
                current = current.next
                step -= 1
            return current.val
        else:
            current = self.tail
            step = self.size - 1 - index
            while step > 0:
                current = current.prev
                step -= 1
            return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        head = self.head
        self.head = new_node
        if head:
            new_node.next = head
            head.prev = new_node
        # first node insert
        else:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        tail = self.tail
        self.tail = new_node
        if tail:
            new_node.prev = tail
            tail.next = new_node
        # first node insert
        else:
            self.head = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        # check whether index in valid
        if index < 0 or index > self.size:
            return
        # if index in [0, size/2), inset from head; else insert from tail
        if index == 0:
            self.addAtHead(val)
        elif index > 0 and index < self.size / 2:
            new_node = ListNode(val)
            prev = self.head
            step = index - 1
            while step > 0:
                prev = prev.next
                step -= 1
            next_node = prev.next
            new_node.next = next_node
            next_node.prev = new_node
            prev.next = new_node
            new_node.prev = prev
            self.size += 1
        elif index < self.size:
            new_node = ListNode(val)
            prev = self.tail
            step = self.size - 1 - index
            while step > 0:
                prev = prev.prev
                step -= 1
            node_prev = prev.prev
            node_prev.next = new_node
            new_node.prev = node_prev
            new_node.next = prev
            prev.prev = new_node
            self.size += 1
        # for index: size -1 or at size, use addAtTail
        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        # check wheter index in valid
        if index < 0 or index >= self.size:
            return
        if self.size == 0:
            self.head = None
            self.tail = None
        elif index == 0:
            head = self.head
            self.head = head.next
            self.head.prev = None
            head.prev = head.next = None
        elif index == self.size - 1:
            tail = self.tail
            self.tail = tail.prev
            self.tail.next = None
            tail.next = tail.prev = None
        elif index < self.size / 2:
            prev = self.head
            step = index - 1
            while step > 0:
                prev = prev.next
                step -= 1
            prev.next = prev.next.next
            if prev.next:
                prev.next.prev = prev
        elif index < self.size - 1:
            prev = self.tail
            step = self.size - 2 - index
            while step > 0:
                prev = prev.prev
                step -= 1
            prev.prev = prev.prev.prev
            if prev.prev:
                prev.prev.next = prev
        self.size -= 1


def decorator(fun):
    def run(*args, **kwargs):
        return fun(*args, **kwargs)
    return run


if __name__ == "__main__":
    inst = MyLinkedList()
    function_list = ["addAtHead","get","addAtIndex","deleteAtIndex","get","addAtIndex","addAtHead","get","deleteAtIndex","get","addAtHead","get","addAtHead","addAtTail","addAtHead","get","addAtHead","addAtHead","get","addAtTail","get","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtIndex","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtTail","get","get","addAtHead","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","addAtTail","addAtHead","addAtTail","addAtHead","get","deleteAtIndex","deleteAtIndex","addAtIndex","addAtTail","addAtTail","deleteAtIndex","get","addAtHead","addAtIndex","addAtHead","addAtTail","addAtIndex","addAtTail","get","addAtHead","addAtHead","addAtTail","addAtTail","addAtHead","addAtHead","addAtIndex","addAtHead","addAtHead","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtTail","addAtIndex","get","addAtTail","get","addAtHead","get","addAtHead","get","get","addAtHead","get","addAtTail","deleteAtIndex","deleteAtIndex","addAtHead","deleteAtIndex","addAtHead","deleteAtIndex","addAtTail","addAtHead"]
    args_list = [[56],[1],[1,50],[1],[1],[1,43],[82],[2],[3],[1],[41],[1],[44],[36],[57],[1],[64],[24],[4],[89],[5],[7],[33],[11],[24],[2,66],[91],[7],[48],[67],[32],[14],[12],[97],[91],[29],[6],[47],[69],[13],[88],[82],[4],[8],[8,85],[75],[56],[16],[51],[4],[13],[27],[11,62],[66],[10],[4],[28],[87],[22,99],[17],[30],[28,82],[17],[16],[76],[61],[36],[45],[31],[19],[2,73],[56],[58],[48],[87],[2],[4,49],[99],[81],[9,2],[39],[35,35],[19],[98],[50],[73],[22],[29],[6],[45],[13],[54],[42],[3],[8],[27],[16],[43],[39],[0],[23]]
    fun_dict = {"addAtHead": inst.addAtHead,
                "addAtTail": inst.addAtTail,
                "addAtIndex": inst.addAtIndex,
                "get": inst.get,
                "deleteAtIndex": inst.deleteAtIndex
                }
    for i in range(len(function_list)):
        func = fun_dict[function_list[i]]
        args = args_list[i]
        func(*args)
        pass
