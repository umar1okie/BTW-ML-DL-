def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
            return contents
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")

def write_to_file(file_path, user_input):
    try:
        with open(file_path, 'w') as file:
            file.write(user_input)
            print(f"Successfully wrote to '{file_path}'.")
    except IOError:
        print(f"Error: An error occurred while writing to the file '{file_path}'.")

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            words = contents.split()
            word_count = len(words)
            print(f"The file '{file_path}' contains {word_count} words.")
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")

# Test reading from 'data.txt'
file_contents = read_file('data.txt')

# Test writing to 'output.txt'
user_input = input("Enter some text to write to 'output.txt': ")
write_to_file('output.txt', user_input)

# Test counting words in 'data.txt'
count_words('data.txt')
