from fastapi import FastAPI
import models
from database import engine
from routers import auth,expense,user
models.Base.metadata.create_all(bind = engine)
app = FastAPI()

app.include_router(expense.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/") 
def index():
    return {"message": "Go to the documentation :)"}

