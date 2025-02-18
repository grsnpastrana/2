from fastapi import FastAPI, HTTPException

from typing import Optional

app = FastAPI(
    title="Mi Primer API 192",
    description="Gerson Pastrana",
    version="1.0.1",
)

usuarios = [
    {"id": 1, "nombre": "Ivan", "edad": 37},
    {"id": 2, "nombre": "Carlos", "edad": 15},
    {"id": 3, "nombre": "María", "edad": 18},
    {"id": 4, "nombre": "Lucía", "edad": 37},
]

# Endpoint home
@app.get("/", tags=["Hola Mundo"])
def home():
    return {"hello": "world FastAPI"}

# End point consulta todos 
@app.get('/todosUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    return{'Los usuarios registrados son ': usuarios}

# End point agregar nuevos
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya existe")
    usuarios.append(usuario)
    return usuario  


# End point para actualizar un usuario
@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizarUsuario(id: int, usuario_actualizado: dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuario_actualizado)
            return {"mensaje": "Usuario actualizado correctamente", "usuario": usuarios[index]}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

    
# End point para eliminar un usuario

@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarUsuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"mensaje": "Usuario eliminado correctamente"}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
