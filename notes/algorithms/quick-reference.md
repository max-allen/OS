---
layout: page
title: DST Quick Reference
permalink: /dst-quick-reference/
---

# Data Structures Quick Reference

Common data structures, use cases, standard operations and associated time complexities:

##### Sections
1. [Arrays](#arrays)
2. [Linked Lists](#linked-lists)
3. [Stacks, Queues](#stacks-queues)

## Arrays

The fundamental [[contiguously-allocated]] data structure. These data records
are of fixed size. Consequently, each element can be located by its numeric
index. Arrays come in two flavors: **static** (fixed size), and **dynamic**.
Arrays offered first class by interpreted languages (e.g. JavaScript, Python)
are implemented dynamically.

**Use Cases**:
- [Stacks](#stacks-queues)
- [Queues](#stacks-queues)
- Graphs (Adjacency Lists)

**Advantages**:
- Constant time access to elements provided the index is known (efficient random
  access).
- Space efficient as it doesn't use pointers.
- Contiguous allocation allows for better memory locality and cache performance.

**Drawbacks**:
- Less efficient, complex insertion in comparison to Linked Lists.
- Overflow is possible when writing to or attempting to access static arrays.
- With large records, moving pointers instead of the items themselves is faster
  and easier.

**Standard Operations:**

| **Operation** | **Time Complexity** |
| -------- | -------- |
| **Access** | **O(1)** |
| **Update** | **O(1)** |
| **Insert / Remove** | **O(N)** |
| **Insert (Size Reached)** | **Amortized O(1) dynamic; O(N) static** |
| **Remove (End)** | **O(1)** |
| **Search** | **O(N)** |

## Linked Lists

The fundamental linked data structure. Unlike their [[contiguously-allocated]],
counterpart, [arrays](#arrays), memory is allocated dynamically,
and their elements consequently have no index or order beyond head and tail
nodes. Elements are connected by pointers, which represent the address of a
location in memory. Linked Lists most commonly come in two flavors: **singly**
and **doubly** linked. Linked lists are a specialized data structure that may or
may not have first class support in a language.

**Use Cases**:
- Stacks
- Queues
- Graphs (Adjacency Lists)

 **Advantages**:
- Unlike static arrays, overflow can never occur.
- Simple insertion and deletion.
- Work well with large records as moving pointers is easier and faster than
  moving the record itself.

**Drawbacks**:
- Inefficient random access given lack of indices.
- Pointers require space consumption.

**Standard Operations:**

| **Operation** | **Time Complexity** |
| -------- | -------- |
| **Access (head/tail)** | **O(1)** |
| **Access / Search (non-head/tail)** | **O(N)** |
| **Insert / Remove (head/tail)** | **O(1)** |
| **Insert / Remove before/after non-head/tail node** | **O(N)** |

- **Note:** Singly linked lists have no tail pointer, so access to final element
  is **O(N)**.

## Stacks, Queues

Stacks and Queues are collections of sequenced data that permit storage and
retrieval independent of content. These structures are distinguished by their
**retrieval order**:

- Stacks support _last-in, first-out_ (**LIFO**) order.
- Queues support _first-in, last-out_ (**FIFO**) order.

These structures can be implemented with [arrays](#arrays) or
[linked lists](#linked-lists). They are used less frequently than arrays;
languages may not offer first class support.

**Stack Use Cases**:

- [Call Stacks](https://en.wikipedia.org/wiki/Call_stack)
- Undo/Redo Operations
- Expression Evaluation
- Browser History


**Queue Use Cases**:

- Task Scheduling
- Batch Processing
- Event Handling (Browser)
- Message Buffering
- Web Servers

**Standard Operations:**

| **Operation** | **Time Complexity** |
| -------- | -------- |
| **Push / Enqueue** | **O(1)** |
| **Pop / Dequeue** | **O(1)** |
| **Peek** | **O(1)** |
| **Search** | **O(N)** |


---
#### References 📚
- [Algorithm Design Manual 2nd](https://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202)
- [Applications, Advantages, and Disadvantages of Stack (Geeks for Geeks)](https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-stack/)
- [Applications of Queue Data Structure (Geeks for Geeks)](https://www.geeksforgeeks.org/applications-of-queue-data-structure/)
- [Data Structures Crash Course (AlgoExpert)](https://www.algoexpert.io/data-structures)

