def convert_to_title_case(input_string):
    return input_string.title()

user_input = input("Enter a string: ")
title_case_result = convert_to_title_case(user_input)
print(f"Title case version: {title_case_result}")