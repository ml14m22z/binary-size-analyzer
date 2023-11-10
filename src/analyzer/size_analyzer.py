import os
from src.utils import helper

class SizeAnalyzer:
    def __init__(self, binary_path):
        self.binary_path = binary_path

    def analyze_size(self):
        # Check if the binary file exists
        if not os.path.isfile(self.binary_path):
            raise FileNotFoundError(f"The binary file {self.binary_path} does not exist.")

        # Calculate the size of the binary file
        binary_size = helper.calculate_file_size(self.binary_path)

        # Find the dependencies of the binary file
        dependencies = helper.find_dependencies(self.binary_path)

        # Calculate the total size of the dependencies
        dependencies_size = sum(helper.calculate_file_size(dep) for dep in dependencies)

        return binary_size, dependencies_size