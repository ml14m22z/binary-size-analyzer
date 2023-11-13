import math
import os
import sys
from analyzer.size_analyzer import SizeAnalyzer
import csv

def save_to_csv(data, filename='output.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Path', 'Size'])  # Write header
        for row in data:
            writer.writerow(row)

def convert_size(size_bytes):
    """
    Convert a file size in bytes to a human-readable format.

    Args:
        size_bytes (int): The file size in bytes.

    Returns:
        str: The file size in a human-readable format.
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    data = []
    
    if os.path.isfile(path):
        data.append(analyze_file(path))
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                data.append(analyze_file(os.path.join(root, file)))
    else:
        print(f"{path} is not a valid file or directory")

    save_to_csv(data)

def analyze_file(file_path):
    analyzer = SizeAnalyzer()
    size_info = analyzer.analyze_size(file_path)
    size_info = [convert_size(size) for size in size_info]  # Convert each size
    print(f"Size information for {file_path}:")
    print(size_info)
    return (file_path, size_info)


if __name__ == "__main__":
    main()
