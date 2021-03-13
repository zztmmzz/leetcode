# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        p_res = res
        p1 = l1
        p2 = l2
        rem = 0
        while p1 and p2:
            node = ListNode()

            val = p1.val + p2.val + rem
            current_node_val = val % 10
            rem = current_node_val / 10
            node.val = current_node_val

            p_res.next = node
            p_res = p_res.next
            p1 = p1.next
            p2 = p2.next

        

        return res

if __name__ == "__main__":
    sol = Solution()
    list1 = ListNode()

    print('test')