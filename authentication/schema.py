from pydantic import BaseModel


# Con este esquema se comunicará lo necesario para el modelo Cursos.
class AuthenticationBase(BaseModel):
    usuario: str


class AuthenticationCreate(AuthenticationBase):
    contraseña: str


class Authentication(AuthenticationBase):
    id: int
    activo: bool

    class Config:
        orm_mode = True
