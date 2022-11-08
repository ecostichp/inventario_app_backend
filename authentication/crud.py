from sqlalchemy.orm import Session


from . import model, schema



def create_authentication(db: Session, schema: schema.AuthenticationCreate):
    authentication = model.Authentications(
        usuarios_id = schema.usuarios_id,
        contraseña_hashed = schema.contraseña_hashed
        )
    db.add(authentication)
    db.commit()
    db.refresh(authentication)

    return authentication



def read_authentication_by_id(db: Session, id: int):
    return db.query(model.Authentications).filter(model.Authentications.id == id).first()


def read_all_authentications(db: Session):
    return db.query(model.Authentications).all()
