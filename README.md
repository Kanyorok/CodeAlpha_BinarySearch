# CodeAlpha_BinarySearch
It is a system that takes any input starting from 0 to any range specified and displays a range of numbers with a difference of two.

## Challenge description

### Binary Search

The binary search system creates a binary search algorithm in Python that generates a range of numbers with a difference of two.

In this code, binary_search_range is a recursive function that generates a list of numbers in the specified range [start, end] with a difference of two. 
The function ensures that the midpoint is even, and it recursively divides the range into two parts until it covers the entire specified range.

You can change the start and end variables to specify the desired range, and the function will return a list of numbers with a difference of two within that range.

#### Examples

```python
print(result_output)
# => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```