from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


from database.orm import Base



# Con este modelo, se genera la tabla usuarios en la base de datos del proyecto.
class Authentications(Base):
    __tablename__ = 'authentications'

    id = Column(Integer, primary_key=True, index=True)
    usuarios_id = Column(String(16,), ForeignKey("usuarios.id"))
    contraseña_hashed = Column(String(128,), nullable=False)

    usuarios_rel_authentications = relationship("Usuarios", back_populates="authentication_rel_usuarios")
