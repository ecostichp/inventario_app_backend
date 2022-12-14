from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



dbtest = 'database/inventario.db'



SQLALCHEMY_DATABASE_URL = f"sqlite:///{dbtest}"
engine = create_engine( SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} )



Base = declarative_base()



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()