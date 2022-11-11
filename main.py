# Se importan las librería necesaria para la aplicación
from fastapi import FastAPI

# Se instancía la clase para generar el objeto 'app'. Este es el módulo principal.
app = FastAPI()



# Se importan las librería necesaria para el manejo del CORS
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Se importan las librería necesaria para el manejo de la descarga de archivos estáticos
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")



# Se importan los sub-modulos router y debjo de incluyen al módulo principal.
from usuarios import router as usuarios
app.include_router(usuarios.router)

from authentication import router as authentication
app.include_router(authentication.router)

from conteo import router as conteo
app.include_router(conteo.router)


# Se crean todas las tablas en la base de datos del proyecto.
from database.orm import Base, engine
Base.metadata.create_all(bind = engine)