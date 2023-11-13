import math
import os
import sys
from analyzer.size_analyzer import SizeAnalyzer


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

    if os.path.isfile(path):
        analyze_file(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                analyze_file(os.path.join(root, file))
    else:
        print(f"{path} is not a valid file or directory")

def analyze_file(file_path):
    analyzer = SizeAnalyzer()
    size_info = analyzer.analyze_size(file_path)
    size_info = [convert_size(size) for size in size_info]  # Convert each size
    print(f"Size information for {file_path}:")
    print(size_info)


if __name__ == "__main__":
    main()
