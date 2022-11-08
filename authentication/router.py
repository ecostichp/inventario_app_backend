# Se importan las librerías necesarias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from . import crud, schema

from database.orm import get_db


# Se instancía la clase para generar el objeto 'router'
router = APIRouter(
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)



# Se contruyen todas las rutas y debajo de ellas el end-point
@router.post("/login/", response_model = schema.Authentication)
def create_authentication(schema: schema.AuthenticationCreate, db: Session = Depends(get_db)):

    return crud.create_authentication(db, schema = schema)


@router.get("/logout", response_model = schema.Authentication)
def delete_authentication(db: Session = Depends(get_db)):

    return crud.delete_authentication(db)