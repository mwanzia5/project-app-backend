from pydantic import BaseModel

class Cakedisplay(BaseModel):
    type:str
    description:str
    image:str
    size:int
    price:int
    date:str
