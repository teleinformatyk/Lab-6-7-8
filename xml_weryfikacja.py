import xml.etree.ElementTree as ET
import os
import sys

def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error: Invalid XML syntax in file '{file_path}': {e}")
        sys.exit(1)

def verify_xml_syntax(file_path):
    try:
        ET.parse(file_path)
    except ET.ParseError as e:
        print(f"Error: Invalid XML syntax in file '{file_path}': {e}")
        sys.exit(1)
    else:
        print(f"The XML syntax in file '{file_path}' is valid.")

def main_task6():
    input_filename = input("Enter the input file name: ")

    file_path = find_file(input_filename)
    if file_path is None:
        print(f"File '{input_filename}' not found on the computer.")
        sys.exit(1)

    verify_xml_syntax(file_path)
    data = load_xml_file(file_path)
    print("Loaded XML data:", data)

if __name__ == '__main__':
    main_task6()
