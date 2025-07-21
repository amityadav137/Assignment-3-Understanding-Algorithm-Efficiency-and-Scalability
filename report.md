# Assignment 3 Report: Understanding Algorithm Efficiency and Scalability

## Overview
This report explores two key algorithms: **Randomized Quicksort** and **Hashing with Chaining**. Through theoretical analysis and practical experimentation, we examine how these algorithms behave under various input conditions and how efficiently they scale.



## Part 1: Randomized Quicksort

### Implementation
The Randomized Quicksort algorithm implemented here chooses the pivot uniformly at random for each recursive call. This helps avoid the worst-case performance that deterministic strategies might suffer when faced with already sorted or reverse-sorted data.

### Theoretical Analysis
- **Time Complexity (Average Case)**: \( O(n \log n) \)
- **Justification**: The expected number of comparisons can be modeled using indicator random variables. On average, the pivot splits the array approximately in half, leading to the recurrence:

  \[
  T(n) = T(i) + T(n - i - 1) + O(n)
  \]

  Solving this gives \( T(n) = O(n \log n) \).

### Empirical Comparison
We compared Randomized Quicksort with Deterministic Quicksort (pivot = first element) across:
- Random arrays
- Sorted arrays
- Reverse-sorted arrays
- Arrays with repeated elements

**Findings**:
- Randomized Quicksort outperforms deterministic in worst-case scenarios like sorted/reversed data.
- Performance gap increases with input size due to pivot selection strategy.



## Part 2: Hashing with Chaining

### Implementation
A hash table is implemented using separate chaining to resolve collisions. Basic operations include:
- **Insert**
- **Search**
- **Delete**

We use Python’s built-in `hash()` and modulo operation for hashing.

### Theoretical Analysis
- **Expected Time** (under Simple Uniform Hashing):
  - Insert, Search, Delete: \( O(1 + lpha) \)
  - Where \( lpha \) is the **load factor** = \( rac{n}{m} \) (n: elements, m: buckets)

- **Performance Notes**:
  - Low load factor improves performance.
  - Dynamic resizing helps maintain efficiency as data grows.

---

## Conclusion

- **Randomized Quicksort** shows better average performance and robustness across input types.
- **Hashing with Chaining** is an effective collision-handling strategy when supported by a good hash function and resizing mechanism.

These implementations and analyses illustrate how theoretical understanding supports practical software development decisions.
