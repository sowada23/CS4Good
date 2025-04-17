# 📰 Newspaper OCR Enhancement & Text-Layering Tool

This project enhances the readability and text extraction capability of scanned newspaper PDFs. It first applies color-preserving image preprocessing and then adds an invisible OCR-based text layer so that users can search and copy text from the resulting PDF without altering the original visual appearance.

---

## 📌 Features

✅ High-resolution image conversion (300 DPI)  
✅ Color-preserving contrast enhancement & denoising  
✅ Image reassembly into a PDF while maintaining full color  
✅ Text-layer embedding using ocrmypdf  
✅ Searchable and selectable final PDF output

---

## 📅 Requirements

Python 3.x  

**Python packages:**
- `ocrmypdf`
- `pdf2image`
- `opencv-python`
- `numpy`
- `Pillow`

**Poppler utilities:**
- macOS: `brew install poppler`
- Ubuntu: `sudo apt-get install poppler-utils`

---

## 🔍 Main Function Explanations ##

- `convert_from_path()`
: Converts PDF pages to high-resolution color images
- `cv2.convertScaleAbs()`
: Enhances contrast and brightness
- `cv2.fastNlMeansDenoisingColored()`
: Denoises while preserving color
- `Image.fromarray()`
: Converts NumPy array back to PIL image for saving
- `ocrmypdf.ocr()`
: Adds an invisible, selectable OCR text layer to the PDF

---

## Results

<table style="width:100%; margin:auto;">
  <tr>
    <th style="text-align:center;">After preparation</th>
    <th style="text-align:center;">After ocr</th>
  </tr>
  <tr>
    <td align="center">
      <img src="./Output/Output/prepErnestARice.pdf" width="330" />
    </td>
    <td align="center">
      <img src="./Output/Output/ErnestARice.pdf" width="330" />
    </td>
  </tr>
</table>

---


## 🔄 How to Run

1. Place the original scanned newspaper PDF in the `./data` folder.  
2. Update the file name in the script (`input_pdf` variable).  
3. Run the Python script:

   ```bash
   python ocr_newspaper.py