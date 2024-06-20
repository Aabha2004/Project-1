user_string = input("Enter a string: ")
user_prefix = input("Enter a prefix: ")
user_suffix = input("Enter a suffix: ")

if check_prefix_suffix(user_string, user_prefix, user_suffix):
    print(f"The string '{user_string}' starts with '{user_prefix}' and ends with '{user_suffix}'.")
else:
    print(f"The string '{user_string}' does not match the specified prefix and suffix.")