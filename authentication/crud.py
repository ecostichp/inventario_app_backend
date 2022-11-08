from sqlalchemy.orm import Session


from . import model, schema



def create_usuario(db: Session, schema: schema.UsuariosCreate):
    usuario = model.Usuarios(
        usuario = schema.usuario,
        nombre_1ro = schema.nombre_1ro,
        nombre_2do = schema.nombre_2do,
        apellido_paterno = schema.apellido_paterno,
        apellido_materno = schema.apellido_materno,
        almacen = schema.almacen,
        foto = schema.foto,
        contraseña = schema.contraseña,
        )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario



def read_usuario_by_id(db: Session, id: int):
    return db.query(model.Usuarios).filter(model.Usuarios.id == id).first()


def read_usuario_by_usuario(db: Session, usuario: str):
    return db.query(model.Usuarios).filter(model.Usuarios.usuario == usuario).first()


def read_all_usuarios(db: Session):
    return db.query(model.Usuarios).all()
