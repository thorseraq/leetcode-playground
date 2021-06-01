# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        string_rep = ''
        cur = self
        while cur:
            string_rep += f'<{cur.val}> ---> '
            cur = cur.next
        string_rep += '<END>'
        return string_rep
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        laterHead = dummyHead = ListNode()
        dummyHead.next = head

        cur = dummyHead.next
        nxt = cur and cur.next

        # 只有一个节点或者没有节点
        if not (cur and nxt):
            return head

        # 一次处理两个节点
        while cur and nxt:
            furNxt = nxt.next

            print(dummyHead)
            # 一次有三个箭头(next)需要动
            dummyHead.next = nxt
            nxt.next = cur
            cur.next = furNxt

            dummyHead = cur
            cur = furNxt
            nxt = cur and cur.next
        
        print(laterHead)
        return laterHead.next

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)

s = Solution()
reversedHead = s.swapPairs(l)
print(reversedHead)