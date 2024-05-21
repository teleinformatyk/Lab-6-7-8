import json
import os
import sys

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def main_task3():
    data = {"key": "value"}  # Tutaj podaj dane, które chcesz zapisać do pliku JSON
    output_filename = input("Enter the output file name: ")
    output_path = f"./{output_filename}"  # Możesz zmienić ścieżkę według potrzeb

    write_json_file(output_path, data)
    print(f"Data successfully saved to '{output_path}'.")

if __name__ == '__main__':
    main_task3()
