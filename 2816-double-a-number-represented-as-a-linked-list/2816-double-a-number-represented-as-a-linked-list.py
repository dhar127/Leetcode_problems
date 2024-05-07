# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0 and head.next is None:
            return head
        def createNode(val):
            return ListNode(val)
        def reverseLinkedList(node):
            prev = None
            current = node
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        num = 0
        current = head
        while current is not None:
            num = num * 10 + current.val
            current = current.next
        num *= 2
        dummy = ListNode(-1)
        current = dummy
        while num > 0:
            current.next = createNode(num % 10)
            current = current.next
            num //= 10
        return reverseLinkedList(dummy.next)
