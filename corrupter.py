import os
import random
import tkinter as tk
from tkinter import filedialog

def corrupt_file(file_path, corruption_percentage):
    # Read the original file in binary mode
    with open(file_path, 'rb') as file:
        data = bytearray(file.read())

    # Calculate the number of bytes to corrupt
    num_bytes_to_corrupt = int(len(data) * (corruption_percentage / 100))
    print(f"Corrupting {num_bytes_to_corrupt} bytes out of {len(data)} bytes")

    # Randomly corrupt the specified number of bytes
    for _ in range(num_bytes_to_corrupt):
        index = random.randint(0, len(data) - 1)
        data[index] = random.randint(0, 255)

    # Create the new filename with "_CORRUPTED" suffix
    directory, filename = os.path.split(file_path)
    basename, extension = os.path.splitext(filename)
    new_filename = f"{basename}_CORRUPTED{extension}"
    new_filepath = os.path.join(directory, new_filename)

    # Write the corrupted data to the new file
    with open(new_filepath, 'wb') as file:
        file.write(data)

    print(f"Successfully created the corrupted file: {new_filepath}")

if __name__ == "__main__":
    # Initialize Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select the file
    file_path = filedialog.askopenfilename(
        title="Select a file to corrupt",
        filetypes=[("literally any file", "*.*")]
    )

    # Check if the user selected a file
    if not file_path:
        print("No file selected.")
    else:
        try:
            # Ask for the corruption percentage
            corruption_percentage = float(input("Enter the corruption percentage (0-100): "))
            if not 0 <= corruption_percentage <= 100:
                print("Invalid percentage. Please enter a value between 0 and 100.")
            else:
                # Corrupt the file
                corrupt_file(file_path, corruption_percentage)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
