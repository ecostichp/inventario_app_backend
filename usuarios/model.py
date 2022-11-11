from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


from database.orm import Base



# Con este modelo, se genera la tabla usuarios en la base de datos del proyecto.
class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(16,), nullable=False, unique=True, index=True)
    estatus = Column(Boolean, nullable=False, default=True, index=True)
    nombre_1ro = Column(String(16,), nullable=False, index=True)
    nombre_2do = Column(String(16,), index=True)
    apellido_paterno = Column(String(16,), nullable=False, index=True)
    apellido_materno = Column(String(16,), nullable=False, index=True)
    almacen = Column(Integer, nullable=False, index=True)
    foto = Column(String(16,), index=True)

    authentication_rel_usuarios = relationship("Authentications", back_populates="usuarios_rel_authentications")