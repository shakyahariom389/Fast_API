# Python & AI/ML Junior Engineer – Task 2 Answers

### Q1. Python Memory Management

Python uses **automatic memory management** handled by the **Python Memory Manager**.

**Key mechanisms:**

**1. Reference Counting**

* Each object maintains a reference count.
* When a variable references an object, the count increases.
* When the reference is deleted, the count decreases.
* When the reference count becomes **0**, Python frees the memory.

Example:

```python
a = [1,2,3]
b = a
del a
```

The object still exists because `b` still references it.

**2. Garbage Collection**
Reference counting cannot handle **circular references**.

Example:

```python
class A:
    pass

a = A()
b = A()

a.ref = b
b.ref = a
```
Python's **Garbage Collector (GC)** detects these cycles and removes them automatically.



##########################################
### Q2. Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) is a mutex that ensures only one thread executes Python bytecode at a time.

Purpose=====

* Prevents memory corruption
* Simplifies memory management

Problem======

* Limits performance of CPU-bound multithreaded programs.

Ways to Mitigate=======

1. Multiprocessing
2. AsyncIO
3. Use C extensions that release the GIL (NumPy)

Example using multiprocessing:=====

```python
from multiprocessing import Process

def task():
    print("Running task")

p = Process(target=task)
p.start()
p.join()
```



#################################
### Q3.  `__new__` vs `__init__`

| Feature | `__new__`            | `__init__`         |
| ------- | -------------------- | ------------------ |
| Purpose | Creates object       | Initializes object |
| Return  | Must return instance | Returns None       |

Example:

```python
class Example:

    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing instance")

obj = Example()
```

Output========

```
Creating instance
Initializing instance
```


### staticmethod vs classmethod

```python
class Example:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create(cls):
        return cls()
```

| Type         | Description                    |
| ------------ | ------------------------------ |
| staticmethod | No access to class or instance |
| classmethod  | Receives class reference       |




###############################
### Q4. Custom Context Manager

Using `__enter__` and `__exit__`:

```python
class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager("test.txt") as f:
    f.write("Hello World")
```

Using `contextlib`:

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering")
    yield
    print("Exiting")

with my_context():
    print("Inside context")
```




###################################
### Q5. Descriptors

Descriptors manage attribute access using:

* `__get__`
* `__set__`
* `__delete__`

Example validating positive integers:

```python
class PositiveInteger:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__['value'] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get('value', None)

class Product:
    price = PositiveInteger()

p = Product()
p.price = 10
print(p.price)
```





#############################
### Q6. Decorators with Arguments (Retry Decorator)

```python
import time

def retry(times):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    time.sleep(1)
            raise Exception("Function failed after retries")

        return wrapper

    return decorator


@retry(3)
def test():
    print("Trying operation")

test()
```





#################################
### Q7. Generators vs Iterators

| Feature  | Generator       | Iterator                  |
| -------- | --------------- | ------------------------- |
| Creation | `yield` keyword | `__iter__` + `__next__`   |
| Memory   | Lazy evaluation | Depends on implementation |

Example Generator:

```python
def count(n):
    for i in range(n):
        yield i

for num in count(5):
    print(num)
```

Generators are **memory efficient** because values are produced **on demand**.




#######################################################################################################################


# Section B: Data Structures & Design
### Q8. LRU Cache (O(1))
Uses:
* HashMap
* Doubly Linked List

Example using OrderedDict:

```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

Time Complexity: **O(1)**





############################
### Q9. Trie (Prefix Tree)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
```




########################################
### Q10. Heap Data Structure

A **heap** is a **complete binary tree**.

Types:

* Min Heap
* Max Heap

Min heap property:

```
Parent <= Children
```

Example using Python:

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)

print(heapq.heappop(heap))
```

Time Complexity:

* Insert → O(log n)
* Delete → O(log n)





####################################
### Q11. Insert Delete GetRandom O(1)

```python
import random

class RandomSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.nums[-1]

        self.nums[idx] = last
        self.pos[last] = idx

        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
```





############################
### Q12. Immutability

Immutable objects **cannot be modified after creation**.

Examples:

* int
* string
* tuple

Advantages:

* Thread safe
* Prevents race conditions
* Safer concurrency






#############################
### Q13. Consistent Hashing

Used in **distributed systems** to distribute data across nodes.

Concept:

* Data and servers are mapped onto a **hash ring**.
* When nodes are added/removed, minimal data moves.

Use Cases:

* Distributed caches
* Load balancing
* NoSQL databases




####################################################################################################

# Section C: Algorithms

### Q14. Kth Largest Element

```python
import heapq

def kthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

Complexity: **O(n log k)**




###################################
### Q15. Quick Sort

```python
def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)
```

Complexity:

* Average → O(n log n)
* Worst → O(n²)





################################
### Q16. Longest Substring Without Repeating Characters

```python
def longestSubstring(s):

    seen = {}
    left = 0
    max_len = 0

    for right, c in enumerate(s):

        if c in seen and seen[c] >= left:
            left = seen[c] + 1

        seen[c] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```






############################
### Q17. Cycle Detection in Graph

**Directed Graph**

* DFS with recursion stack

**Undirected Graph**

* Union Find






################################
### Q18. Topological Sorting

Used for:

* task scheduling
* dependency resolution

Algorithm: **Kahn's Algorithm**

Time Complexity:

```
O(V + E)
```




################################
### Q19. Number of Islands

```python
def numIslands(grid):

    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):

        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```







####################################
### Q20. Coin Change (Dynamic Programming)

```python
def coinChange(coins, amount):

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i-c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```




#####################################################################################################################

# Section D: Performance & Concurrency

### Q21. Threading vs Multiprocessing vs AsyncIO

| Type            | Best Use            |
| --------------- | ------------------- |
| Threading       | IO tasks            |
| Multiprocessing | CPU tasks           |
| AsyncIO         | High IO concurrency |







#################################
### Q22. AsyncIO Example

```python
import asyncio

async def task():
    await asyncio.sleep(2)
    print("Task completed")

async def main():
    await asyncio.gather(task(), task(), task())

asyncio.run(main())
```




####################################
### Q23. Profiling Python Applications

Tools:

* cProfile
* line_profiler
* memory_profiler

Example:

```python
import cProfile
cProfile.run("my_function()")
```

Optimization Techniques:

* caching
* async programming
* vectorization
* multiprocessing




#########################################################################

# Section E: System Design

### Q24. URL Shortener System Design

Components:

* Client
* API Server
* Database
* Cache
* Hash Generator

Flow:

```
Long URL → Hash Generator → Store in Database → Return Short URL
```

Example:

```
https://example.com/very-long-url
↓
https://short.ly/abc123
```




##########################################
### Q25. High Throughput Log Analytics System

Architecture:

```
Log Producers
      ↓
Message Queue (Kafka)
      ↓
Stream Processing (Spark / Flink)
      ↓
Storage (Elasticsearch)
      ↓
Dashboard (Kibana / Grafana)
```

Features:

* Real-time analytics
* Fault tolerance
* Horizontal scalability
* High ingestion rate
