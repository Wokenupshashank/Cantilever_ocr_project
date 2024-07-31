from PIL import Image
import pytesseract

def extract_text(image_path):
    """
    Extract text from an image using Tesseract OCR.
    :param image_path: Path to the image file
    :return: Extracted text
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    sample_image_path = 'sample_image.png'
    print(extract_text(sample_image_path))
