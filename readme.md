# Assignment 3: Algorithm Efficiency and Scalability

## How to Run the Code

1. **Clone or Download the Repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Install Required Libraries**:
   Make sure you have Python 3.x installed along with `matplotlib`:
   ```bash
   pip install matplotlib
   ```

3. **Run Sorting Algorithm Benchmark**:
   ```bash
   python sort_test.py
   ```

4. **Test Hash Table Operations**:
   ```bash
   python hash_table_test.py
   ```



## Summary of Findings

- **Randomized Quicksort**:
  - Performs better on average than Deterministic Quicksort, especially on sorted, reverse-sorted, and repeated data arrays.
  - Average-case time complexity: `O(n log n)` due to random pivot selection.

- **Hash Table with Chaining**:
  - Efficient for insert, search, and delete operations with expected time `O(1 + α)` under simple uniform hashing.
  - Performance depends on load factor and effectiveness of the hash function.
