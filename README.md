# IACele Inventario APP

Este código es la porción del backend del microservicio de la app IACele que controla el inventario. Se desarrolla en el framework FastAPI.



### 1. Actualiza PIP en python.
```
python -m pip install -U Pip  
```

### 2. Crea un entorno para el proyecto.
```
python -m venv env
env\Scripts\activate
```


### 3. Actualiza PIP en tu entorno e instala las dependencias del proyecto.
```
python -m pip install -U Pip  
python -m pip install -U Uvicorn FastAPI Psycopg2 SQLAlchemy PyDantic Pandas OpenPyXL iPYKernel
```

### 4. Inicia el servidor.
```
uvicorn main:app --reload
```
Si quieres iniciar el servidor en otro host (ej: 192.168.1.82):
```
uvicorn main:app --reload  --host 192.168.1.82
```


## La base de datos.
Se va a utilizar SQLite como el motor de la base de datos. Puedes configurar nombre y dirección de esta base de datos dentro del archivo 'database/orm.py'.