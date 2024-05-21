import argparse
import os
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='File format converter')
    parser.add_argument('input_filename', type=str, help='Input file name')
    parser.add_argument('--output_format', '-o', choices=['json', 'xml', 'yaml'], default='json', help='Output format (default: json)')
    parser.add_argument('--output_path', '-p', type=str, help='Output file path (default: same directory as input file)')
    return parser.parse_args()

def main():
    args = parse_arguments()

    input_filename = args.input_filename
    output_format = args.output_format
    output_path = args.output_path


if __name__ == '__main__':
    main_task1()
