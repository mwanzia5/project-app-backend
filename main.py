from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Cake
from display import Cakedisplay

app = FastAPI()


@app.get("/")

def index():
    return {"message":"My first Api"}

#get all events
@app.get('/cakes')
def cakes(db :Session = Depends(get_db)):
     cakes = db.query(Cake).all()
     return cakes
#get a single event
@app.get('/cakes/{cake_id}')
def cakes(cake_id:int,db:Session= Depends(get_db)):
     event = db.query(Cake),filter(Cake.id == cake_id)
     return[]
#create an event
@app.post("/cakes")
def create_cake(cake: Cakedisplay,db:Session = Depends(get_db)):
     new_cake=(Cake(**cake.model_dump()))
     db.add(new_cake)
     db.commit()
     db.refresh(new_cake)
     return {"message":"Data recieved","cake":new_cake}
#update an event
@app.patch('/cakes/{cake_id}')
def updated_cake(cake_id:int):
     return{"message":f"Event{cake_id} created successfully"}
#delete an event
@app.delete('/cakes/{cake_id}')
def delete_cake(cake_id:int):
     return{"message":f"Event{cake_id}deleted"}