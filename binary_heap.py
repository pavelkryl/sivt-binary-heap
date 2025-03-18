from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 

class BinaryHeap:

    def __init__(self):
        self.heap = []
    
    def push(self, element):
        # naivni implementace binarni haldy
        self.heap.append(element)

    def pop(self):
        # naivni implementace binarni haldy
        # najdi nejmensi prvek a vrat ho
        if not self.heap:
            raise Exception("Heap is empty")
        min_idx = 0
        for idx in range(1,len(self.heap)):
            if self.heap[idx].priority < self.heap[min_idx].priority:
                min_idx = idx
        return self.heap.pop(min_idx)


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        # vrati nejmensi element ve fronte (element na cele fronty)
        # protoze mame naivni implementaci, musime projit cely seznam
        min_idx = 0
        for idx in range(1,len(self.heap)):
            if self.heap[idx].priority < self.heap[min_idx].priority:
                min_idx = idx
        return self.heap[min_idx]
        