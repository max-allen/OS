---
layout: page
title: Contiguously Allocated Data Structures
permalink: /contiguously-allocated/
published: false
---

# Contiguously Allocated Data Structures

- _Continously-allocated structures_ are composed of single slabs of memory.
  - Examples: arrays, matrices, heaps, hash tables

- _Linked data structures_ are composed of distinct chunks of memory bound by _pointers_.
  - Examples: lists, trees, adjacency lists

## Arrays

Fundamental contiguously-allocated data structure. Fixed size data records such
that each element can be located by its _index_ (address).

### Advantages:

- Constant time access (given index): Each index maps to a particular memory
  address, so data can be accessed arbitrarily given the index is known.

- Space efficiency: Consist purely of data. No space is wasted with pointers.

- Memory locality: Physical continuity between successive data accesses exploits
  high-speed cache memory on modern computer architectures

A downside of arrays is that their size can't be adjusted during program
execution; the program will fail when adding a record beyond the number
allocated. Dynamic arrays provide a means of enlarging arrays as needed, but we
should consider what this entails:

Suppose we have an array of size 1, and double its size from **m** to **2m**
when we run out of space. The doubling process would consist of:
  - allocating a new array of size 2m
  - copying the contents of the old array to the new one
  - returning the space used by the old array to the storage allocation system

How many times will an element be recopied given _n_ insertions? The first
element will be recopied following the first, second, fourth, eighth insertions
and so on. _log sub2 n_ doublings will be required to reach n positions.

Most elements won't be subject to this. On average, element will move
_2n_ times, which maintains the time complexity of static arrays.

Using dynamic arrays, we lose the guarantee of constant time array access.
Queries will be fast except for those that trigger array doubling. We get an
_amortized_ guarantee that the _nth_ array access will complete quickly enough
that the total effort expended remains _O(n)_.

#### References
---
- [Algorithm Design Manual 2nd](https://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202)


