from fastapi import FastAPI
from app.routers import tasks, auth

app = FastAPI(title="API de Gestão de Tarefas")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"msg": "API de Gestão de Tarefas - João Vitor Ferreira"}
