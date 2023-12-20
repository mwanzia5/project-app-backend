from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://admin:TmWcv7JVIIuiBTRWYpAEICrwPmYQ0BxC@dpg-cm1bumi1hbls73agcsu0-a.frankfurt-postgres.render.com/cakes_paah",
                      echo=True   )
 

sessionLocal = sessionmaker(bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()    