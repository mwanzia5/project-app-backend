from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {"message":"My first Api"}


@app.get('/cakes')
def cakes():
     return[]
@app.post("/cakes")
def create_cake():
     return {"message":"Data recieved"}
@app.patch('/cakes/{cake_id}')
def updated_event(cake_id:int):
     return{"message":f"Event{cake_id} created successfully"}

@app.delete('/cakes/{cake_id}')
def delete_event(cake_id:int):
     return{"message":f"Event{cake_id}deleted"}