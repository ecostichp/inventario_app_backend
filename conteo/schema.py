from pydantic import BaseModel


# Con este esquema se comunicará lo necesario para el modelo Cursos.
class ProductosBase(BaseModel):
    codigo: str
    descripcion: str
    cantidad: float
    ultimo_costo: float


class ProductosCreate(ProductosBase):
    pass


class Productos(ProductosBase):
    id: int

    class Config:
        orm_mode = True
