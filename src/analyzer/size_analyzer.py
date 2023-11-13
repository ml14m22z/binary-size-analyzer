import os
from src.utils import helper


class SizeAnalyzer:
    def analyze_size(self, binary_path):
        # Check if the binary file exists
        if not os.path.isfile(binary_path):
            raise FileNotFoundError(f"The binary file {binary_path} does not exist.")
        
        # Calculate the size of the binary file
        binary_size = helper.calculate_file_size(binary_path)

        # Find the dependencies of the binary file
        dependencies = helper.find_dependencies(binary_path)

        # Prepare the result
        result = [[binary_path, binary_size]]

        # Calculate the size of each dependency and add it to the result
        for dep in dependencies:
            dep_size = helper.calculate_file_size(dep)
            result.append([dep, dep_size])

        return result
