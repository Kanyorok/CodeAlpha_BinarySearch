def binary_search_range(start, end):
    if start > end:
        return []

    mid = (start + end) // 2
    if mid % 2 != 0:
        mid += 1  # Checks that the number is even

    result = [mid]

    left_range = binary_search_range(start, mid - 2)
    right_range = binary_search_range(mid + 2, end)

    result = left_range + result + right_range

    return result


start = 0
end = 20
result = binary_search_range(start, end)
print(result)
