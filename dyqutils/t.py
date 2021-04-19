from dataclasses import dataclass

@dataclass
class Node:
    val:int
    left = None
    right = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f'Node[{self.val=}, {self.next.val if self.next else None}]'
    
    def __repr__(self):
        return self.__str__()

