from pdf2image import convert_from_path
import pytesseract
import utils

from backend.src.parser_prescription import ParserPrescription
from backend.src.parser_patient_details import ParserPatientDetails

POPPLER_PATH = "C:/poppler-24.08.0/Library/bin"
TESSERACT_PATH =  "C:/Program Files/Tesseract-OCR/tesseract.exe"

def extract(file_path, file_type):
    # Step-1: Extract text from the image
    extracted_text = ""
    if file_type == "prescription":
        extracted_text = extract_prescription(file_path)
    elif file_type == "patient_details":
        extracted_text = extract_patient_details(file_path)
    else:
        raise Exception("Invalid file type : {}".format(file_type))

    # Step-2: Parse the text
    if file_type == "prescription":
        extracted_data = ParserPrescription(extracted_text).parse()
    elif file_type == "patient_details":
        extracted_data = ParserPatientDetails(extracted_text).parse()
    else:
        raise Exception("Invalid file type : {}".format(file_type))

    return extracted_data

def extract_prescription(file_path):
    document_text = ""
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    
    if len(pages) > 0:
        processed_img = utils.preprocess_image(pages[0])
        text = pytesseract.image_to_string(processed_img, lang='eng')
        document_text = "\n" + text

    return document_text


def extract_patient_details(file_path):
    document_text = ""
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    if len(pages) > 0:
        processed_img = utils.preprocess_image(pages[0])
        text = pytesseract.image_to_string(processed_img, lang='eng')
        document_text = "\n" + text

    return document_text

if __name__ == "__main__":
    pre_1 = extract(r"..\resources\prescription\pre_1.pdf", "prescription")
    print(pre_1)

    pd_1 = extract(r"..\resources\patient_details\pd_1.pdf", "patient_details")
    print(pd_1)

        