class ListNode:
    def __init__(self, key: int, val: int, pred=None, next=None):
        self.key = key
        self.val = val
        self.pred = pred
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = self.tail = None
        self.count: int = 0
        self.cap: int = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.refresh(key, self.cache[key].val)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        self.refresh(key, value)

    def refresh(self, key, val) -> None:
        if key not in self.cache:
            self.count += 1
            node = ListNode(key, val, self.tail, None)
            self.cache[key] = node
            if self.count == 1:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            if self.count > self.cap:
                old_head = self.head
                self.head = old_head.next
                if self.head:
                    self.head.pred = None
                del self.cache[old_head.key]
                self.count -= 1
        else:
            node = self.cache[key]
            node.val = val
            if node == self.tail:
                return
            else:
                if node == self.head:
                    self.head = node.next
                    self.head.pred = None
                else:
                    node.pred.next = node.next
                node.next.pred = node.pred
                self.tail.next = node
                node.pred = self.tail
                node.next = None
                self.tail = node

# init
# hashmap key int, val -> doubly linked list node of key, val, pred, next
# head tail = None
# length = 0

# get
# put key to tail
# return node.val from hashmap[key]

# put
# put key to tail

# put key to tail:
# if key not in hashmap:
#     count += 1
#     hashmap[key] = new node of key
#     if count == 1:
#         head = hashmap[key]
#     if count > cap:
#         old_head = head
#         head = head.next
#         head.pred = None
#         del hashmap[old_head]
#         count -= 1
# else:
#     get node from hashmap[key]
#     if key is tail do nothing
#     else
#         if node is head
#             head = node.next
#         else
#             node.pred.next = node.next
#         node.next.pred = node.pred
#         tail.next = node
#         node.pred = tail
#         node.next = None
#         tail = node



# cap 1
# 1: None, None  

# 1: None, 2
# 2: 1, None

# 2: None, None

# cap 3
# 1: None       

# 1: 2
# 2: None

# 1: None, 2
# 2: 1, 3
# 3: 2, None

# 1: None, 3
# 3: 1, 2
# 2: 3, None

# cap 1
# 1: None

# 1: None


# cap 4
# 1: None       

# 1: 2
# 2: None

# 1: None, 2
# 2: 1, 3
# 3: 2, None

# 1: None, 2
# 2: 1, 3
# 3: 2, 4
# 4: 3, None

# 1: None, 3

# 3: 1, 4
# 4: 3, 2
# 2: 4, None