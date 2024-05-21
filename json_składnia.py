import json
import os
import sys

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON syntax in file '{file_path}': {e}")
            sys.exit(1)

def verify_json_syntax(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON syntax in file '{file_path}': {e}")
        sys.exit(1)
    else:
        print(f"The JSON syntax in file '{file_path}' is valid.")

def main_task2():
    input_filename = input("Enter the input file name: ")

    file_path = find_file(input_filename)
    if file_path is None:
        print(f"File '{input_filename}' not found on the computer.")
        sys.exit(1)

    verify_json_syntax(file_path)
    data = load_json_file(file_path)
    print("Loaded JSON data:", data)

if __name__ == '__main__':
    main_task2()
