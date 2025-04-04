def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            # Read the content of the file
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Write the modified content to the new file
            outfile.write(modified_content)
        
        print(f"File '{input_file}' has been modified and saved as '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file name
    output_file = "output.txt"  # Replace with your desired output file name
    modify_file(input_file, output_file)