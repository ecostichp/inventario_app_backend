# Se importan las librerías necesarias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


from . import crud, schema

from database.orm import get_db


# Se instancía la clase para generar el objeto 'router'
router = APIRouter(
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)



# Se contruyen todas las rutas y debajo de ellas el end-point
@router.get("/usuarios", response_model=list[schema.Usuarios])
def get_read_all_usuarios(db: Session = Depends(get_db)):

    return crud.read_all_usuarios(db)