def calculate_age(birth_year):
    current_year = 2024  # You can update this to the current year
    age = current_year - birth_year
    return age

try:
    user_birth_year = int(input("Enter your birth year: "))
    user_age = calculate_age(user_birth_year)
    print(f"You are approximately {user_age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid birth year (e.g., 1990).")