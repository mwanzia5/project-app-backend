from pydantic import BaseModel

class Cakedisplay(BaseModel):
    type:str
    description:str
    image:str
    size:int
    price:int
    date:str

class Userdisplay(BaseModel):
    name: str
    phone: str

class Bookingdisplay(BaseModel):
    cake_id: int
    name: str
    phone: str
    booking_date: str
