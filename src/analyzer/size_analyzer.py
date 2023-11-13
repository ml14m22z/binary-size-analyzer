import os
from src.utils import helper


class SizeAnalyzer:
    def analyze_size(self, binary_path):
        # Check if the binary file exists
        if not os.path.isfile(binary_path):
            raise FileNotFoundError(f"The binary file {binary_path} does not exist.")
        
        # # Check if the file is a binary file
        # if not helper.is_binary(binary_path):
        #     raise ValueError(f"The file {binary_path} is not a binary file.")

        # Calculate the size of the binary file
        binary_size = helper.calculate_file_size(binary_path)

        # Find the dependencies of the binary file
        dependencies = helper.find_dependencies(binary_path)

        # Calculate the total size of the dependencies
        dependencies_size = sum(helper.calculate_file_size(dep) for dep in dependencies)

        return binary_size, dependencies_size
