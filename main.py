from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {"message":"My first Api"}

#get all events
@app.get('/cakes')
def cakes():
     return[]
#get a single event
@app.get('/cakes/{cake_id}')
def cakes():
     return[]
#create an event
@app.post("/cakes")
def create_cake():
     return {"message":"Data recieved"}
#update an event
@app.patch('/cakes/{cake_id}')
def updated_cake(cake_id:int):
     return{"message":f"Event{cake_id} created successfully"}
#delete an event
@app.delete('/cakes/{cake_id}')
def delete_cake(cake_id:int):
     return{"message":f"Event{cake_id}deleted"}