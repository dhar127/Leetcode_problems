# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        k = []
        # Collect all values from all linked lists
        for head in lists:
            while head:
                k.append(head.val)
                head = head.next
        
        # Sort the collected values
        k.sort()
        
        # Convert sorted values back into a linked list
        return self.convert(k) if len(k) != 0 else None
    
    def convert(self, k):
        if not k:
            return None
        
        head = ListNode(k[0])
        current = head
        for value in k[1:]:
            new_node = ListNode(value)
            current.next = new_node
            current = current.next
        
        return head
