# 2. Add Two Numbers
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(carry)
        curr = l3
        ln1 = l1
        ln2 = l2
        while ln1 is not None or ln2 is not None:
            v1 = ln1.val if ln1 is not None else 0
            v2 = ln2.val if ln2 is not None else 0
            s1 = v1 + v2 + carry
            carry = s1 / 10
            curr.next = ListNode(s1 % 10)
            curr = curr.next
            if ln1 is not None:
                ln1 = ln1.next
            if ln2 is not None:
                ln2 = ln2.next

        if carry > 0:
            curr.next = ListNode(carry)
        return l3.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
r1 = s.addTwoNumbers(l1, l2)
while r1 is not None:
    print(r1.val)
    r1 = r1.next
