from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from file_handler import load_file, sample_columns
from llm_classifier import classify_columns

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        df = load_file(file)
        samples = sample_columns(df)
        classification = classify_columns(samples)
        return {"status": "success", "classification": classification}
    except Exception as e:
        return {"status": "error", "message": str(e)}
