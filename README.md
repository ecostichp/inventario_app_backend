# IACele Inventario APP

Este código es la porción del backend del microservicio de la app IACele que controla el inventario. Se desarrolla en el framework FastAPI.



### 1. Crea un entorno en python.
```
python -m venv 'nombre_env'
'nombre_env'\Scripts\activate
```


### 2. Instalar las siguientes dependencias del proyecto.
```
python -m pip install -U Pip  
python -m pip install -U Uvicorn FastAPI Psycopg2 SQLAlchemy PyDantic Pandas OpenPyXL
```

### 3. Inicia el servidor.
```
uvicorn main:app --reload
```


## La base de datos.
Se va a utilizar SQLite como el motor de la base de datos. Puedes configurar nombre y dirección de esta base de datos dentro del archivo 'database/orm.py'.