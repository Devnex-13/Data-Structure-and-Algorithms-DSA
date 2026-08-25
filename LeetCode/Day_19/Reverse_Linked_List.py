class ListNode:
    """Represents a single node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
  prev = None
  current = head 

  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

def print_list(head):
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    print(" -> ".join(nodes) if nodes else "Empty List")

# --- Example Usage ---
if __name__ == "__main__":
    # Create list: 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    
    print("Original List:")
    print_list(head)
    
    # Reverse the list
    reversed_head = reverseLinkedList(head)
    
    print("\nReversed List:")
    print_list(reversed_head)