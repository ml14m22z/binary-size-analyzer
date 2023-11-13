import sys
from analyzer.size_analyzer import SizeAnalyzer


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <binary_file>")
        sys.exit(1)

    binary_file = sys.argv[1]
    analyzer = SizeAnalyzer()
    size_info = analyzer.analyze_size(binary_file)

    print(f"Size information for {binary_file}:")
    print(size_info)


if __name__ == "__main__":
    main()
