# Newspaper OCR Pre-Processing and OCRmyPDF Workflow

This project processes a newspaper PDF containing images by first enhancing the quality of each page while preserving color, then applying OCR to add an invisible text layer. This enables users to select and search the text from the newspaper without altering its original appearance.

## Features

- **High-Quality Conversion:**  
  Converts PDF pages to high-resolution images (300 DPI) to boost OCR accuracy.

- **Color Preservation:**  
  Applies contrast and brightness adjustments along with denoising on the original color images, avoiding grayscale conversion.

- **OCR Processing:**  
  Uses OCRmyPDF to add an invisible text layer, making the final PDF searchable and selectable.

- **Automatic Deskewing & Optimization:**  
  Corrects skewed scans and optimizes file size during OCR processing.

## Requirements

- **Python 3.x**  
- **Required Python Packages:**  
  - [ocrmypdf](https://ocrmypdf.readthedocs.io/en/latest/)
  - [pdf2image](https://pypi.org/project/pdf2image/)
  - [OpenCV (cv2)](https://opencv.org/)
  - [NumPy](https://numpy.org/)
  - [Pillow (PIL)](https://python-pillow.org/)

- **Poppler:**  
  Required by `pdf2image` to convert PDF pages to images.  
  - **macOS:** Install via Homebrew:  
    ```bash
    brew install poppler
    ```
  - **Ubuntu/Linux:**  
    ```bash
    sudo apt-get install poppler-utils
    ```

## How It Works

1. **PDF Conversion:**  
   The script converts each page of the input PDF into high-resolution images using `pdf2image`.

2. **Image Pre-Processing:**  
   Each page is processed in color:
   - **Contrast & Brightness Enhancement:** Adjusts image quality without converting to grayscale.
   - **Denoising:** Uses a color-preserving denoising filter to reduce noise.

3. **Reassembly:**  
   The processed images are reassembled into a new PDF, maintaining the original color.

4. **OCR Application:**  
   OCRmyPDF adds an invisible text layer to the preprocessed PDF. This makes the document searchable and selectable without altering its visual appearance.

## Setup

1. **Install Python Packages:**
   ```bash
   pip install ocrmypdf pdf2image opencv-python numpy Pillow