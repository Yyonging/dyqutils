from dataclasses import dataclass

@dataclass
class Node:
    val:int
    left = None
    right = None

@dataclass
class ListNode:
    val:int
    next = None
    
    def __str__(self):
        return f'Node[{self.val=}, next:{self.next.val if self.next else None}]'
    
    def __repr__(self):
        return self.__str__()
