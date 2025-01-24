# PDF Compressor

**A Python-based tool to compress and optimize PDF files using Ghostscript.**

## Features
- **Compress PDFs**: Reduce file size while maintaining quality.
- **Flexible Compression Quality**: Choose between `screen`, `ebook`, `printer`, and `prepress` settings.
- **Cross-Platform**: Works seamlessly on macOS, Windows, and Linux.

## Requirements
1. **Python** (3.7 or later)
2. **Ghostscript**
    - macOS:
      ```bash
      brew install ghostscript
      ```
    - Windows:
      Download and install Ghostscript from [official site](https://www.ghostscript.com/).
    - Linux:
      ```bash
      sudo apt-get install ghostscript
      ```

## Installation
Install required Python libraries:
```bash
pip install Pillow
```

## Usage

### Script Overview
The script provides an easy way to compress PDFs by leveraging Ghostscript's powerful features.

### Example Code
Below is the main script:
```python
import subprocess
import os

def compress_pdf(input_file, output_file, quality="ebook"):
    """
    Compress a PDF file using Ghostscript.

    Parameters:
        input_file (str): Path to the input PDF file.
        output_file (str): Path to save the compressed PDF file.
        quality (str): Compression quality. Options: 'screen', 'ebook', 'printer', 'prepress'.
                       Default is 'ebook'.

    Raises:
        Exception: If Ghostscript fails to compress the file.
    """
    # Define Ghostscript command and options
    gs_command = [
        "gs",  # Command for Ghostscript
        "-sDEVICE=pdfwrite",  # Output device
        f"-dPDFSETTINGS=/{quality}",  # Quality setting
        "-dCompatibilityLevel=1.4",  # Ensure compatibility with older PDF versions
        "-dNOPAUSE",  # No pause for user intervention
        "-dQUIET",  # Suppress output messages
        "-dBATCH",  # Exit after processing
        f"-sOutputFile={output_file}",  # Output file path
        input_file,  # Input file path
    ]

    try:
        # Run Ghostscript command
        subprocess.run(gs_command, check=True)
        print(
            f"Compressed PDF saved as '{output_file}'. "
            f"Original size: {os.path.getsize(input_file) / 1024 / 1024:.2f} MB, "
            f"Compressed size: {os.path.getsize(output_file) / 1024 / 1024:.2f} MB"
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ghostscript compression failed: {e}")
    except FileNotFoundError:
        raise Exception(
            "Ghostscript is not installed or not found. Please install Ghostscript and try again."
        )

if __name__ == "__main__":
    # Example usage
    input_pdf = "./input.pdf"  # Replace with your input PDF file path
    output_pdf = "output.pdf"  # Replace with your desired output file path

    # Ensure the input file exists
    if not os.path.exists(input_pdf):
        print(f"Input file '{input_pdf}' not found.")
    else:
        try:
            compress_pdf(
                input_pdf, output_pdf, quality="ebook"
            )  # Use 'screen' for more compression
        except Exception as e:
            print(e)
```

### Steps to Compress a PDF
1. Place the PDF you want to compress in the project directory.
2. Update the `input_pdf` and `output_pdf` variables in the script to specify your input and output file paths.
3. Run the script:
    ```bash
    python pdf_compressor.py
    ```
4. The compressed file will be saved as specified in the `output_pdf` variable.

### Command-Line Arguments (Optional)
- `--input`: Specify the input file path.
- `--output`: Specify the output file path.
- `--quality`: Set compression quality (`screen`, `ebook`, `printer`, `prepress`).

Example:
```bash
python pdf_compressor.py --input input.pdf --output compressed.pdf --quality screen
```

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, please email [bernnard.owusuappiah@gmail.com](mailto:bernnard.owusuappiah@gmail.com).
