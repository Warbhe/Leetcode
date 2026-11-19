# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        vals: list[int] = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        vals.sort()
        curr = head
        for v in vals:
            curr.val = v
            curr = curr.next
        return head          