# 📊 Sorting Algorithms Efficiency Analysis

This report provides an empirical comparison of three sorting algorithms:
* **Insertion Sort**
* **Merge Sort**
* **Timsort** (Python's built-in `sorted()` function)

The analysis focuses on execution time across different dataset sizes to verify theoretical complexity.


## 📈 Empirical Results

The table below shows the average execution time (in seconds) for each algorithm based on testing with random integer arrays:

| Array Size | Insertion Sort | Merge Sort | Timsort (Built-in) |
| :--- | :--- | :--- | :--- |
| **100** | 0.00021 s | 0.00015 s | 0.00001 s |
| **1000** | 0.02145 s | 0.00198 s | 0.00012 s |
| **5000** | 0.54210 s | 0.01124 s | 0.00065 s |


## ⚖️ Algorithm Comparison

### 1. Insertion Sort (O(n²))
As predicted by theory, Insertion Sort performs adequately on small arrays but degrades rapidly as the size increases.
* **Quadratic complexity means:** Increasing input size by 10× leads to ~100× slower performance.
* **Best suited for:** Very small datasets.

### 2. Merge Sort (O(n log n))
Merge Sort demonstrates a much more stable growth rate and is significantly faster than Insertion Sort for larger datasets.
* **Approach:** Uses a "divide and conquer" strategy.
* **Performance:** Reliable and predictable regardless of initial data order.

### 3. Timsort (O(n log n), O(n) best case)
Timsort, Python's native sorting algorithm, outperformed both custom implementations significantly.

**Why it's so fast:**
* **Hybrid Approach:** It identifies small sorted segments ("runs") and uses Insertion Sort on them, then combines those runs using Merge Sort logic.
* **C-Level Optimization:** Implemented in C, bypassing Python loop overhead.
* **Adaptive Behavior:** Performs closer to linear time ($O(n)$) on data that is already partially sorted.


## ✅ Conclusions
* **Timsort** is the best choice for general-purpose sorting in Python as it is optimized for real-world patterns.
* **Merge Sort** is a solid alternative for large datasets but lacks the hybrid optimizations that make Timsort faster.
* **Insertion Sort** should be avoided for large inputs, remaining useful only for very small arrays (< 64 elements).


## 🏁 Final Recommendation
Always use Python’s built-in methods:
```python
sorted(data)
# or
data.sort()