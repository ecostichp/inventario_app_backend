from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


from database.orm import Base



# Con este modelo, se genera la tabla usuarios en la base de datos del proyecto.
class Productos(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(16,), nullable=False, unique=True, index=True)
    descripcion = Column(String(124,), nullable=False, index=True)
    cantidad = Column(Float(2,), nullable=False)
    ultimo_costo = Column(Float(2,), nullable=False)