from pydantic import BaseModel


# Con este esquema se comunicará lo necesario para el modelo Cursos.
class UsuariosBase(BaseModel):
    usuario: str
    nombre_1ro: str
    nombre_2do: str
    apellido_paterno: str
    apellido_materno: str
    almacen: int
    foto: str


class UsuariosCreate(UsuariosBase):
    contraseña: str


class Usuarios(UsuariosBase):
    id: int

    class Config:
        orm_mode = True
