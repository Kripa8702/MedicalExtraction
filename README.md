# Medical Prescription Data Extraction
This project is a part of the course "Python Beginner to Advanced" from Codebasics The goal of the project is to extract information from medical prescriptions and patient details documents in form of separate data fields.

## Extracting information from the prescription
The prescription is in the form of an image. The information to be extracted from the prescription includes:

- patient_name
- patient_address
- medicine
- directions
- refill

## Extracting information from the patient details
The patient details are in the form of a PDF. The information to be extracted from the patient details includes:
- patient_name
- patient_phone
- hepatitis_b_vaccination
- medical_problems

## Tools used
- Tesseract OCR
- Pytesseract
- OpenCV
- FastAPI
- Pydantic
- Uvicorn
- Pytest