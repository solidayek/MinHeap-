####################################################
# CS 22, Prof. Muldrow
# Name: Soliday Ek  
# Assignment: CS 22 – Week 9 Homework Assignment
# Due Date: 11/26/2023
####################################################
class MinHeap(): # the values of nodes are smaller than the parents
    def __init__(self):
        self.heap = []
        self.size = 0
    def get_left_child(self, index):
        return 2*index + 1
    def get_right_child(self, index):
        return 2*index + 2
    def get_parent(self, index):
        return (index - 1) // 2 # we assume that root node has index 0
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] # you will take the indicated indexes that have been passed and switch the two nodes between tehse two indexes
    def remove_root(self): # simply remove the root
        # we want to test if the heap is empty, if is, then return NONE
        if len(self.heap) == 0:
            return None
        # we can use the method pop() to remove last item of the list like we've used for stack
        if len(self.heap) == 1:
            return self.heap.pop() # simply pop it since it's the last item
        # we also want the program to determine the followings:
        value = self.heap[0] # 1. salve the value at the root (index 0)
        self.heap[0] = self.heap.pop()
        self.size -= 1 # 2. change the value at the root to the value at the end
        # 3. use sink_down to get the new root in its proper place in the heap
        self.sink_down(0)
    def insert(self, value): # this function will take the new value and insert all the way at the end of the heap
        self.heap.append(value)
        # since we are creating a function for minheap, that means the values of children should be less than parents
        current = len(self.heap) - 1 # we will obtain the index of last node from heap
        # we will use the bubble-up or upheap process as instructed
        while current > 0 and self.heap[current] < self.heap[self.get_parent(current)]:
        # the line above here is very crucial because we want to compare the value at the current index whether its value is or not greater than the value of its parent. If it is, we have to swap
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)
        self.size += 1
    # In simple words, the purpose of the sink down operation is to maintain the heap property after an element is removed or its priority is decreased.
    def sink_down(self, index):
        smallest = index
        while True: 
            left = self.get_left_child(index)
            right = self.get_right_child(index)
            
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                return
def main():
    minheap = MinHeap()
    minheap.insert(99)
    minheap.insert(72)
    minheap.insert(61)
    minheap.insert(58)
    print(minheap.heap)
    minheap.insert(100)
    print('After inserting 100: ', end = '')
    print(minheap.heap)
    minheap.insert(75)
    print('After inserting 75: ', end = '')
    print(minheap.heap)
    minheap.remove_root()
    print('After removing root: ', end = '')
    print(minheap.heap)
    minheap.remove_root()
    print('After removing root: ', end = '')
    print(minheap.heap)
if __name__ == "__main__":
    main()
