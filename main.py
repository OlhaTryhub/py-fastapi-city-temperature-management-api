from fastapi import FastAPI

# from cheese import router as cheese_router
from city import router as city_routers
from temperature import router as temperature_routers

app = FastAPI()

# app.include_router(cheese_router.router)
app.include_router(city_routers.router)
app.include_router(temperature_routers.router)


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}