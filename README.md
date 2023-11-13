# Binary Size Analyzer

Binary Size Analyzer is a Python application that analyzes the size of a Linux binary program and its dependencies.

## Installation

To install the Binary Size Analyzer, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/username/binary-size-analyzer.git
```

2. Navigate to the project directory:

```bash
cd binary-size-analyzer
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To use the Binary Size Analyzer, run the `main.py` script with the path to the binary program as an argument:

```bash
export PYTHONPATH="${PYTHONPATH}:${PWD}"
python src/main.py /path/to/binary
```

The script will output the size of the binary program and its dependencies.

## Testing

To run the unit tests, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

Binary Size Analyzer is released under the MIT License.