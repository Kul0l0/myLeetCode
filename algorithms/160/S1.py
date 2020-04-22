# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = ListNode(-1)
        self.reverse(head,res)
        return res.next

    def reverse(self, head, res):
        if head.next is None:
            res.next = head
            return head
        else:
            foo = self.reverse(head.next, res)
            print(head)
            print(foo)
            foo.next = head
            # head.next = None

a = [1,2,3,4,5]
e = ListNode(0)
foo = e
for i in a:
    foo.next = ListNode(i)
    foo = foo.next

foo = Solution().reverseList(e)
print(foo)
