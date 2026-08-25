class ListNode():
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def hasCycle(head):
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True
  return False

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(hasCycle(head))