# use a pointer to remember the value and swap on the copied value

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            swap1, swap2, swap3 = current.next, current.next.next, current.next.next.next
            current.next = swap2
            swap2.next = swap1
            swap1.next = swap3
            current = swap1
        return dummy.next