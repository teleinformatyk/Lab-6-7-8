import yaml
import os
import sys

def load_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error: Invalid YAML syntax in file '{file_path}': {e}")
            sys.exit(1)

def verify_yaml_syntax(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML syntax in file '{file_path}': {e}")
        sys.exit(1)
    else:
        print(f"The YAML syntax in file '{file_path}' is valid.")

def main_task4():
    input_filename = input("Enter the input file name: ")

    file_path = find_file(input_filename)
    if file_path is None:
        print(f"File '{input_filename}' not found on the computer.")
        sys.exit(1)

    verify_yaml_syntax(file_path)
    data = load_yaml_file(file_path)
    print("Loaded YAML data:", data)

if __name__ == '__main__':
    main_task4()
