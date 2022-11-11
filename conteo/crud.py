from sqlalchemy.orm import Session


from . import model, schema



def read_all_productos(db: Session):
    return db.query(model.Productos).all()
