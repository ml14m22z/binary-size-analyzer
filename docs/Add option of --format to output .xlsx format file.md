# Add option of --format to output .xlsx format file

```markdown
    ml14m22z: Add option of `--format` to output `.xlsx` format file

    GitHub Copilot: Sure, to add an option for `--format` to output `.xlsx` format file, we need to do the following:

    1. Add a new argument to the argument parser for the `--format` option.
    2. Create a new function `save_to_excel` to save the data to an Excel file.
    3. In the `main` function, check the format argument and call the appropriate function to save the data.

    Here is the updated code:

    ```python
    import argparse
    import os
    import sys
    from analyzer.size_analyzer import SizeAnalyzer
    import json
    import pandas as pd
    from src.utils import helper

    def save_to_json(data, filename='output.json'):
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def save_to_excel(data, filename='output.xlsx'):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

    def main():
        parser = argparse.ArgumentParser(description='Analyze file sizes.')
        parser.add_argument('path', help='The file or directory to analyze.')
        parser.add_argument('--filter', nargs='*', default=[], help='The file extensions to exclude.')
        parser.add_argument('--format', choices=['json', 'xlsx'], default='json', help='The output format.')
        args = parser.parse_args()

        path = args.path
        filters = args.filter
        data = []

        if os.path.isfile(path):
            if helper.is_binary(path) and not any(path.endswith(f) for f in filters):
                data.append(analyze_file(path))
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if helper.is_binary(os.path.join(root, file)) and not any(file.endswith(f) for f in filters):
                        data.append(analyze_file(os.path.join(root, file)))
        else:
            print(f"{path} is not a valid file or directory")

        if args.format == 'json':
            save_to_json(data)
        elif args.format == 'xlsx':
            save_to_excel(data)

    def analyze_file(file_path):
        analyzer = SizeAnalyzer()
        size_info = analyzer.analyze_size(file_path)
        return size_info


    if __name__ == "__main__":
        main()
    ```

    This code uses the `pandas` library to save data to an Excel file. If you haven't installed it yet, you can do so with `pip install pandas openpyxl`.
```