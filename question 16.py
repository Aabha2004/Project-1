def char_frequency_naive(test_str):
    all_freq = {}
    for char in test_str:
        if char in all_freq:
            all_freq[char] += 1
        else:
            all_freq[char] = 1
    return all_freq

user_input = input("Enter a string: ")
result = char_frequency_naive(user_input)
print("Character frequencies:", result)