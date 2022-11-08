from pydantic import BaseModel


# Con este esquema se comunicará lo necesario para el modelo Cursos.
class AuthenticationBase(BaseModel):
    usuarios_id: int
    activo: bool


class AuthenticationCreate(AuthenticationBase):
    contraseña_hashed: str


class Authentication(AuthenticationBase):
    id: int

    class Config:
        orm_mode = True
