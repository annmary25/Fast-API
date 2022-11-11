import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Addressbook(BaseModel):
    person_name: str
    address: str

## Converting address to latitude and longitude
from geopy.geocoders import Nominatim
def convert_address_to_coordinates(address):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)
    return (location.latitude, location.longitude)

## Distance between 2 points
import math
math.dist([10],[10])

@app.get("/get_address_by_distance/{id}")
#def get_address_by_distance(distance: float = Path(None, description="", gt=0)):
def get_address(id) 
   return {"id": id, "person_name": person_name, "address": address}

### Creating data
@app.post("/addressbook/")
def create_address(id:int, addressbook:Addressbook):
    return addressbook

#### Updating data
@app.put("/addressbook/{id}")
def update_address(id: int, item:Addressbook):
    return {"id": id, "Name": item.person_name, "Address": item.address_coordinates}

@app.delete("/addressbook/{id}")
def delete_address(id: int):
    return {"deletion done"}

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8000)
