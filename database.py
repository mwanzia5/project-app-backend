from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://admin:TmWcv7JVIIuiBTRWYpAEICrwPmYQ0BxC@dpg-cm1bumi1hbls73agcsu0-a.frankfurt-postgres.render.com/cakes_paah")

sessionLocal = sessionmaker(bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()    