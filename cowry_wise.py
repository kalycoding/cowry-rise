from fastapi import FastAPI
import uuid
import datetime


app = FastAPI()

item = {}

@app.post('/cowry/')
def generate_uuid():
    item[datetime.datetime.now()] = uuid.uuid1()
    return item
