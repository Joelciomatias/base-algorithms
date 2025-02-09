class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        """Sobe o elemento para manter a propriedade da Min Heap."""
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        """Desce o elemento para manter a propriedade da Min Heap."""
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def push(self, value):
        """Adiciona um novo valor na heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove e retorna o menor elemento da heap."""
        if not self.heap:
            raise IndexError("Heap vazia!")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move o último elemento para a raiz
        self._heapify_down(0)  # Ajusta a heap
        return root

    def peek(self):
        """Retorna o menor elemento sem remover."""
        if not self.heap:
            return None
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

# Exemplo de uso
heap = MinHeap()
heap.push(10)
heap.push(4)
heap.push(15)
heap.push(1)
heap.push(7)

print("Min Heap:", heap)  # Deve estar ordenada como Min Heap
print("Menor elemento removido:", heap.pop())  # Deve remover 1
print("Min Heap após remoção:", heap)
print("Menor elemento atual:", heap.peek())  # Deve mostrar 4
