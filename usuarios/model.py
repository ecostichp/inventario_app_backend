from sqlalchemy import Column, VARCHAR, INTEGER, SMALLINT, BOOLEAN
from sqlalchemy.orm import relationship


from database.orm import Base



# Con este modelo, se genera la tabla usuarios en la base de datos del proyecto.
class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(INTEGER, primary_key=True, index=True)
    usuario = Column(VARCHAR(16,), nullable=False, unique=True, index=True)
    estatus = Column(BOOLEAN, nullable=False, default=True, index=True)
    nombre_1ro = Column(VARCHAR(16,), nullable=False, index=True)
    nombre_2do = Column(VARCHAR(16,), index=True)
    apellido_paterno = Column(VARCHAR(16,), nullable=False, index=True)
    apellido_materno = Column(VARCHAR(16,), nullable=False, index=True)
    almacen = Column(SMALLINT, nullable=False, index=True)
    foto = Column(VARCHAR(16,), index=True)

    authentication_rel_usuarios = relationship("Authentications", back_populates="usuarios_rel_authentications")