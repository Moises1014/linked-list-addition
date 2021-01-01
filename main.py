# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #carry over for addition (ex 7 + 4 =11 will have a carry over of 1)
        carry_over= 0
        
        # makes sure where in the current node of list
        head = curr = ListNode(0)
        
        #itirations 
        while l1 or l2  or carry_over:
            currentVal = carry_over
            #add current values in list after carry over from last node if 
            #list has has a value in node
            #add nodes 
            if(l1 is None):
                currentVal += 0
            else:
                currentVal += l1.val
            if(l2 is None):
                currentVal += 0 
            else:
                currentVal += l2.val
            #check if value after adding is more than 10
            if currentVal >= 10:
                currentVal -=10
                carry_over = 1
            else:
                carry_over = 0
                
            #add current value to list new listnode 
            curr.next = ListNode(currentVal)
            curr = curr.next
            
            #itteration for linked list l1 and l2
            if l1 is None and l2 is None :
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
                
        return head.next
            
