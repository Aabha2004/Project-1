def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    return lines

user_lines = read_lines()
print("\n".join(user_lines))