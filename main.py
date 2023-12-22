from fastapi import FastAPI,Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Cake,User,Booking
from display import Cakedisplay,Userdisplay,Bookingdisplay

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
    )



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
     cake = db.query(Cake),filter(Cake.id == cake_id).first()
     return cake
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
def delete_cake(cake_id:int ,db:Session=Depends(get_db)):
      delete_event = db.query(Cake).filter(Cake.id == cake_id).first()
     
      if delete_event == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cake {cake_id} does not exist")
      else:
        delete_cake.delete()
        
        db.commit()

      return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post('/booking')
def book(booking: Bookingdisplay, db: Session = Depends(get_db)):
    # 1. Check if user exists using the phone number
    user = db.query(User).filter(User.phone == booking.phone).first()

    if user == None:
        # this means the user doesn`t exist so we create
        user = User(name=booking.name, phone=booking.phone)
        db.add(user)
        db.commit()

        # after creating user, now we can create a booking
        saved_booking = Booking(booking_date=booking.booking_date,
                          user_id= user.id,
                          event_id = booking.event_id)

        db.add(saved_booking)
        db.commit()

    else:
        # check if the user has already booked for an event
        saved_booking = db.query(Booking).filter(Booking.user_id == user.id,
                                           Booking.event_id == booking.event_id).first()

        if saved_booking == None:
            # this means the user has not booked the event
            saved_booking = Booking(booking_date=booking.booking_date,
                          user_id= user.id,
                          event_id = booking.event_id)

            db.add(saved_booking)
            db.commit()
        else:
            # if the user already has a booking we throw an error
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Event already booked")


    return {"message": "Event booked successfully"}