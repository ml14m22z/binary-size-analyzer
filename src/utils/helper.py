import os
import subprocess


def read_binary_file(file_path):
    """
    This function reads a binary file and returns its content.
    """
    with open(file_path, 'rb') as file:
        return file.read()


def calculate_file_size(file_path):
    """
    This function calculates the size of a file in bytes.
    """
    return os.path.getsize(file_path)


def find_dependencies(file_path):
    """
    This function finds the dependencies of a binary file.

    Args:
        file_path (str): The path to the binary file.

    Returns:
        list: A list of dependencies for the binary file.
    """
    try:
        output = subprocess.check_output(['ldd', file_path], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        # If ldd fails, return an empty list
        return []

    dependencies = []
    for line in output.decode().split('\n'):
        if '=>' in line:
            dependency = line.split('=>')[0].strip()
            if dependency:
                dependencies.append(dependency)

    return dependencies

def is_binary(file_path):
    """
    Check if a file is binary.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file is binary, False otherwise.
    """
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(1024), b''):
            if b'\0' in chunk:  # Null bytes are a good indicator of binary files
                return True
    return False
