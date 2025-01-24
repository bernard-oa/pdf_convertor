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
