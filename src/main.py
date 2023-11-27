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
    df['binary_path'] = df['binary_path'].apply(lambda x: os.path.basename(x))

    def extract_deps_size(deps):
        return helper.convert_size(sum([helper.recover_size(dep['dep_size']) for dep in deps]))
    
    df['deps_size'] = df['deps'].apply(extract_deps_size)

    def extract_file_names(deps):
        return [os.path.basename(dep['dep']) for dep in deps]

    all_deps = list(set(df['deps'].apply(extract_file_names).sum()))

    df['deps'] = df['deps'].apply(extract_file_names)

    for dep in all_deps:
        df[dep] = df['deps'].apply(lambda x: '√' if dep in x else '')

    df = df.drop(columns=['deps'])
    df.to_excel(filename, index=True, sheet_name='binary')

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
