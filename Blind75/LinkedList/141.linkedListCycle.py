class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:ListNode) ->bool:
        fast = head.next
        slow = head
        while(fast):
            while(slow != fast):
                if slow == fast.next:
                    return True
                slow = slow.next
            fast = fast.next
            
        return False
    
Solution = Solution()
print(Solution.hasCycle(ListNode([3,2,0,-4])))