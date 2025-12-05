class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None
    
def createLL(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head

def createCycle(head, pos):
    if pos == -1: return head
    cycle_node = None
    curr = head
    idx = 0
    while curr.next:
        if idx == pos:
            cycle_node = curr
        curr = curr.next
        idx += 1
    curr.next = cycle_node
    return head

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow==fast:
            return True
    return False

#main
arr = [3, 2, 0, -4]
pos = 1
head = createLL(arr)
head = createCycle(head, pos)
print(hasCycle(head))