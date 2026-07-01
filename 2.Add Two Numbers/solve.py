# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.l1 = l1
        self.l2 = l2

        node_value = l1.val
        node_next = l1.next
        num1 = ""
        
        while True:
            num1 += str(node_value)
            if node_next == None:
                break
            node_value = node_next.val
            node_next = node_next.next

        node_value = l2.val
        node_next = l2.next
        num2 = ""
        while True:
            num2 += str(node_value)
            if node_next == None:
                break
            node_value = node_next.val
            node_next = node_next.next
        
        x = int(num1[::-1]) + int(num2[::-1])

        if x == 0:
            return ListNode(0)
        
        y = []
        while x != 0:
            y.append(x%10)
            x //= 10
        
        head = ListNode(y[0])
        tail = head
        counter = 1
        while counter < len(y):
            tail.next = ListNode(y[counter])
            tail = tail.next
            counter+=1
        
        return head
