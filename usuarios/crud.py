from sqlalchemy.orm import Session


from . import model, schema


def read_usuario_by_id(db: Session, id: int):
    return db.query(model.Usuarios).filter(model.Usuarios.id == id).first()


def read_usuario_by_usuario(db: Session, usuario: str):
    return db.query(model.Usuarios).filter(model.Usuarios.usuario == usuario).first()


def read_all_usuarios(db: Session):
    return db.query(model.Usuarios).all()
