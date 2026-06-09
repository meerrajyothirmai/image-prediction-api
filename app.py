
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import pickle

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Image Prediction API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("L")
    image = image.resize((8, 8))

    img_array = np.array(image)
    img_array = img_array.flatten().reshape(1, -1)

    prediction = model.predict(img_array)

    return {
        "filename": file.filename,
        "prediction": int(prediction[0])
    }