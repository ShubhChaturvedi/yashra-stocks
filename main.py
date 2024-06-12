from typing import Union
from fastapi import Request
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import Service

app = FastAPI()
from db import connect_to_mongodb

client = connect_to_mongodb()
db = client["service_db"]
collection = db["services"]

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/add-service")
def add_service(request: Request):
    return templates.TemplateResponse("add_service.html", context={"request": request})

@app.post("/add-service")
def add_service(request: Request, service: Service):
    service = service.dict()
    collection.insert_one(service)
    return templates.TemplateResponse("add_service.html", context={"request": request, "service": service})

@app.get("/get-service")
def get_service():
    services = collection.find()
    return {"services": services}

@app.get("/get-service/{service_name}")
def get_service_by_name(service_name: str):
    service = collection.find_one({"service_name": service_name})
    return service

@app.put("/update-service/{service_name}")
def update_service(service_name: str, service: Service):
    collection.update_one({"service_name": service_name}, {"$set": service.dict()})
    return service.dict()

@app.delete("/delete-service/{service_name}")
def delete_service(service_name: str):
    collection.delete_one({"service_name": service_name})
    return {"message": "Service deleted successfully!"}
    
