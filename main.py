def binary_search_range(start_num, end_num):
    if start_num > end_num:
        return []

    mid = (start_num + end_num) // 2
    if mid % 2 != 0:
        mid += 1  # Checks that the number is even

    result = [mid]

    left_range = binary_search_range(start_num, mid - 2)
    right_range = binary_search_range(mid + 2, end_num)

    result = left_range + result + right_range

    return result


start = 0
end = 20
result = binary_search_range(start, end)
print(result)
