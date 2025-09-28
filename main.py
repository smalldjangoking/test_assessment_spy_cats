from fastapi import FastAPI
from router import cats, agency, spies
app = FastAPI()

@app.get("/")
async def read_root():
    return {"info": "/docs to see all endpoints"}

app.include_router(cats.router)
app.include_router(agency.router)
app.include_router(spies.router)