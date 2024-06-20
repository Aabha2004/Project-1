def find_min_max(numbers):
    if not numbers:
        return None, None  # Empty list case

    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

