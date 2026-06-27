class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.remove(self.hashmap[key])
        self.add(self.hashmap[key])
        return self.hashmap[key].value
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.remove(self.hashmap[key])
            self.add(self.hashmap[key])
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.add(node)
            if(len(self.hashmap) > self.capacity):
                lru = self.tail.prev
                self.remove(lru)
                del self.hashmap[lru.key]
    def add(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

class Node:
    def __init__(self, key = 0, value = 0):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value