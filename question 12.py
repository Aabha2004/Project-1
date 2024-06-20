def sum_of_digits_iterative(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    return total_sum

user_number = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits_iterative(user_number)}")