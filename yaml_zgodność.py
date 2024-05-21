import yaml
import os
import sys

def write_yaml_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

def main_task5():
    data = {"key": "value"}  # Tutaj podaj dane, które chcesz zapisać do pliku YAML
    output_filename = input("Enter the output file name: ")
    output_path = f"./{output_filename}"  # Możesz zmienić ścieżkę według potrzeb

    write_yaml_file(output_path, data)
    print(f"Data successfully saved to '{output_path}'.")

if __name__ == '__main__':
    main_task5()
