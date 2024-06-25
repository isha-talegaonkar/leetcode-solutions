# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return None
        
#         tempHead = head
#         length = 1
#         while tempHead.next is not None:
#             length += 1
#             tempHead = tempHead.next
        
#         print(length)
        
#         result = None
#         for i in range(length):
#             if i == length // 2:
#                 result = head
#             head = head.next         
#         return result

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
        