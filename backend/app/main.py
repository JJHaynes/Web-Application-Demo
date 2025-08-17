from fastapi import FastAPI
from .api.routers import auth, charities, roles, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"message": "Hello, World"}

app.include_router(auth.router)
app.include_router(charities.router)
app.include_router(roles.router)
app.include_router(users.router)