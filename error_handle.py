def modify_file_content(content):
    """
    Modify the content of the file.
    Example modification: Convert text to uppercase.
    """
    return content.upper()

def main():
    # Prompt the user for the input file name
    input_file = input("Enter the name of the file to read: ").strip()

    try:
        # Attempt to open and read the input file
        with open(input_file, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the file name and try again.")
        return
    except IOError:
        print(f"Error: Cannot read the file '{input_file}'. Please check the file permissions.")
        return

    # Modify the file content
    modified_content = modify_file_content(content)

    # Generate output filename
    output_file = f"modified_{input_file}"

    try:
        # Attempt to write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Modified content written to '{output_file}'.")
    except IOError:
        print(f"Error: Could not write to '{output_file}'. Please check the file permissions.")

if __name__ == "__main__":
    main()

# This code handles file reading and writing errors gracefully, providing user-friendly messages.
# It also includes a function to modify the file content, which can be customized as needed.