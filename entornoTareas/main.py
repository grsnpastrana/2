from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Gestión de Tareas",
    description="Una API para gestionar una lista de tareas.",
    version="1.0.0",
)

# Base
tareas = [
    {"id": 1,
     "titulo": "Estudiar para el examen", 
     "descripcion": "Repasar los apuntes de TAI", 
     "vencimiento": "12-02-25", 
     "estado": "completada"},
    {"id": 2,
     "titulo": "hacer tarea de TAI", 
     "descripcion": "generar reporte de actividad", 
     "vencimiento": "25-02-25", 
     "estado": "proceso"},
    {"id": 3,
     "titulo": "hacer tarea de pons", 
     "descripcion": "busquedas de nodos", 
     "vencimiento": "27-03-25", 
     "estado": "proceso"},
    {"id": 4,
     "titulo": "Estudiar para el examen", 
     "descripcion": "Repasar los apuntes de TAI", 
     "vencimiento": "11-03-25", 
     "estado": "pendiente"},
]

# Endpoint home
@app.get("/", tags=["Inicio"])
def home():
    return {"mensaje": "Bienvenido"}


@app.get("/todasTareas", tags=["Operaciones CRUD"])
def obtener_tareas():
    return {"Las tareas registradas son": tareas}

# nueva tarea
@app.post("/tarea/", tags=["Operaciones CRUD"])
def crear_tarea(tarea: dict):
    for t in tareas:
        if t["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
    tareas.append(tarea)
    return tarea

# Obtener id
@app.get("/tarea/{id}", tags=["Operaciones CRUD"])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
