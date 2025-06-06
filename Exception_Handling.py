def read_numbers(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue  # skip empty lines
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid number: {line}")
    except FileNotFoundError:
        print("File not found.")
    finally:
        print('The of program')
    return numbers
# Example usage
nums = read_numbers("numbers.txt")
print("Numbers:", nums)
