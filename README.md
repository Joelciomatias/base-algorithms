## base-algorithms

### Matrix

#### 36. Valid Sudoku
É possível encontrar submatrizes (3x3) em uma matriz 9x9 dividindo o índice por 3.  
Exemplo: `4 / 3 == 1` (submatriz 1).

---

### Backtracking

**Backtracking** é uma técnica de resolução de problemas onde construímos uma solução incrementalmente, retrocedemos quando uma solução parcial falha e exploramos outras possibilidades. É frequentemente usada em problemas como:
- Geração de permutações
- Solução de Sudoku
- Problema das N-Rainhas

#### **Conceitos-chave no Backtracking:**
- **Base Case:** Quando o caminho atual representa uma solução válida, a recursão é interrompida.
- **Constraints:** Verifica-se se a escolha atual é válida antes de prosseguir.
- **Exploration:** Explora-se todas as opções válidas de forma recursiva.
- **Backtracking:** Desfaz a escolha para explorar outras possibilidades.

---

### Heap

Um **Heap** é uma estrutura de dados baseada em **árvore binária** que mantém a propriedade de heap, podendo ser de dois tipos:

- **Max-heap:** O valor de cada nó pai é **maior ou igual** ao valor de seus filhos. O maior elemento sempre está na raiz.
- **Min-heap:** O valor de cada nó pai é **menor ou igual** ao valor de seus filhos. O menor elemento sempre está na raiz.

A implementação mais comum de heaps é utilizando **arrays** para armazenar a árvore de forma eficiente.

#### **Casos de Uso Hoje em Dia**
- **Filas de prioridade** (ex: gerenciadores de tarefas, roteamento de redes).
- **Algoritmos de ordenação**, como **HeapSort** \(O(n \log n)\).
- **Sistemas de agendamento**, como escalonamento de processos em SO.
- **Algoritmos de caminho mínimo**, como **Dijkstra** para encontrar a menor rota em mapas.
- **Streaming de dados**, como encontrar os **k maiores elementos** em um fluxo contínuo de dados.

#### **Exemplo de Implementação em Python**
```python
import heapq

# Criando um min-heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)

print("Menor elemento:", heapq.heappop(heap))  # Remove e retorna o menor elemento (1)

# Convertendo uma lista existente em um heap
nums = [10, 2, 14, 7, 5]
heapq.heapify(nums)

print("Menor el após heapify:", heapq.heappop(nums))  # Retorna 2
```

