import timeit
import random


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    middle = len(numbers) // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def compare_sort():
    sizes = [100, 1000, 5000]

    print(f"{'Algorithm':<18} | {'Size':<6} | {'Time (seconds)':<15}")
    print("-" * 45)

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]

        if size <= 5000:
            time_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=5)
            print(f"{'Insertion Sort':<18} | {size:<6} | {time_insertion / 5:.6f}")

        time_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=5)
        print(f"{'Merge Sort':<18} | {size:<6} | {time_merge / 5:.6f}")

        time_timsort = timeit.timeit(lambda: sorted(data.copy()), number=5)
        print(f"{'Timsort (sorted)':<18} | {size:<6} | {time_timsort / 5:.6f}")
        print("-" * 45)


if __name__ == "__main__":
    compare_sort()