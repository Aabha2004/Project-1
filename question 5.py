def main():
    user_input = input("Enter a string: ")
    with open("user_input.txt", "w") as file:
        file.write(user_input)
    print(f"String '{user_input}' has been written to 'user_input.txt'.")

if __name__ == "__main__":
    main()