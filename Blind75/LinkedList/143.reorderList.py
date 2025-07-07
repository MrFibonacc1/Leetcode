class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode)->None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next 
            slow = slow.next
        second = slow.next
        slow.next = None
        
        curr,prev = second, None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, other = head, prev
        while(first and other):
            temp1, temp2 = first.next, other.next
            first.next = other
            other.next = temp1
            first, other = temp1,temp2


    
Solution = Solution()
print(Solution.reorderList(ListNode([1,2,3,4,5])))