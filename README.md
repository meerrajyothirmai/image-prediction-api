\# Image Prediction API



A simple Image Prediction API built using FastAPI and Scikit-learn.



\## Features



\- Upload images

\- Process images using PIL and NumPy

\- Predict using a trained machine learning model

\- Interactive API documentation with Swagger UI



\## Installation



```bash

pip install -r requirements.txt

```



\## Run the Application



```bash

uvicorn app:app --reload

```



\## API Documentation



\### Base URL



```

http://127.0.0.1:8000

```



\### Endpoints



\#### GET /



Returns the API status.



\*\*Response:\*\*



```json

{

&#x20; "message": "Image Prediction API is running"

}

```



\#### POST /predict



Uploads an image and returns a prediction.



\*\*Response:\*\*



```json

{

&#x20; "filename": "image.png",

&#x20; "prediction": 3

}

```



\### Interactive Documentation



Visit:



```

http://127.0.0.1:8000/docs

```



\## Technologies Used



\- Python

\- FastAPI

\- Scikit-learn

\- NumPy

\- Pillow

\- Uvicorn



\## Project Structure



```text

image\_prediction\_api/

│

├── app.py

├── train\_model.py

├── model.pkl

├── requirements.txt

└── README.md

```

