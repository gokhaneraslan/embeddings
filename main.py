from fastapi import FastAPI, Body
from base64 import b64decode
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ad_to_db import main_data


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str

@app.get("/")
async def root():
    return {
        "Message": "Hello World!"
    }
    
@app.post("/api/document")
async def post_document(file: str = Body(...)):
    b64 = file
    bytes = b64decode(b64, validate=True)

    if bytes[0:4] != b'%PDF':
        raise ValueError('Missing the PDF file signature')

    f = open('data/test.pdf', 'wb')
    f.write(bytes)
    f.close()
    
    db_chroma = main_data()
    
    print("We are ready!")
    
    return db_chroma
