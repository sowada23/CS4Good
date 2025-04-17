import ocrmypdf
import os
from pdf2image import convert_from_path
import cv2
import numpy as np
from PIL import Image

# Input and output file paths
input_pdf = "./data/ErnestARice.pdf"          # Your original newspaper PDF
preprocessed_pdf = "prepErnestARice.pdf"
output_pdf = "ErnestARice.pdf"

print("Converting PDF pages to images...")
# Convert PDF pages to images using 300 DPI for high quality
pages = convert_from_path(input_pdf, dpi=300)
processed_images = []

# Process each page while preserving color
for idx, page in enumerate(pages):
    # Convert PIL image to a NumPy array (initially in RGB order)
    img = np.array(page)
    # OpenCV works in BGR, so convert to BGR for processing
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Apply contrast and brightness enhancement without converting to grayscale.
    # Adjust 'alpha' (contrast multiplier) and 'beta' (brightness offset) as needed.
    alpha = 1.2  # Contrast control: 1.0 means no change, >1 increases contrast
    beta = 10    # Brightness control: positive values increase brightness
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    
    # Apply denoising while preserving color details
    denoised = cv2.fastNlMeansDenoisingColored(adjusted, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)
    
    # Convert back to RGB for saving with PIL
    processed_page = cv2.cvtColor(denoised, cv2.COLOR_BGR2RGB)
    processed_page = Image.fromarray(processed_page)
    processed_images.append(processed_page)

# Save all processed images back into a single PDF
if processed_images:
    processed_images[0].save(
        preprocessed_pdf, "PDF", resolution=300, save_all=True, append_images=processed_images[1:]
    )
print("Preprocessing complete. Processed PDF saved as:", preprocessed_pdf)

# Now run OCRmyPDF on the preprocessed colored PDF.
# This will add an invisible text layer while preserving the original colored appearance.
try:
    print("Processing OCR on the preprocessed PDF...")
    ocrmypdf.ocr(
        preprocessed_pdf,
        output_pdf,
        deskew=True,              # Corrects skewed scans
        optimize=1,               # Optimizes file size
        force_ocr=True,           # Forces OCR even if a text layer already exists
        language="eng",           # Set language to English
        tesseract_pagesegmode=1   # Set Tesseract's page segmentation mode (adjust if needed)
    )
    print("OCR complete! Processed file saved as:", output_pdf)
except Exception as e:
    print("Error during OCR:", e)