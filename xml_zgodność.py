import xml.etree.ElementTree as ET
import os
import sys

def write_xml_file(file_path, data):
    root = ET.Element("root")


    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

def main_task7():
    data = {"key": "value"}
    output_filename = input("Enter the output file name: ")
    output_path = f"./{output_filename}"

    write_xml_file(output_path, data)
    print(f"Data successfully saved to '{output_path}'.")

if __name__ == '__main__':
    main_task7()
