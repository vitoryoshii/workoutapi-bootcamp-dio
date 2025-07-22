from fastapi import FastAPI
from workoutapi.app.routers import api_router

app = FastAPI(title='WorkoutAPI')
app.include_router(api_router)