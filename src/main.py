import math
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
        print("Usage: python main.py <binary_file>")
        sys.exit(1)

    binary_file = sys.argv[1]
    analyzer = SizeAnalyzer()
    size_info = analyzer.analyze_size(binary_file)
    size_info = [convert_size(size) for size in size_info]  # Convert each size

    print(f"Size information for {binary_file}:")
    print(size_info)


if __name__ == "__main__":
    main()
