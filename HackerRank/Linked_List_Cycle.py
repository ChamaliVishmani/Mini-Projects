class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while (True):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            if fast == None or fast.next == None:
                return False


if __name__ == '__main__':
    head = ListNode(1)
    # node1 = ListNode(2)
    # head.next = node1
    # node2 = ListNode(0)
    # node1.next = node2
    # node3 = ListNode(-4)
    # node2.next = node3
    # node3.next = node1

    solution_instance = Solution()
    print(solution_instance.hasCycle(head))
