class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 100000
        # Initialize every bucket with a Dummy Node to avoid head-insertion edge cases
        self.arr = [ListNode(-1, -1) for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        # Start at the dummy node
        curr = self.arr[key % self.size] 
        
        # Traverse looking for the key to update it
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
            
        # If we reach the end and didn't find the key, append it
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # Start at the first REAL node (skipping the dummy)
        curr = self.arr[key % self.size].next
        
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        # Start at the dummy node so we can safely check curr.next
        curr = self.arr[key % self.size]
        
        while curr.next:
            if curr.next.key == key:
                # Bypass the node to delete it
                curr.next = curr.next.next 
                return
            curr = curr.next