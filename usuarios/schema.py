from pydantic import BaseModel


# Con este esquema se comunicará lo necesario para el modelo Cursos.
class UsuariosBase(BaseModel):
    usuario: str
    nombre_1ro: str
    nombre_2do: str | None
    apellido_paterno: str
    apellido_materno: str
    almacen: int
    foto: str


class UsuariosCreate(UsuariosBase):
    pass


class Usuarios(UsuariosBase):
    id: int
    estatus: bool

    class Config:
        orm_mode = True
