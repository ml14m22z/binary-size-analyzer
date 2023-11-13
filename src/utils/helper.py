import os


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
    For simplicity, let's assume it returns an empty list for now.
    """
    return []

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
