def check_substring(string, substring):
    if substring in string:
        return "Yes"
    else:
        return "No"

user_string = input("Enter a string: ")
user_substring = input("Enter a substring: ")
result = check_substring(user_string, user_substring)
print(f"Is '{user_substring}' present in the string? {result}")