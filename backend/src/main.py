from fastapi import FastAPI, Form, UploadFile, File
from extractor import extract
import uvicorn
import uuid
import os

app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(
        file_type: str = Form(...),
        file: UploadFile = File(...),
):
    content = file.file.read()

    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"
    with open(file_path, "wb") as f:
        f.write(content)

    try:
        extracted_data = extract(file_path, file_type)
    except Exception as e:
        return {"error": str(e)}

    if os.path.exists(file_path):
        os.remove(file_path)
    return extracted_data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)