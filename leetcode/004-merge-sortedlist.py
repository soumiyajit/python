"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def merge_sorted_list(a, b):
    vec = []
    while a:
        vec.append(a.data)
        a = a.next
    while b:
        vec.append(b.data)
        b = b.next

    vec.sort()
    temp = Node(-1)
    head = temp
    for value in vec:
        temp.next = Node(value)
        temp = temp.next
    head = head.next
    return head

a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)

b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

merged_list = merge_sorted_list(a, b)

temp = merged_list
print("Merged Link List is:")
while temp:
    print(temp.data,end=' ')
    temp = temp.next