from scr.db.models import init_db
from scr.db.routes.all_routes import router
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def init_process():
    init_db()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= "0.0.0.0" , port=8000, reload=True)