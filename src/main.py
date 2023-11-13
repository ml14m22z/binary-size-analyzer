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

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    data = []

    if os.path.isfile(path):
        data.extend(analyze_file(path))
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                data.extend(analyze_file(os.path.join(root, file)))
    else:
        print(f"{path} is not a valid file or directory")

    save_to_csv(data)

def analyze_file(file_path):
    analyzer = SizeAnalyzer()
    size_info = analyzer.analyze_size(file_path)
    return size_info


if __name__ == "__main__":
    main()
