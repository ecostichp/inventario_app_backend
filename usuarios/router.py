# Se importan las librerías necesarias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from . import crud, schema

from database.orm import get_db


# Se instancía la clase para generar el objeto 'router'
router = APIRouter(
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)



# Se contruyen todas las rutas y debajo de ellas el end-point
@router.get("/", response_model=list[schema.Usuarios])
def get_read_all_usuarios(db: Session = Depends(get_db)):

    usuarios = crud.read_all_usuarios(db)

    return usuarios



@router.post("/crear_usuario/", response_model = schema.Usuarios)
def post_crear_usuario(schema: schema.UsuariosCreate, db: Session = Depends(get_db)):

    return crud.create_usuario(db, schema = schema)