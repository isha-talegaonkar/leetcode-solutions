# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head, k):
        prev, curr = None, head
        while k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ptr = head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reversedHead = self.reverseLinkedList(head, k)

            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head