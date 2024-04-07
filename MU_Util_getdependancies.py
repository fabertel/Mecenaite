#get al libraries 

import os
import ast


directory = os.getcwd()


# Mapping of import names to PyPI package names
library_to_pypi = {
    'sklearn': 'scikit-learn',
    'PIL': 'Pillow',
    # Add more mappings as necessary
}

def extract_imports_from_file(file_path):
    """
    Extracts imported libraries from a Python file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        root = ast.parse(file.read(), filename=file_path)

    for node in ast.walk(root):
        if isinstance(node, ast.Import):
            for name in node.names:
                yield name.name.split('.')[0]
        elif isinstance(node, ast.ImportFrom):
            yield node.module.split('.')[0]

def list_python_files(directory):
    """
    List all Python files starting with 'MU' in the given directory.
    """
    for item in os.listdir(directory):
        if item.startswith('MU') and item.endswith('.py'):
            yield os.path.join(directory, item)

def main(directory):
    imported_libraries = set()
    for file_path in list_python_files(directory):
        imported_libraries.update(extract_imports_from_file(file_path))

    # Map to PyPI names and remove duplicates
    pypi_libraries = set(library_to_pypi.get(lib, lib) for lib in imported_libraries)

    # Generate the pip install command
    pip_install_command = f"pip install {' '.join(pypi_libraries)}"

    print(pip_install_command)

# Run the main function with your directory
main(directory)


futgvyoh jnbmo