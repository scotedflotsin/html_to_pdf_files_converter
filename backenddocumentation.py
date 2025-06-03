import os
import pdfkit
from PyPDF2 import PdfMerger
from pathlib import Path
import platform
import shutil

# Path to your HTML files
HTML_DIR = "html_files"  # folder containing HTML files
TEMP_PDF_DIR = "temp_pdfs"
FINAL_OUTPUT_NAME = "MergedOutput.pdf"

# Detect Downloads folder cross-platform
def get_downloads_path():
    if platform.system() == "Windows":
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:
        return os.path.join(Path.home(), "Downloads")

def convert_html_to_pdf(input_path, output_path):
    pdfkit.from_file(input_path, output_path)

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def main():
    # Create temp folder
    os.makedirs(TEMP_PDF_DIR, exist_ok=True)

    # Get all HTML files (sorted to preserve sequence)
    html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith(".html")])
    pdf_paths = []

    for idx, html_file in enumerate(html_files):
        input_path = os.path.join(HTML_DIR, html_file)
        output_pdf = os.path.join(TEMP_PDF_DIR, f"{idx+1}_{html_file}.pdf")
        convert_html_to_pdf(input_path, output_pdf)
        pdf_paths.append(output_pdf)

    # Merge all PDFs
    final_pdf_path = os.path.join(get_downloads_path(), FINAL_OUTPUT_NAME)
    merge_pdfs(pdf_paths, final_pdf_path)

    # Clean temp
    shutil.rmtree(TEMP_PDF_DIR)

    print(f"\n✅ Merged PDF saved to: {final_pdf_path}")

if __name__ == "__main__":
    main()
